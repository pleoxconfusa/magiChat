# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:12:54 2018

@author: cbony
@auther: cojaroge
"""
#if 91.1% data, then send our way, otherwise send norm
import socket
import sys
import select

port_1 = 63543
port_2 = 63544
magic_file_name = 'squares.txt'
SOCKET_LIST = []
RECV_BUFFER = 4096
HOST = ''


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
    
def open_connection():
    #"first function" opens a socket on an interface and returns a socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server_socket
    
def connect(socket):
    #"second function" binds a socket to an interface


def first_user():
    #first function, asks for interface to listen on and opens server and presents current IP. then with return data calls "second function" to connect.
    socket = open_connection()
    socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket.bind((HOST, port_1))
    socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(socket)
 
    print "Chat server started on port " + str(PORT)

    #return the socket
    return socket
    
    
def second_user(ip):
    #second function, asks for IP of server ready then calls "first function".
    
    #return the socket

def reconstruct(squares, scheme_dict):
    #reconstruct magic squares

def decode(message, scheme_dict):
    #take in the message and pull out magic squares
    list(message)
    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed

def receive_chat():
    #this will be a process run function to receive chats and their times into a dictionary
    
    
def encode(message, scheme_dict): 


def send_chat(message, socket):

def display_chat():
    
def chat_handler():
    #prompt user for first or second in either text or openCV
    response = input("Are you first?\n").capitalize
    
    valid_responses = ("YES", "NO")
    
    while response not in valid_responses:
        response = input("Err. Are you first?\n").capitalize
    
    
    #if first, -> first function
    if response == "YES":
        socket = first_user()
    
    #if second, -> second function
    elif response == "NO":
        socket = second_user()
        
    else: 
        exit(1) #handle errors later
    

    #while not terminated by closing window, enable chat client with threading
    #encode all messages as magic squares
    #decode all receptions from magic squares

    
    #make a handler for the chat that prompts user an initiates chat
    #gets an IP address from the user
    
    #return log of messages

def save_log(log):
    #save log

def save_handler(log):
    #ask user to save log if they want to

def main():
    #main

    #upon close, prompt user to save or discard chat session
    
    #call save handler that will handle our chat handler
    save_handler(chat_handler())
    
    #return 0/profit
    return 0
    

if __name__ == "__main__": main()  