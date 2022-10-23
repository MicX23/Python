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