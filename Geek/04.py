'''
    Faça um programa que preencha um vetor com 10 numeros reais calcule e
    mostre a quantidade de numeros negativos e a soma dos numeros positivos
    desse vetor.
'''

#  Primeira tentativa
#vetor = list()
#menor = 0
#maior = 0

#for i in range(10):
#    vetor.append(float(input('Numero: ')))
#    if vetor[i] < 0:
#        menor += vetor[i]
#    else:
#        maior += vetor[i]

#  Segunda tentativa

vetor2 = list()

for i in range(10):
    vetor2.append(float(input('Numero: ')))

menor = [x for x in vetor2 if x < 0]
maior = [x for x in vetor2 if x > 0]
print(len(menor))
print(sum(maior))