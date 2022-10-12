import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.11.168', 8888)) #առաջին արգումենտում նշել այն համակարգչի IP-ն, որին պետք է միանալ
while True:
    sock.send(input().encode('utf-8'))
    data1 = sock.recv(1024)
    print(data1.decode('utf-8'))
