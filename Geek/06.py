import pickle
from os import system as sy
from time import sleep

def incluir_produto(cod, desc, quant):
    produto = dict()
    produto["código"] = cod
    produto["descrição"] = desc
    produto["quantidade"] = quant
    registros.append(produto)

def retirar_produto(desc):
    for produto in registros:
        i = 0
        if produto["descrição"] == desc:
            registros.remove(produto)
            return
    print("Produto não encontrado")
    
def encapsular(dados):
    try:
        arquivo = open("registros.bin", "wb")
        pickle.dump(dados, arquivo)
        arquivo.close()
    except:
        print("Não foi possivel salvar os dados")
    
def recolher_dados():
    while True:
        cod = input("insira o código\n»» ")
        desc = input("Descrição do produto\n»» ")
        quant = input("insira a quantidade de produtos\n»»")
        sy("clear")
        print(f"\nCódigo do produto: {cod}")
        print(f"Descrição do produto: {desc}")
        print(f"Quantidade: {quant}")
        verifica = input(f"Os dados estão corretos? se sim digite S se não N\n»» ").upper().split()[0]
        if verifica == "S":
            lista = [cod, desc, quant]
            break
    return lista
    
registros = list()

try:
    arquivo = open("registros.bin", "rb")
    registros = pickle.load(arquivo)
    arquivo.close()
except:
    pass

while True:
    sy("clear")
    print("\n1. incluir produto\n2. remover produto\n3. mostrar armazem\n4. salvar\n5. sair e salvar")
    opc = input("»» ").split()[0]
    while True:
        if opc == "1":
            sy("clear")
            resposta = recolher_dados()
            incluir_produto(*resposta)
            break
        elif opc == "2":
            resposta = input("Insira a descrição do produto pra retirar\n»» ")
            retirar_produto(resposta)
            break
        elif opc == "3":
            sy("clear")
            for produto in registros:
                print("\nCódigo: {}".format(produto["código"]))
                print("descrição: {}".format(produto["descrição"]))
                print("quantidade: {}".format(produto["quantidade"]))
            resposta = input("Digite S para sair\n»» ").upper().split()[0]
            if resposta == "S":
                break
        elif opc == "4":
            encapsular(registros)
            break
        elif opc == "5":
            encapsular(registros)
            exit(1)
        else:
            print("Erro de digitação")
            sleep(3)