import socket

import sys

def create_socket():
    try:
        global host
        global port
        global s 
        host = ""
        port= 9999

        s= socket.socket()
    except socket.error as msg:
        print("Error:" + str(msg))

#binding socket/listening

def bind_socket():
    try:
        global host
        global port
        global s

        print("port : " + str(port))

        s.bind((host,port))
        s.listen(6)


    except socket.error as msg:
        print("Error : "+ msg+ " " + "Retrying....")
        bind_socket()

#establish conn

def socket_accept():
    conn,address = s.accept()
    print("established,,,,,,,,,,,,,," + address[0] + " " + str(address[1]))
    send_cmd(conn)
    con.close()

#working on client system

def send_cmd(conn):

    while True:
        cmds = input()

        if cmds == "quit":
            conn.close()
            s.close()
            sys,exit()
        if len(str.encode(cmds)) > 0:
            conn.send(str.encode(cmds))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end ="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
    
    
    
