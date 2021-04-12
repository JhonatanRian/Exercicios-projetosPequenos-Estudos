'''
    Escreva um programa que peça um número inteiro do usuário e mostre na 
    tela o fatorial deste número.
'''

# Solução 1

num = int(input('Digite um número inteiro: '))
fatorial = 1
for i in range(1, num+1):
    fatorial = fatorial*i
print(f'O fatorial de {num} é {fatorial}')

#  Solução 2

num = int(input('Digite um número inteiro: '))
fatorial = 1
x = 1
while x <= num:
    fatorial *= x
    x += 1
print(f'O fatorial de {num} é {fatorial}')
