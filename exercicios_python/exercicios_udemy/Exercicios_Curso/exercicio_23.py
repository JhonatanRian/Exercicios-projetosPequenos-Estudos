'''
Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:
"O número [número] é [par/ímpar]"
'''
numero = int(input('Digite um numero: '))
if numero % 2 == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é ímpar')