'''
    Escreva um programa que peça ao usuário 20 números reais e ao final mostre
    a soma e a média dos números digitados.
'''

#  Variável que será usada parar somar
soma = 0
for i in range(1, 21):
    numero = float(input(f'Número {i}: '))
    #  Somando
    soma += numero
    
    #  No final irá mostrar os resultados
    if i == 20:
        print(f'Soma dos números digitados: {soma} ')
        print(f'Média dos números digitados: {soma/20}')
