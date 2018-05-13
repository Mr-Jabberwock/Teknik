import socket
import re

# Create a UDP socket

#AF står for address family. AF_INET definerer at man kun kan sende og modtage til sockets som også er i denne adresse familie
#Ifølge stackOverflow er alternativer, f.eks, AF_UNIX og AF_PDX. INET delen betyder det er Internet Protocol v4 adresse familien
#Vi benytter her.

#sock_dgram definerer at vi benytter os af datagram sockets. Det her er en UDP forbindelse
from collections import Counter

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port

#data = "whatever"  + tal + "besked"
#conn.sendto(data.encode())

#definer hostname og port nummer
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
#Bind den socket vi lavede tidligere til dette bestemte hostname og port
sock.bind(server_address)
counter = 0
file = open("Log.txt", "w")

#while loop: så længe forbindelsen ikke er afbrudt

while True:
    #modtag
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    #Udskriv antallet af bytes modtaget, og hvor de er modtaget fra
    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    #hvis beskeden er b'com-0 127.0.0.1, send da en besked tilbage
    if data == (b'com-0 127.0.0.1'):
        sent = sock.sendto('com-0 accept 127.0.0.1'.encode(), address)
        print('sent {} bytes back to {}'.format(sent, address))
        # Lidt hardkodet måde at gøre det på, men det følger protokollen


#hvis det modtagne svar er b'com-accept er den godtaget og three way handskaet er ovre
    if data == (b'com-0 accept'):
        #der bliver ventet på yderligere beskeder fra klienten
       print('\nwaiting for client message')
        #nyt while loop; så længe der er forbindelse
       while True:

           #skal den modtage beskeder via socket 4096
           #beskedens tal stiger med en og beskeden bliver decodet fra bits til String
           data1, address = sock.recvfrom(4096)
           counter = counter +1
           print(data1.decode())

           number1 = re.findall('\d+', data1.decode())

           file.write(data1.decode() + "\n")
           file.flush()

           whatever = "asw-" + str(counter) + " = I am groot"
           send = sock.sendto(whatever.encode(), address )
           counter = counter +1

           print(f'asw-{counter}')
           daway = data1.decode()






