import socket

magic_file_name = "squares.txt"
BUFFER = 20480

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
            if square[i] is not "":
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
    #take in the message and pull out magic squares
    #80 bits into 16 -> 5 bit bitstrings
    return 'great'
    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed

def Main():
    MNU_IP = "127.0.0.1"
    MNU_PORT = 63545
    scheme_dict = load_encoding()

     
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((MNU_IP, MNU_PORT))
	# become a server socket

    # while True:
        # accept connections from outside
        # (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
    while True:
        (data, addr) = sock.recvfrom(int(BUFFER/8)) # buffer size is 1024 bytes
        # print("received message:", data)
        print(decode(data))
    # while True:
    #         data = conn.recv(BUFFER).decode()
    #         if not data:
    #                 break
    #         print ("from connected  user: " + str(data))
             
    #         data = str(data).upper()
    #         print ("sending: " + str(data))
    #         conn.send(data.encode())
             
    sock.close()
     
if __name__ == '__main__':
    Main()
