"""
    Considere a lista abaixo e faça um programa que some todos
    os seus elementos.Tente implementar ao menos duas soluções.
    
    lista=[10,2,40,50,-2,3,100,21,33,29,123,234,32,88,90,23] 
"""

lista = [10,2,40,50,-2,3,100,21,33,29,123,234,32,88,90,23]

#Solução 1
soma = sum(lista)
print(soma)

#solução 2
soma = 0
for i in lista:
    soma += i
print(lista)
