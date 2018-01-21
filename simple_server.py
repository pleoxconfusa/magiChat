import socket

magic_file_name = "squares.txt"

def load_encoding():
    #Function to load dictionary of ascii -> 48bit data from text file
    scheme_dict = {}
    #load file
    #[########]:HEX
    with open(magic_file_name, 'r') as f:
        for lines in f:
            x = lines.split(':')[0]
            scheme_dict[x] = chr(int(lines.split(':')[1].replace('\n','')))
        f.close()

    #generate dictionary from file
    # print(scheme_dict)
    #return dictionary
    #48 bit -bitstream
    #12 length hex per char
    return scheme_dict
 
def decode(message, scheme_dict):
    #take in the message and pull out magic squares
    x = list(message)

    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed

def Main():
    host = "127.0.0.1"
    port = 63544
    scheme_dict = load_encoding()

     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()
