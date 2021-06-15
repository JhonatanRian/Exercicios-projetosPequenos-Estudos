'''
    Escreva um programa que peça dois números e apresente a divisão e
    multiplicação entre eles. A tela de apresentação deverá seguir o 
    seguinte formato:

    "[número1]x[número2]=[multiplicação]"

    "[número1]/[número2]=[divisão]"
'''

numero1 = int(input('n1: '))
numero2 = int(input('n2: '))
print(f'{numero1} + {numero2} = {numero1+numero2}')
print(f'{numero1} x {numero2} = {numero1*numero2}')