'''
    Escreva um programa que solicite duas notas do
    usuário e apresente a média na tela da seguinte
    forma:

    "A média das notas [nota1] e [nota2] é [média]"
'''

n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
print(f"A média das notas {n1} e {n2} é {(n1+n2)/2}")