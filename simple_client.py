import socket

magic_file_name = "squares.txt"
# BUFFER = 20480

def load_encoding():
    #Function to load dictionary of ascii -> 48bit data from text file
    scheme_dict = {}
    #load file
    with open(magic_file_name, 'r') as f:
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
 
def encode(data, scheme_dict):
    str = '';
    res = dict(v, bin(k)[2:]) for k, v in scheme_dict.items()
    for k in res:
        if k.endswith('0'):
           str += '2'
        elif k.endswith('1'):
           str += '1'
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