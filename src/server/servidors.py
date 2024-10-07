from socket import *

def servidor(port):
    sever_port = int(port)
    seversocket = socket(AF_INET, SOCK_DGRAM)
    seversocket.bind(('',sever_port))
    print ("servidor está pronto para receber")
    while 1:
        message, clientAddress = seversocket.recvfrom(2048)
        message = message.decode('utf-8')
        modified_message = message.upper()
        print(modified_message)
        modified_message = str(modified_message).encode('utf-8')
        seversocket.sendto(modified_message,clientAddress)