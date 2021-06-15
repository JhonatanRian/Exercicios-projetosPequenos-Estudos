'''
Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.
'''

numero1 = float(input('Número 1: '))
numero2 = float(input('Número 2: '))
numero3 = float(input('Número 3: '))
if (numero1>=numero2) and (numero1>=numero3):
    print(f'Maior número: {numero1}')
elif (numero2>=numero1) and (numero2>=numero3):
    print(f'Maior número: {numero2}')
else:
    print(f'Maior número: {numero3}')
