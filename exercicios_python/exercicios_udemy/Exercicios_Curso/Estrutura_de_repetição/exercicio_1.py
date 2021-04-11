'''
    Escreva um programa que mostre de 1 até 50 na tela.
'''

#  Solução 1
for indice in range(1, 51):
    print(indice, end=', ')
    
#  Solução 2
numero = 1

while numero <= 50:
    print(numero, end=', ')
    numero += 1