from socket import socket
from threading import Thread

def accept_(sock):
	while True:
		data = sock.recv(1024)
		if data == b'/q':
			sock.close()
			break
		print('Server:',data.decode('utf-8'))

def send_(sock):
    while True:
        a = input()
        if a == '/q':
            print(f"Close connection")
            sock.send(a.encode('utf-8'))
            sock.close()  
            break
        sock.send(a.encode('utf-8'))

def start_test_client():
	sock = socket()
	sock.connect(('localhost', 9090))

	t1 = Thread(target=accept_, args=(sock,))
	t2 = Thread(target=send_, args=(sock,))
	t1.start()
	t2.start()