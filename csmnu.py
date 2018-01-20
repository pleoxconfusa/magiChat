# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:12:54 2018

@author: cbony
"""

port_1 = 63543
port_2 = 63544

def load_encoding():
    #Function to load dictionary of ascii -> 48bit data from text file
    
    #load file
    
    #generate dictionary from file
    
    #return dictionary
    
def open_connection():
    #"first function" opens a socket on an interface and returns a socket
    
def connect(socket):
    #"second function" binds a socket to an interface


def first_user():
    #first function, asks for interface to listen on and opens server and presents current IP. then with return data calls "second function" to connect.

    #return the socket
    
    
def second_user(ip):
    #second function, asks for IP of server ready then calls "first function".
    
    #return the socket

def reconstruct(squares, scheme_library):
    #reconstruct magic squares

def decode(message, scheme_library):
    #take in the message and pull out magic squares
    
    #if magic square matches, keep it, else store it.
    #reconstruct magic squares that need to be reconstructed

def receive_chat():
    #this will be a process run function to receive chats and their times into a dictionary
    
    
def encode(message, scheme_library):    

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