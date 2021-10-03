import socket

HEADER = 1028
PORT = 1234
FORMAT = 'utf-8'
SERVER = "10.40.1.166"
ADDR = (SERVER, PORT)
DISCONNECT = "Disconnected"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello!")
