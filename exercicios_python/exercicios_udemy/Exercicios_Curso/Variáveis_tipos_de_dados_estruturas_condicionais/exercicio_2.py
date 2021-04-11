'''
    Faça um programa que solicite um número do usuário e apresente a
    seguinte mensagem na tela:
    O numero digitado foi ...
'''

#primeiro modo
numero = input("Digite um numero: ")
print(f"O numero digitado foi {numero}")

#Segundo modo(observação, pode gerar um ValueError)
numero = int(input("Digite um numero: "))
print(f"O numero digitado foi {numero}")

#terceiro modo(observação, pode gerar um ValueError)
numero = float(input("Digite um numero: "))
print(f"O numero digitado foi {numero}")

