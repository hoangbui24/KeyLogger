from pynput.keyboard import Listener
import logging
import threading, subprocess, socket, argparse, sys

import socket

# Tạo một socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thiết lập địa chỉ IP và cổng của server
server_address = ('192.168.159.129', 9000)
server_socket.bind(server_address)

# Cho phép server lắng nghe kết nối từ client
server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()

print('Received connection from {}:{}'.format(*client_address))

# Nhận dữ liệu từ client
data = client_socket.recv(1024)

# Xử lý dữ liệu
response = 'Hello, client!'
client_socket.sendall(response.encode())

# Đóng kết nối
client_socket.close()
server_socket.close()
