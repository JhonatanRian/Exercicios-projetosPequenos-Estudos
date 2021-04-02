'''
Elabore um programa para calcular a hipotenusa de um triângulo.

Dicas:

    Veja o módulo math (math.hypot);

    Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2: 
'''
from math import hypot

cateto_a = float(input('Cateto oposto: '))
cateto_o = float(input('Cateto adjacente: '))

print(f'O valor da hipotenusa é {(cateto_o**2+cateto_a**2)**(1/2):.2f}')#valor atrávez da formula
print(f'O valor da hipotenusa é {hypot(cateto_a, cateto_o):.2f}')#valor usando a blibioteca math