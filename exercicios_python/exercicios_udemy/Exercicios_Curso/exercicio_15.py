'''
Elabore um programa para calcular a hipotenusa de um triângulo.

Dicas:

    Veja o módulo math (math.hypot);

    Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2: 
'''
from math import hypot

x = float(input('Valor do lado x: '))
y = float(input('Valor do lado y: '))
print(f'O valor da hipotenusa é {hypot(x, y):.2f}')