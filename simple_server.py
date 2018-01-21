import socket
from MMU import *
BUFFER = 20480

def Main():
   MMU_IP = "127.0.0.1"
   MMU_PORT = 63545
   
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.bind((MMU_IP, MMU_PORT))
    # become a server socket
   while True:
       (data, addr) = sock.recvfrom(int(BUFFER/8)) # buffer size is 1024 bytes
       # print("received message:", data)
       # if number of bytes in data %10 = 0 then ->
       if (len(BitArray(bytes=data).bin) % 10) == 0:
           print(MMU_decode(data))
           
   sock.close()
   
if __name__ == '__main__':
   Main()