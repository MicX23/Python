# Test_client-->server
from socket import socket
from threading import Thread


def start_test_client():
	pass



def start_test_server():
	pass


def menu():
	while True:
		a = input('1.Client\n2,Server\n:: ')
		if a == 1:
			start_test_client()
		elif a == 2:
			start_test_server()
		else:
			return 0

if __name__ == '__main__':
	menu()