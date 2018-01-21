magic_file_name = "squares.txt"


def load_encoding(file_name=magic_file_name):
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

    #generate dictionary from file
    # print(scheme_dict)
    #return dictionary

    return scheme_dict
    

def load_decoding(file_name=magic_file_name):
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

    #generate dictionary from file
    # print(scheme_dict)
    #return dictionary

    return scheme_dict