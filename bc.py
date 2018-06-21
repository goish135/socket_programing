import random

import socket
import select
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address,Port))



#server.close()
            			
number_all = []    
line = []        
Bingo = 1        

#print('Hello World',end='') # no use
#print('Hello World'), # ok
#print(',Same Line')   # ok

for i in range(1,26):
    number_all.append(i)

random.shuffle(number_all)

for j in range(25):
    #print(number_all[j]),
    print("{0:2}".format(number_all[j])),
    if j%5 ==4:
        print("\n")

for k in range(12):
    line.append(5)

#lines = 5
#count = 0

while(Bingo != 0):
#while True:  
#while(count<6):
    #socks.recv(1024) #
    #server.recv(1024)#
    while True:
        sockets_list = [sys.stdin,server]
	#while(Bingo != 0):
        flag = 0
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                mes = message[-7:]
                print mes
	        if message != "Welcome to this chatroom!" and message != "your turn:" and mes!="the end":
		    num = int(message)
		    print num
	        else:
		    print message
                    flag = 1
                    break  
                    #continue
                      
	    else:
                message = sys.stdin.readline()
		num = int(message)
                server.send(message)
                sys.stdout.write("<You>")
                sys.stdout.write(message)
	        sys.stdout.flush()
        if mes=="the end":
            print "are u serious?"
            Bingo = 0
            break
        if flag == 1:
            print "test"
            continue
        #choice = input("input: ")
	choice = num
        #print()       
    
        for check_column in range(5):
            if(number_all.index(int(choice)) % 5 == check_column):
                line[check_column] -= 1
    
        for check_row in range(5):
            if(number_all.index(int(choice)) // 5 == check_row):
                line[check_row+5] -= 1
    
        if(number_all.index(int(choice)) == 0):
            line[10] -= 1
        elif(number_all.index(int(choice)) == 12): #imp.
            line[10]-=1
            line[11]-=1
        elif(number_all.index(int(choice)) % 6 == 0):
            line[10] -= 1
        elif(number_all.index(int(choice)) % 4 == 0):
            line[11] -= 1
       
        #number_all[number_all.index(int(choice))] = "*" + str(number_all[number_all.index(int(choice))])
        number_all[number_all.index(int(choice))] ="*"
        for j in range(25):
            #print(number_all[j]),
            print("{0:2}".format(number_all[j])), 
            if j%5 ==4:
                print("\n")
    
        count = 0
        for l in range(12):
            #print(line[l])
            if(line[l]==0):
                count = count + 1
            # Bingo *= line[l]
        if(count==3):
            Bingo = 0
            print "Bingo XDD"
            server.send("the end")
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
	    break
        #server.send(message)
        #sys.stdout.write("<You>")
        #sys.stdout.write(message)
        #sys.stdout.flush()
       
       #  count += line[l]
  
    #print("Bingo!!!")    
server.close()
