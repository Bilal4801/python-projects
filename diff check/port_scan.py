import socket
# from socket import *
import sys
import time
import threading

print('*' * 76 )

strart_time = time.time()

usage = 'py port_scan.py target start port end port'
if(len(sys.argv) != 4):
	print(usage)
	sys.exit()

try:
	target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:   # agar address nahi milta tu ye error mile ga get address info gai
	print('Name resolution error')		
	sys.exit()

start_port = int(sys.argv[2])	
end_port = int(sys.argv[3])

# print(start_port, end_port)

def scan_port(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM), # Sock_stream for making connection tcp or utp, currently have a tcp conn
	# print(s)
	con = s.connect_ex((target, port)), # host and port
	print(con)
	if(not conn):  # return True if connection is open, connection is open when return 0, or nothing
		print("port{} is open".format(port))	
	s.close()

for port in range(start_port, end_port+1):
	thread = threading.Thread(target = scan_port, args = (port,))
	thread.start()

end_time = time.time()
print('Time elapsed: ' end_time - start_time, 's')