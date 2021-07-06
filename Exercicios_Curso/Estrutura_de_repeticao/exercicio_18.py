'''
    Elabore um programa que embaralhe a lista a seguir e mostre na tela cada elemento.
    lista=['A','B','C','D','E','F','G','H','I','J','K','L','M']  
'''

import random
lista=['A','B','C','D','E','F','G','H','I','J','K','L','M']
     
random.shuffle(lista)
     
for letra in lista:
    print(letra)