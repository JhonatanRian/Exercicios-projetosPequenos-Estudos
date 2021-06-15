'''
Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:

    Triângulo equilátero: todos os lados possuem o mesmo tamanho;

    Trângulo escaleno: todos os lados possuem medidas diferentes;

    Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.
'''

#  Entrada de dados, valor dos lados do triângulo
ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ladoC = float(input('Lado C: '))
#  Caracterização do triângulo
if ladoA == ladoB == ladoC:
    print('O triângulo é equilátero.')
elif ladoA == ladoB or ladoA == ladoC or ladoB ==ladoC:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')