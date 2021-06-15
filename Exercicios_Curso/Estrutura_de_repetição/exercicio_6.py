'''
    Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.
'''

#  Solução 1
lista = list()
x = 1

#  armazenando os números em uma lista
while len(lista) < 20:
    if x % 5 == 0:
        lista.append(x)
        x += 1
    x += 1

#  mostrando os números na tela
for num in lista:
    print(num)

#  Solução 2
# usando List Comprehension
lista = [num for num in range(1, 101) if num % 5 == 0]
for num in lista:
    print(num)

#  Solução 3
for num in range(1, 101):
    if num % 5 == 0:
        print(num)

#  Solução 4
x = 1
while x <= 100:
    if x % 5 == 0:
        print(x)
        x += 1
    x += 1