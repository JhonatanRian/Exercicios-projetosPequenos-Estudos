'''
Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.

Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.

Dica: você pode usar a biblioteca math para pegar a constante pi.
'''
from math import pi

raio = float(input("Qual o valor do raio?\n》 "))
print(f"O valor da area é {pi*raio**2:.2f}")