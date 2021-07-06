"""
    Considere a tupla1 e responda as seguintes questões:

    tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')
    
    a) mostre na tela o tamanho desta tupla;

    b) ordene a tupla e mostre o resultado na tela;

    c) mostre na tela o número de ocorrências da string 'A';

    d) mostre na tela o número de ocorrências da string 'B';

    e) mostre na tela o índice da string 'X';

    f) mostre na tela o último elemento da tupla1.
"""

tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')
#a)
print(f'Tamanho da tupla1:',len(tupla1))
#b)
print(sorted(tupla1))
#c)
print("Número de ocorrências de 'A' ",tupla1.count('A'))
#d)
print("Número de ocorrências de 'B' ",tupla1.count('B'))
#e)
print("Índice da string 'X' ",tupla1.index('X'))
#f)
print(tupla1[-1])