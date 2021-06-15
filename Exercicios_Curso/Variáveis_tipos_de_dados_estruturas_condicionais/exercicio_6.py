'''
    Faça um programa que calcule a raiz quadrada de
    um número. O usuário deve inserir um número e o
    programa deve mostrar na tela o resultado da
    raiz quadrada do número inserido.
'''

#Modo 1
numero = int(input("Digite um numero: "))
print(f"A raiz quadrada de {numero} é {numero**0.5}")

#modo 2
from math import sqrt

print(f"A raiz quadrada de {numero} é {sqrt(numero)}")