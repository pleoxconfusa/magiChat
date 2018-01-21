"""
       o          o
        \   /\   /
         \ /* \ /
          (__*_)
    _______(oo) - I am Alfonso.
   /|  ___  \/
  / | {M U}||
 *  ||{_M_}||
    ||-----||
    ^^     ^^
    
BEHOLD, ALFONSO: OUR MAGIC COW!


This program is a PoC for a future package class.  The MMU program implements
the use of Pan-Magic Squares as a coding mechanism for 8-bit data.  The traditional
single-error correcting coding schema for 8-bit data is 17-bits long and allows 
for 1 error at a maximum sustainable error rate of 1 in 17.  Using magic squares
with error-detecting coding schemas, an 80-bit translation can be made.  A 
pan-magic square can be seen below:

| 2  5 11 12|
|15  8  6  1|
| 4  3 13 10|
| 9 14  0  7|

Using rules for pan-magic square construction, this square could be reconstructed
with the following worst-case input:

| 2  *  * 12|
| *  8  *  *|
| *  * 13  *|
| *  *  *  7|

There are 192 pan-magic squares, which is 64 short of 256, but we attempt a best
match for our reconstruction method, with priority given to values 0-192.  Our
values 193-256 are not pan-magic squares, so they require at least 9 matches.

To attain a magic square with possible accept and deny values, we encode the
required 4-bit 0-16 value as a 5-bit error detecting even parity value.

The resulting coding schema translates 8-bits to 80-bits rather than 17-bits, but
allots for a floor of 11 bits lost of 80 for 3/4 of data, and a floor off 6
bits lost of 80 for 1/4 of data, or an average floor of 12.1% data loss.

As shown in the documentation for reconstruct, the floor for error loss if worst
case bits are lost is 7.5%, and if best case bits are lost, is 68.75%

In future iterations beyond PoC we plan to implement data validation, user
error detection, and an efficient coding mapping of non-pan-magic squares to
infrequent mapped data (in other words, applying the codes with a floor of 7.5%
data loss to the most infrequently occurring data, and a floor of 12.5% data
loss to the rest).  

Defaults:
    ERR_DET_MAPPING -- This is a dictionary that converts 0 to 15 into a 5-bit
        even parity error detecting bitstring.
    ERR_DET_MAP_REV -- This is a dictionary that converts 5-bit even parity
        error detecting bitstrings to their corresponding 0 to 15 value.

Functions:
    MMU_decode -- Takes a bitstring message of length %80 = 0 and finds
        corresponding 0 to 255 (unicode for this PoC) values for the most likely 
        magic square. If no likely magic square exists for a given character, it
        is left blank.
    reconstruct -- Takes a partial or non-matching magic square and returns the
        most likely character, which, if error rate < 7.5% is guaranteed to be
        accurate.  If error rate < 12.5% is 75% likely to be accurate.  If
        error rate < 68.75%, it will provide a matching for at least some 
        characters.
    MMU_encode -- Takes a list of 0 to 255 values (string in our case) and finds
        corresponding magic squares as bitstrings of length 80.  It then appends
        these bitstrings together for a data transmission that will be decoded
        by MMU_decode


    
"""

from bitstring import BitArray
from MMU_load_coding import *

ERR_DET_MAPPING = { 0: "00000", 1: "00011", 2: "00101", 3: "00110", 4: "01001", 
5: "01010", 6: "01100", 7: "01111", 8: "10001", 9: "10010", 10: "10100",
11: "10111", 12: "11000", 13: "11011", 14: "11101", 15: "11110"}

ERR_DET_MAP_REV = {"00000": 0, "00011" : 1, "00101" : 2, "00110" : 3, "01001" : 4, 
"01010" : 5, "01100" : 6, "01111" : 7, "10001" : 8, "10010" : 9, "10100" : 10, 
"10111" : 11, "11000" : 12, "11011" : 13, "11101" : 14, "11110" : 15}

DEF_ENCODING_SCHEME = load_encoding()
DEF_DECODING_SCHEME = load_decoding()

    
def reconstruct(square, scheme_dict):
    """ This function takes a scheme dictionary of magic squares and tries
    to find the most likely matching based on a corrupt square that is not
    able to be found.

    Args:
        Required:
            square -- a tuple of ints of size n^2.
            scheme_dict -- a dictionary of tuples that correspond to 0 to 255 values.
        Optional:
            None

    Returns:
        The most likely square 0 to 255 value in the dictionary for the given 
        square.  If all keys are more dissimilar than similar, no value is returned.
    """
    highest_sim = 0
    sim_key = ""
    
    for key in scheme_dict.keys():
        sim_count = 0
        
        for i in range(len(square)):
            if square[i] is not -1:
                if square[i] == key[i]:
                    sim_count = sim_count + 1
                else:
                    sim_count = sim_count - 1
                    
        if sim_count > highest_sim:
            sim_key = key
            highest_sim = sim_count
        
    if sim_key is "":
        return ""
    else:
        return scheme_dict.get(sim_key)
        
def MMU_decode(message, scheme_dict=DEF_DECODING_SCHEME):
    """ This function takes a bitstring of length %80 = 0 and converts it into
    bitstrings of length 80, which get converted into error-detecting magic
    squares.  The error-detecting magic squares are keys in a coding schema
    for 0 to 255 values, and the most likely match is found for each square, 
    giving a unicode string output.

    Args:
        Required:
            message -- a message bitstring of length %80 = 0
        Optional:
            scheme_dict -- a separate scheme dictionary can be selected here.

    Returns:
        A decoded message (a string for this PoC)
    """
    output = "" 

    bitstr = BitArray(bytes=message).bin

    characters = []
    for i in range(int(len(message)/10)):
        #keep iterating until end of message. this can be found as i in range(len(message)/10)
        cur_char = []
        for j in range(16):
            cur_char.append(bitstr[i*80+5*j: i*80+5*(j+1)])
            #this is initially populates with collections of len16 lists of 5bit bitstrings
            #append to characters a list
            #   in this list is 16 5 bit bitstrings
        characters.append(cur_char) #may have to copy this list because of garbage collection

    for c in characters:
        for i in range(16):
            if c[i] not in ERR_DET_MAP_REV.keys():
                c[i] = -1
            else:
                c[i] = ERR_DET_MAP_REV.get(c[i])
        c_tup = tuple(c)
        if c_tup not in scheme_dict.keys():
            output = output+reconstruct(c_tup,scheme_dict)
        else:
            output = output + scheme_dict.get(c_tup)




    return output
    
    
def MMU_encode(data, scheme_dict=DEF_ENCODING_SCHEME):
    """ This function takes a bitstring of length %80 = 0 and converts it into
    bitstrings of length 80, which get converted into error-detecting magic
    squares.  The error-detecting magic squares are keys in a coding schema
    for 0 to 255 values, and the most likely match is found for each square, 
    giving a unicode string output.

    Args:
        Required:
            data -- a list of 0-255 values (a string for this PoC)
        Optional:
            scheme_dict -- a separate scheme dictionary can be selected here.

    Returns:
        An encoded bitstring of length 80*len(data)
    """
    st = ''
    for char in data:
        magic = scheme_dict.get(ord(char))
        magic_list = list(magic)
        for i in magic_list:
            st = st + ERR_DET_MAPPING.get(i)
    
    #convert str to binary bitstring
    x = int(st, 2)
    return (x).to_bytes((x.bit_length() + 7) // 8, byteorder='big')