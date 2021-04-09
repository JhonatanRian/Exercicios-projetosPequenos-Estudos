'''
    Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.

    Área: valor da superfície retangular, sendo calculado pela multiplicação entre a altura (h) e a base (b) do retângulo. É expresso pela formula:
    A=b.h.

    Perímetro: valor encontrado quando se soma os quatro lados da figura. É expresso pela fórmula:
    2(b + h).
'''

base = float(input('Por favor indique a base do retângulo: '))
altura = float(input('Por favor indique a altura do retângulo: '))
area = base * altura
perimetro = 2 * (base+altura)
print(f'\nA área do retâgulo é {area} e seu perímetro é {perimetro}')