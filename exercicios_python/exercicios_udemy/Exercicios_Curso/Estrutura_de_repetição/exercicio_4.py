'''
    Escreva um programa de contagem regressiva, ou seja, imprima na tela o seguinte padrão numérico:
'''

from time import sleep

#  Solução 1
for num in range(5, -1, -1):
    print(num)
    sleep(0.5)

#  Solução 2
x = 5
while x >= 0:
    print(x)
    x -= 1