'''
    Escreva um programa que peça números reais (float) do usuário indefinidamente.
    Caso os números digitados não estejam situados entre 0 e 10 o programa deverá
    ser finalizado, mostrando a soma e a quantidade de números digitados e quais foram.
'''

#  Variável numero sustentará o while e numeros_digitados guardará os numeros
numero = 0
numeros_digitados = list()

while 0 <= numero <= 10:
    #  Usuario entra com o numero
    numero = float(input('Digite um número real entre 0-10: '))
    
    #  Caso o usuario digite um numero acima de 10 e menor que zero
    if numero < 0 or numero > 10:
        print(f'Soma dos números digitados: {sum(numeros_digitados)}')
        print(f'Quantidade de números digitados: {len(numeros_digitados)}')
        print(f'O numeros digitados foi {numeros_digitados}')
        break
    
    #  Adiciona o numero na lista
    numeros_digitados.append(numero)
