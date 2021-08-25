import socket
import sys

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print("erro: {}".format(e))
        sys.exit()
    print("socket criado")
    
    host = input("Host: ")
    porta = input("Porta: ")
    
    try:
        sock.connect((host, int(porta)))
        print("Criado conexão tcp cliente")
        sock.sendall(str.encode('Bom dia ae vencedor'))
        data = sock.recv(1024)
        print('mensagem ecoada: {}'.format(data.decode()))
    except socket.error as e:
        print(f"Erro: {e}")
        sys.exit()
        
if __name__ == "__main__":
    main()