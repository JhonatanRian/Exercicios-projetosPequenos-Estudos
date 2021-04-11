'''
    Utilizando estruturas de repetição escreva um programa que mostre
    os resultados da tabuada de um número inserido pelo usuário.
'''

#  Pede pro usuario qual numero será usado
n = int(input('Informe o numero que deseja ver a tabuada: '))

#  Retorna a tabuada usando 'for' e formatação de strings
for i in range(11):
    multi = f'{i:2}x{n:<2} = {i*n:<3} |'
    soma = f'{i:2}+{n:<2} = {i+n:<3} |'
    sub = f'{i:2}-{n:<2} = {i-n:<3} |'
    div = f'{i:2}/{n:<2} = {i/n:.2f} |'
    print(multi, soma, div, sub)
