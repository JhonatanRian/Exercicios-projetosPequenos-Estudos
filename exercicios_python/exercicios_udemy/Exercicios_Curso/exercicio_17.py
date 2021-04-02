'''
Escreva um programa que peça um número do usuário e calcule o logaritmo deste número nas bases 10 e 2.
Dica: utilize o módulo math.
'''
from math import log2, log10

valor = float(input('valor: '))
print(f'O logaritmo de {valor} na base 2 é {log2(valor):.1f}')
print(f'O logaritmo de {valor} na base 10 é {log10(valor):.1f}')