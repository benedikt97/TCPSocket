#!/usr/bin/python3

import socket;



HOST = '192.168.10.21'
dummy = True

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
    
    
    while True:
        try:
            print("...waiting for connection")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
                conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                conn.bind((HOST, PORT))
                conn.listen()
                conn, addr = conn.accept()
                with conn:
                    print("Connected by: ", addr)
                    while dummy:     
                        data = conn.recv(1024)
                        if not data: 
                            raise ValueError('Connection Closed')
                        print("~~~~~~~~~~~~Data Received~~~~~~~~~~~~")
                        stri = data.replace(b'\r', b'\x43'b'\x52')
                        stri = stri.replace(b'\x18', b'\x43'b'\x4C'b'\x52'b'\x20')
                        stri = stri.replace(b'\x00', b'\n'b'\x20'b'\x20'b'\x20'b'\x20')
                        stri =stri.decode('UTF-8')
                        print(stri)
                        

        except Exception as e:
            print(e)
            dummy = True
            
                        
