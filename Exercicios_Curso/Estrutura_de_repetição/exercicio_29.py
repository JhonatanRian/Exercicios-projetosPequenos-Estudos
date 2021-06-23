'''
    Escreva um programa que replique o padrão de caracteres descrito a seguir.

Dica: use loop for.

    *
    **
    ***
    ****
    *****
    *****
    ******
    *******
    ********
    *********
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
'''

for i in range(1,10):
    print('*'*i)
    if i==4:
        print('*'*(i+1))
for i in range(10,0,-1):
    print('*'*i)