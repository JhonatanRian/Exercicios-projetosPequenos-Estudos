'''
    Escreva um programa que verifique se um determinado número digitado 
    pelo usuário é nulo, positivo ou negativo.
'''

n = int(input('»» '))
if n > 0:
    print('Positivo')
elif n < 0:
    print('Negativo')
else:
    print('Nulo')