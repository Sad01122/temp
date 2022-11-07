import os
import socket

def recv():
    try:
        stuff=target.recv(2048)
        data=stuff.decode('utf-8')
        print(data)
        send()
    except:
        print("failed to rcv")

def send():
    while True:
        try:
            data=input("data to be sent.")
            if(data=="quit"):
                cmd=data.encode('utf-8')
                target.sendall(cmd)
                break
            else:    
                cmd=data.encode('utf-8')
                target.sendall(cmd)
                recv()
        except:
            print("error occured while sending")


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.10.7',6665))
s.listen()
target, ip=s.accept()
send()


