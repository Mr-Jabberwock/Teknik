import ast
import re
import socket
import datetime
from collections import Counter

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#algorytmen. Hvis nummeret af den besked man lige har sendt minus den besked man lige har modtaget er lig med 1,
#betyder det at beskederne er i den rigtige rækkefølge.

server_address = ('localhost', 10000)
message = b'com-0 127.0.0.1'
count = 0
file = open("Log.txt", "a")

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    tid = str(datetime.datetime.now())

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

    # give accept
    if data == b'com-0 accept 127.0.0.1':
        accept = b'com-0 accept'
        print('sending {!r}'.format(accept))
        acceptSend = sock.sendto(accept, server_address)

        file.write("succes with: " + socket.gethostbyname(socket.gethostname()) + " time: " + tid +"\n")
        file.flush()

    while True:

        #variablen aswer bliver oprettet. Den bliver sat til at være et bruger indput
         answer = input()
         whatever = "msg-" + str(count) + " = " + answer
         send = sock.sendto(whatever.encode(), server_address)
        #variablen whatever er en string som består msg- protokollen, nummeret hvortil vi er nået, og hvad
        #end brugeren indsatte af tekst
        #vi sender en encodet udgave af whatever. Vores string er nu bits og kan sendes via datagrampackets

         print(f'msg-{count}')
         count = count + 1
         data1, server = sock.recvfrom(4096)
         count = count + 1
         number1 = re.findall('\d+', data1.decode())

         number2 = count - int(number1[0])
         print(data1.decode())

         if number2 == 1:
             print("den er godkendt")


         else:
             print('closing socket')
             sock.close()



finally:
    print('closing socket')
    sock.close()