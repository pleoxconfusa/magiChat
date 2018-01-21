import socket
from bitstring import BitArray

magic_file_name = "squares.txt"
BUFFER = 20480

err_det_map_rev = {"00000": 0, "00011" : 1, "00101" : 2, "00110" : 3, "01001" : 4, "01010" : 5, "01100" : 6, "01111" : 7, "10001" : 8, "10010" : 9, "10100" : 10, "10111" : 11, "11000" : 12, "11011" : 13, "11101" : 14, "11110" : 15}

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
                    sim_count = sim_count - 1
                    
        if sim_count > highest_sim:
            sim_key = key
            highest_sim = sim_count
        
    if sim_key is "":
        return ""
    else:
        return scheme_dict.get(sim_key)

def decode(message, scheme_dict):
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
            if c[i] not in err_det_map_rev.keys():
                c[i] = -1
            else:
                c[i] = err_det_map_rev.get(c[i])
        c_tup = tuple(c)
        print(c_tup)
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

    return output + "\n" #return date/time string + output + \n
    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed

def Main():
    MNU_IP = "127.0.0.1"
    MNU_PORT = 63545
    scheme_dict = load_encoding()
     
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((MNU_IP, MNU_PORT))
	# become a server socket
    while True:
        (data, addr) = sock.recvfrom(int(BUFFER/8)) # buffer size is 1024 bytes
        # print("received message:", data)
        # if number of bytes in data %10 = 0 then ->
        if (len(BitArray(bytes=data).bin) % 10) == 0:
            print(decode(data, scheme_dict))
             
    sock.close()
     
if __name__ == '__main__':
    Main()