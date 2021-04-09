'''
    Faça um programa que peça uma temperatura em Fahrenheit (F) e converta
    esta temperatura para grau Celsius (C), mostrando o resultado da
    conversão na tela.

    Use a fórmula: C = 5 * ((F-32) / 9).
'''

f = float(input('Temperatura (F): '))
c = 5 * ((f-32) / 9)
print(f'{f:.2f}° Fahrenheit equivale a {c:.2f}')
