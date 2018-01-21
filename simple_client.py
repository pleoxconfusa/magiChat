import socket

magic_file_name = "squares.txt"
BUFFER = 20480

err_det_mapping = { 0: "00000", 1: "00011", }

def load_encoding():
     #Function to load dictionary of ascii -> 48bit data from text file
    scheme_dict = {}
    #load file
    with open(magic_file_name, 'r') as f:
        for lines in f:
            value, key = lines.split(':')[0], lines.split(':')[1]
            x_list = value.split(' ')
            x_list = x_list[:-1] #maybe. may cause errors
            x_list = list(map(int, x_list))
            x_tuple = tuple(x_list)
            scheme_dict[key] = x_tuple
        f.close()

    #generate dictionary from file
    # print(scheme_dict)
    #return dictionary

    return scheme_dict
    
def encode(data, scheme_dict):
    str = '';
    for char in data:
        str = str + err_det_mapping(char)
    
    #convert str to binary bitstring
    
    return str;
    
def Main():
    MNU_IP = "127.0.0.1"
    MNU_PORT = 63545
    scheme_dict = load_encoding()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("Send Data:")
        while message.len >= 256:
            message = input("Send Data:")
        
        sock.sendto(encode(message, scheme_dict), (MNU_IP, MNU_PORT))
        
if __name__ == '__main__':
    Main()