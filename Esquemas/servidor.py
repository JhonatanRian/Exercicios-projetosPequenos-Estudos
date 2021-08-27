import socket

host = "localhost"
porta = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,porta))
s.listen()
print("aguardando conexão.")
con, end = s.accept()
print("conectado em {}".format(end))

while True:
    data = con.recv(1024)
    if not data:
        print("fechando conexão")
        con.close()
        break
    con.sendall(data)
    print("mensagem recebida: {}".format(data.decode()))