'''
    Escreva um programa que peça um número inteiro do usuário e calcule e
    imprima a tabuada deste número.
'''

#  Entra com o numero
n = int(input('Informe o numero que deseja ver a tabuada: '))
#  Retorna a tabuada usando 'for' e formatação de strings
for i in range(11):
    multi = f'{i:2}x{n:<2} = {i*n:<3} |'
    soma = f'{i:2}+{n:<2} = {i+n:<3} |'
    sub = f'{i:2}-{n:<2} = {i-n:<3} |'
    div = f'{i:2}/{n:<2} = {i/n:.2f} |'
    print(multi, soma, div, sub)