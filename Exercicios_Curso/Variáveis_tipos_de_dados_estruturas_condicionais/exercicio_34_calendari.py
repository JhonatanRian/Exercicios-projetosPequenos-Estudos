'''
    Modifique o programa anterior e permita que o usuário especifique o ano e o
    mês a serem mostrados na tela.
'''

from calendar import month

ano = int(input('Digite o ano: '))
mes = int(input('Digite o mes: '))
print(month(ano, mes))