import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server.bind((host, port))
server.listen(5)

while True:
    client,addr = server.accept()
    print("address: %s" % str(addr))
    msg = "Hello Python"
    client.send(msg.encode('utf-8'))
    client.close()
