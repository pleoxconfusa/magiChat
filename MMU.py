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
    highest_sim = 0
    sim_key = ""
    
    for key in scheme_dict.keys():
        sim_count = 0
        
        for i in range(len(square)):
            if square[i] is not -1:
                if square[i] == key[i]:
                    sim_count = sim_count + 1
                else:
                    sim_count = -16
                    
        if sim_count > highest_sim:
            sim_key = key
            highest_sim = sim_count
        
    if sim_key is "":
        return ""
    else:
        return scheme_dict.get(sim_key)
        
def MMU_decode(message, scheme_dict=DEF_DECODING_SCHEME):
    output = "" 

    #take in the message and pull out magic squares

    #turn message to bytes
    #turn bytes of message to bitstring

    bitstr = BitArray(bytes=message).bin
    # print(bitstr)

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

    # print(characters)
    for c in characters:
        for i in range(16):
            if c[i] not in ERR_DET_MAP_REV.keys():
                c[i] = -1
            else:
                c[i] = ERR_DET_MAP_REV.get(c[i])
        c_tup = tuple(c)
        #print(c_tup)
        if c_tup not in scheme_dict.keys():
            output = output+reconstruct(c_tup,scheme_dict)
        else:
            output = output + scheme_dict.get(c_tup)


        #turn c in characters into a tuple

        #look up tuple in scheme_dict
        #if not in scheme_dict.keys()
        #   output = output + reconstruct(key, scheme_dict)
        #else
        #   output = output + scheme_dict.get(key)

    return output #return date/time string + output + \n
    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed
    
def MMU_encode(data, scheme_dict=DEF_ENCODING_SCHEME):
    st = ''
    for char in data:
        magic = scheme_dict.get(ord(char))
        magic_list = list(magic)
        for i in magic_list:
            st = st + ERR_DET_MAPPING.get(i)
    
    #convert str to binary bitstring
    # st = int(st, 2);
    # print(st)
    x = int(st, 2)
    # print(x)
    # print((x).to_bytes((x.bit_length() + 7) // 8, byteorder='big'))
    return (x).to_bytes((x.bit_length() + 7) // 8, byteorder='big')