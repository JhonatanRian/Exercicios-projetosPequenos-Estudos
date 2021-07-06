'''
    Elabore um programa para imprimir a sequência de Fibonacci até o n-ésimo termo definido pelo usuário. Certifique que o usuário digite um número inteiro positivo.


0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,...
'''

n_termo = int(input('Deseja imprimir a sequência de Fibonacci até qual termo? '))
    
num1,num2=0,1  #números iniciais da sequência
contador=0
    
if n_termo<=0:
    print('O número deve ser positivo.')
elif n_termo==1:
    print(num1)
else:
    while contador<n_termo:
        print(num1)
        num1,num2=num2,num1+num2  #atualizando os valores
        contador+=1