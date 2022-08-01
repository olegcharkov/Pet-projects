import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 1397))
# server.listen(20)
# print('In process...')
# client_socket, address = server.accept()
# data = client_socket.recv(1024).decode('utf-8')
# print(data)
# HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
# content = 'I am alive'.encode('utf-8')
# client_socket.send(HDRS.encode('utf-8') + content)
# print('Need some rest!')


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.bind((__name__))
# s.listen(20)
# conn, addr = s.accept()
#
# while True:
# 	data = conn.recv(1024)
# 	if not data:
# 		break
# 	conn.sendall(data)
# 	print(data.decode('utf-8'))
# conn.close()
#
# if __name__ == "__main__":
#     s.run(host = '127.0.0.2', port = 1397)

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('127.0.0.1', 2310))
serv_sock.listen(100)

while True:
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(data)

    client_sock.close()



