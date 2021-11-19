import socket
import sys


query ="\r\n"

s_old = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_old.connect(("whois.iana.org", 43))
s_old.send(sys.argv[1] + b"\r\n")
resp = s_old.recv(1024).split()
print (resp[19])
correct = (resp[19])

s_new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_new.connect_ex((correct, 43))
s_new.send(sys.argv[1] + b"\r\n")
response = s_new.recv(1024)
print (response)
