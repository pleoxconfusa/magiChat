"""
This simple client program allows messages to be encoded with MMU and sent over
UDP to a pre-designated simple server program.  This is for PoC.
"""

import socket
from MMU import *
BUFFER = 20480

   
def Main():
   MMU_IP = "127.0.0.1"
   MMU_PORT = 63545
   
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   while True:
       message = input("Send Data: ")
       while len(message) >= 256:
           message = input("Err. Message too large.\nSend Data:")
           sock.sendto(MMU_encode("!!!Too large file.!!!"), MMU_IP, MMU_PORT)
       
       if message:
           sock.sendto(MMU_encode(message), (MMU_IP, MMU_PORT))
       
if __name__ == '__main__':
   Main()