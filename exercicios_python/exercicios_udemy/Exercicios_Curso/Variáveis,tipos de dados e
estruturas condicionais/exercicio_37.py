'''
Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene as vogais em uma lista e implemente sua solução. Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.
'''
letra = input('Digite uma letra: ')
vogais = ['a', 'e', 'i', 'o', 'u']
if letra in vogais:
    print('A letra digitada é uma vogal.')
else:
    print('A letra digitada é uma consoante.')
