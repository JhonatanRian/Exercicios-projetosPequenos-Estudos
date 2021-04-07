'''
Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.

Dica: utilize o módulo math do Python, especificamente math.fatorial.
'''
#Obtendo resultado atrávez da lib math
from math import factorial
valor = int(input('Indique um numero para calcular o fatorial: '))
print(f'resultado: {factorial(valor)}')

#Obtentdo o resultado atrávez da lógica.
factorial = 1
while valor > 1:
    factorial = factorial * valor
    valor = valor - 1
print(f'Resultado: {factorial}')