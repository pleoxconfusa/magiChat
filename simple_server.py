"""
This simple server program allows messages to be received over UDP from a simple
client server program and decoded with MMU.
"""

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
       (data, addr) = sock.recvfrom(int(BUFFER/8))
       # if number of bytes in data %10 = 0 then ->
       if (len(BitArray(bytes=data).bin) % 10) == 0:
           print(MMU_decode(data))
           
   sock.close()
   
if __name__ == '__main__':
   Main()