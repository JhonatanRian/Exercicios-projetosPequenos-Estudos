import pickle
from os import system as sy
from time import sleep

def incluir_numero(nome, fone, niver):
    produto = dict()
    produto["nome"] = nome
    produto["fone"] = fone
    produto["niver"] = niver
    registros.append(produto)

def retirar_numero(desc):
    for produto in registros:
        i = 0
        if produto["nome"] == desc:
            registros.remove(produto)
            return
    print("Nome não encontrado")
    
def encapsular(dados):
    try:
        arquivo = open("registros.bin", "wb")
        pickle.dump(dados, arquivo)
        arquivo.close()
    except:
        print("Não foi possivel salvar os dados")

def recolher_dados():
    while True:
        nome = input("nome\n»» ")
        fone = input("fone\n»» ")
        niver = input("aniversário[mês/ano]\n»»")
        sy("clear")
        print(f"\nnome: {nome}")
        print(f"fone: {fone}")
        print(f"aniversario: {niver}")
        verifica = input(f"\nOs dados estão corretos? se sim digite S se não N\n»» ").upper().split()[0]
        if verifica == "S":
            lista = [nome, fone, niver]
            break
    return lista

registros = []

try:
    arquivo = open("registros.bin", "rb")
    registros = pickle.load(arquivo)
    arquivo.close()
except:
    pass

while True:
    sy("clear")
    print("1. Inserir contato\n2. Remover contato\n3. listar contatos\n4. Salvar e sair")
    opc = input("»» ").split()[0]
    while True:
        if opc == "1":
            sy("clear")
            lista = recolher_dados()
            incluir_numero(*lista)
            break
        elif opc == "2":
            resposta = input("Insira o nome que deseja excluir ou S para sair\n»» ").split()[0]
            if resposta == "N":
                break
            else:
                retirar_numero(resposta)
                break
        elif opc == "3":
            sy("clear")
            for pessoa in registros:
                print("\nnome: {}\nfone: {}\naniversario: {}".format(pessoa["nome"], pessoa["fone"], pessoa["niver"]))
            resposta = input("\nDigite S para sair\n»» ").upper().split()[0]
            if resposta == "S":
                break
        elif  opc == "4":
            encapsular(registros)
            exit(1)
        else:
            print("\nDigito incorreto\n")
            sleep(3)