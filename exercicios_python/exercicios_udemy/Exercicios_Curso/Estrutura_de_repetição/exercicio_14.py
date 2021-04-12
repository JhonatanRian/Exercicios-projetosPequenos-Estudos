'''
        Elabore um programa que calcule e mostre na tela os números pares entre 1 e 200.
'''

for numero in range(1, 201):
    if numero % 2 == 0:
        print(numero, end=' ')