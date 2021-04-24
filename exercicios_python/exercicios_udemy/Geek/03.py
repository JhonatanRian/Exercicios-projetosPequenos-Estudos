'''
    Crie um programa que leia um vetor de 8 poicições, em seguida leia também 
    2 valores x e y, quais corespondem as pocições do no vetor. ao final do 
    programa ele descreverá a soma dos valores nas pocições x e y.
'''

vetor = list()

#  Lendo valores e adicionando no vetor
for numero in range(10):
    vetor.append(int(input('n°: ')))

# obtendo pocições x e y
x = int(input('posição(x): '))
y = int (input('posição(y): '))

print(f'{vetor[x]} + {vetor[y]} = {vetor[x]+vetor[y]}')