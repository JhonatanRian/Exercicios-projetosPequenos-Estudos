'''
    Leia uma temperatura em graus Celsius e a a converta para Fahrenheit.
    A formula é F = c*(9.0/5.0)+32
'''
#  Pede o numero que será usado na conversão
C = float(input('Digite o numero que quer converter: '))
#  conversão do C 
F = C*(9.0/5.0)+32
print(f'{C}° Celsius vale {F}° Fahrenheit.')
