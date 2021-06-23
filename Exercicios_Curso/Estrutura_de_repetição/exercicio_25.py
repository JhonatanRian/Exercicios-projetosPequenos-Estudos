'''
    Elabore um programa para imprimir todos os números primos 
    existentes em um intervalo delimitado pelo usuário.
'''

num1=int(input('Número inferior do intervalo: '))
num2=int(input('Número superior do intervalo: '))
     
for numero in range(num1,num2+1):
    if numero>1:
        for k in range(2,numero):
            if numero%k==0:
                break
        else:
            print(numero)