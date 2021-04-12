'''
    Escreva um programa que peça números inteiros positivos indefinidamente
    e armazene-os em uma lista. O programa deverá ser encerrado caso o número
    digitado seja negativo ou nulo. Ao final mostre na tela a quantidade 
    números pares e ímpares. 
'''
#  Lista que será armazenada os numeros digitados
lista = []

while True:
    num = int(input('Digite um número: '))  #  Pede o numero pro usuario
    if num > 0:  #  Se o numero for maior que zero adiciona na lista
        lista.append(num)
    else:
        break

#  Verificação de numeros pares e impares com comprehensions
par = [par for par in lista if par % 2 == 0]
impar = [impar for impar in lista if impar % 2 == 1]

print(f'Quantidade de números pares: {len(par)}')
print(f'Quantidade de números ímpares: {len(impar)-1}')
print(f'Lista dos numeros pares digitados:\n{par}')
print(f'Lista dos numeros impares digitados:\n{impar}')
