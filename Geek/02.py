"""
    Ler um conjuntos de numeros reais armazenando em um vetor e calculando
    o quadrado dos componetes deste vetor, armazendo o resultado em outro
    vetor. cada um com 10 elemento.
"""
#  declarando as listas que serão trabalhada
vetor_1 = list()
vetor_2 = list()

#  loop de 10 vezes para recolher os numeros e adicionar no vetor_1
for i in range(1, 10):
    while True:
        try:
            vetor_1.append(int(input('Adicione um numero: ')))
            break
        except:
            print('Erro de digitação, tente novamente')

#  loop para passar os numeros do vetor_1 para vetor_2 calculando-o
for numero in vetor_1:
    #  adiciona o numero do vetor_1 somando seu quadrado
    vetor_2.append(numero**2)
    
print(vetor_1)
print(vetor_2)