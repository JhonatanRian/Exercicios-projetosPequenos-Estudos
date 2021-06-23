'''
    Escreva um programa que replique o padrão de números a seguir, tal que o usuário insira o n-ésimo termo.



    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
    1 2 3 4 5 6 
    1 2 3 4 5 6 7 
    1 2 3 4 5 6 7 8 
    1 2 3 4 5 6 7 8 9 
    1 2 3 4 5 6 7 8 9 10 
          ...
    1 2 3 4 5 6 7 8 9 10 ... n
'''

num=int(input('N-ésimo termo: '))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()