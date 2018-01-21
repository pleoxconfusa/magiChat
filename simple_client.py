import socket

def load_encoding():
    #Function to load dictionary of ascii -> 48bit data from text file
    scheme_dict = {}
    #load file
    #[########]:HEX
    with open(magic_file_name, 'r') as f:
        for lines in f:
            x = lines.split('[')[1]
            scheme_dict[x.split(']')[0]] = lines.split(':')[1].replace('\n','')
        f.close()

    #generate dictionary from file
    printf(scheme_dict)
    #return dictionary
    #48 bit -bitstream
    #12 length hex per char
    return scheme_dict
 
def Main():
        host = '127.0.0.1'
        port = 63544
        scheme_dict = load_encoding()
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()