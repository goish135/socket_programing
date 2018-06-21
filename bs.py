# Python program to implement server side of chat room.
import socket
import select
import sys
from thread import *
 
"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
 
# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])
 
# takes second argument from command prompt as port number
Port = int(sys.argv[2])
 
"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((IP_address, Port))
 
"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)
 
list_of_clients = []



def decide_order(count):
    turn = 0
    while True:
        #turn = 0 
        print "it's your turn: ", (turn % count+1)
        try:  #
            list_of_clients[turn%count].send("your turn:")
        except:   #
         #   list_of_clients.remove(turn%count) #
            pass 
        
        num_chosed = list_of_clients[turn%count].recv(2048)
        if num_chosed :
            print num_chosed
            broadcast(num_chosed,list_of_clients[turn%count])
            if num_chosed[-7:] =="the end":
                print "is here?"
                break
        turn = turn + 1
        print turn 
        #if turn == 10: # to be fix 
           # break  

 
def clientthread(conn, addr):
 
    # sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom!")
    #print addr[1]
    while True:
            try:
                #message = conn.recv(2048)
                if message:
 
                    """prints the message and address of the
                    user who just sent the message on the server
                    terminal"""
                    #print addr
                    print "< client's ID: " + str(addr[1]) + " > " + message
                    #print str(count)
                    # Calls broadcast function to send message to all
                    message_to_send = "< client's ID: " + str(addr[1]) + " > " + message
                    # message_to_send = "<"+ "client" ,count,">"+ message
                    #broadcast(message_to_send, conn)
 
                else:
                    """message may have no content if the connection
                    is broken, in this case we remove the connection"""
                    remove(conn)
 
            except:
                continue
 
"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
 
                # if the link is broken, we remove the client
                remove(clients)
 
"""The following function simply removes the object
from the list that was created at the beginning of 
the program"""
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

count = 0 #
while True:
 
    """Accepts a connection request and stores two parameters, 
    conn which is a socket object for that user, and addr 
    which contains the IP address of the client that just 
    connected"""
    conn, addr = server.accept()
 
    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)
    print conn
 
    # prints the address of the user that just connected
    print "client's ID: ", addr[1] ," connected"
    count = count + 1 #
    print count 
    # creates and individual thread for every user 
    # that connects
    start_new_thread(clientthread,(conn,addr))
    #decide_order(count)    
    if count == 3:
        break
decide_order(count)
print "Round Over..."
conn.close()
server.close()
