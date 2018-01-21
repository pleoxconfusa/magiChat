#Conor Rogers
# Server Side:
import sys
import socket
import select

#set consts
RECV_BUFF = 4096
port =63544
Host =''
SOCK_LIST=[]

#subject to change
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

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((Host, port))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print "Chat server started on " + str(port)
 
    while 1:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        broadcast(server_socket, sock, "\n" + '[' + str(sock.getpeername()) + '] ' + decode(data))  
                    else:
                        # remove the socket that's broken    
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    
 #just passes the message along...
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)



def decode(message, scheme_dict):
    #take in the message and pull out magic squares
    list(message)
    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed
    #return translation

# def receive_chat():
    #this will be a process run function to receive chats and their times into a dictionary
    
    
def encode(message, scheme_dict): 

def main():
    #main
    chat_server()
    #upon close, prompt user to save or discard chat session
    
    #call save handler that will handle our chat handler
    # save_handler(chat_handler())

    #return 0/profit
    return 0
    

if __name__ == "__main__": main()  