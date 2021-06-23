'''
    Escreva um programa que gere 100 números aleatórios entre 
    1 e 1000 e armazene-os em uma lista.

'''

from random import randint
    
lista=[]
for num in range(1,101):
    lista.append(randint(1,1000))