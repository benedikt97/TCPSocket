#!/usr/bin/python3

import socket;



HOST = '192.168.10.21'


def ownip():
    connection=socket.socket()
    connection.connect(("google.de",int(80)))
    own = (connection.getsockname()[0])
    connection.close()
    print("Your IP is ", own)
    return own



if __name__ == "__main__":  
    print("Welcome to Socket.py / HeuserB")
    HOST = '172.16.45.100' #ownip()
    
    print("Please type Port to listen to: ")
    PORT = int(input())
    print("Listening on ", HOST, " at Port: ", PORT)
    print("...waiting for connection")
    
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
                conn.bind((HOST, PORT))
                conn.listen()
                conn, addr = conn.accept()
                with conn:
                    print("Connected by: ", addr)
                    while True:     
                        data = conn.recv(1024)
                        if not data: 
                            print("Connection closed")
                            #break
                        print("Data Received")
                        print(data)
        except Exception as e:
            print(e)
            
                        
