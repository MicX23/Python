# Test_client-->server
from socket import socket
from threading import Thread
from server import start_test_server
from client import start_test_client

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