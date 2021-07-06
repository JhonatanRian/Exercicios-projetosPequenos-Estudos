'''
    Peça 5 números do usuário e mostre na tela a média dos números digitados.
'''

numeros = 0

for i in range(5):
    var = int(input('Digite um numero: '))
    numeros += 1
    
media = numeros / 5

print(f'A media dos numeros é média: {media}')