'''
Escreva um programa que receba dois números de ponto flutuante e mostre na 
tela o maior número digitado. Considere a possibilidade de o usuário digitar
dois números iguais.
'''

n1 = float(input('digite um numero: '))
n2 = float(input('\ndigite outro numero: '))
if n1 < n2:
    print(f'\n{n2} é maior que {n1}.')
elif n1 > n2:
    print(f'\n{n1} é maior que {n2}')
else:
    print(f'\n{n1} é igual a {n2}')