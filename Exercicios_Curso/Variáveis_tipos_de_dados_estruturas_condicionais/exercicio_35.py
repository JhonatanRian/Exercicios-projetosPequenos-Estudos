'''
    Escreva um script que mostre na tela o preço de um produto associado a 
    uma categoria especificada pelo usuário.  Utilize como referência as 
    informações a seguir. Caso o usuário não digite uma categoria válida 
    (número entre 1 e 10) mostre na tela uma mensagem personalizada.
    
    Exemplo: preço x categoria
    * Categoria 1 - $ 0,5 
    * Categoria 2 - $ 11,3
    * Categoria 3 - $ 17,5
    * Categoria 4 - $ 33,97
    * Categoria 5 - $ 103,47
    * Categoria 6 - $ 44,67
    * Categoria 7 - $ 12,55
    * Categoria 8 - $ 14,87
    * Categoria 9 - $ 98,12
    * Categoria 10 - $ 131,4
'''

categoria = int(input('Digite a categoria do produto: '))
if categoria == 1:
    print('O preço do produto é: $ 0.5')
elif categoria == 2:
    print('O preço do produto é: $ 11.3')
elif categoria == 3:
        print('O preço do produto é: $ 17.5')
    elif categoria == 4:
        print('O preço do produto é: $ 33.97')
    elif categoria == 5:
        print('O preço do produto é: $ 103.47')
    elif categoria == 6:
        print('O preço do produto é: $ 44.67')
    elif categoria == 7:
        print('O preço do produto é: $ 12.55')
    elif categoria == 8:
        print('O preço do produto é: $ 14.87')
    elif categoria == 9:
        print('O preço do produto é: $ 98.12')
    elif categoria == 10:
        print('O preço do produto é: $ 131.4')
    else:
        print('Opção inválida.')