import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.11.168', 8888)) # առաջին արգոմենտում գրել այս համակարգչի IP-ն
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)
while True:
    data = conn.recv(1024)
    print(data.decode())
    conn.send(input().encode("utf-8"))

