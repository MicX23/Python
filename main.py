# Test_client-->server
from socket import socket
from threading import Thread

def main(conn,addr):
    while True:
        data = conn.recv(1024)
        if data == b'/q':
            print(f"Close connection: {addr}")
            break 
        elif data:
            print('Client:',data.decode('utf-8'))

def send_(con):
    while True:
        a = input()
        if a == '/q':
            print(f"Close connection")
            con.send(a.encode('utf-8'))
            con.close()  
            break
        con.send(a.encode('utf-8'))  


def start_test_client():
	sock = socket()

	sock.connect(('localhost', 9090))
	while True:
		a = input()
		sock.send(a.encode('utf-8'))
		if a == '/q':
			break
		data = sock.recv(1024)
		if data == b'/q':
			sock.close()
			break
		print('Server:',data.decode('utf-8'))

	sock.close()





def start_test_server():
	sock = socket()
	sock.bind(('', 9090))
	sock.listen(1)
	conn, addr = sock.accept()
	print(f'Connect: {addr}')
	t1 = Thread(target=main, args=(conn,addr))
	t2 = Thread(target=send_, args=(conn,))
	t1.start()
	t2.start()


def menu():
	while True:
		a = int(input('1.Client\n2.Server\n:: '))
		if a == 1 or a == 2:
			return a
		print('no')
		continue

if __name__ == '__main__':
	if menu() == 1:
		start_test_client()
	else:
		start_test_server()