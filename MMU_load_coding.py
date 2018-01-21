"""
This program is a PoC for a future package class.  The MMU_load_coding program 
loads a coding scheme for decoding and encoding in two sepearate function calls
that return dictionaries of the scheme.

Defaults:

DEF_MAGIC_FILE_NAME -- The default magic file name is "squares.txt", which
    contains magic squares read left to right in rows and top to bottom in 
    columns followed by a colon then a value from 0 to 255. Example:

The Generated Pan-Magic Square:
| 2  5 11 12|
|15  8  6  1|
| 4  3 13 10|
| 9 14  0  7|

Becomes:

2 5 11 12 15 8 6 1 4 3 13 10 9 14 0 7 : 0

Functions:

load_encoding -- defaults to reading from our default magic file name, but an
    argument may be passed: a different file name.  There is no error checking
    involved in this PoC.
load_decoding -- defaults to reading from our default magic file name, but an
    argument may be passed: a different file name.  Once again, there is no
    error checking involved in this PoC.
"""

#Default Magic Square text database
DEF_MAGIC_FILE_NAME = "squares.txt"


def load_encoding(file_name=DEF_MAGIC_FILE_NAME):
    """ This function reads an encoding schema from a specifically formatted 
    text document.  The location of this text document has a default, but may
    be reassigned.  As this PoC includes no error handling, this reassignment is
    not suggested.

    Args:
        Required:
            None
        Optional:
            file_name -- a text document formatted for reading magic squares. 
                see squares.txt for an example.

    Returns:
        Dictionary of keys with 0 to 255 and assigned corresponding magic squares
        as tuple values.
    """
    
     #Function to load dictionary of ascii -> 48bit data from text file
    scheme_dict = {}
    #load file
    with open(file_name, 'r') as f:
        for lines in f:
            value, key = lines.split(':')[0], lines.split(':')[1].replace('\n','').replace(' ','')
            x_list = value.split(' ')
            x_list = x_list[:-1] #maybe. may cause errors
            x_list = list(map(int, x_list))
            x_tuple = tuple(x_list)
            scheme_dict[int(key)] = x_tuple
        f.close()

    return scheme_dict
    

def load_decoding(file_name=DEF_MAGIC_FILE_NAME):
    """ This function reads an decoding schema from a specifically formatted 
    text document.  The location of this text document has a default, but may
    be reassigned.  As this PoC includes no error handling, this reassignment is
    not suggested.

    Args:
        Required:
            None
        Optional:
            file_name -- a text document formatted for reading magic squares. 
                see squares.txt for an example.

    Returns:
        Dictionary of keys with magic squares as tuple values and assigned 
        corresponding 0 to 255 unique values.
    """
    
    #Function to load dictionary of ascii -> 48bit data from text file
    scheme_dict = {}
    #load file
    with open(file_name, 'r') as f:
        for lines in f:
            x = lines.split(':')[0]
            x_list = x.split(' ')
            x_list = x_list[:-1]
            x_list = list(map(int, x_list))
            x_tuple = tuple(x_list)
            scheme_dict[x_tuple] = chr(int(lines.split(':')[1].replace('\n','')))
        f.close()


    return scheme_dict