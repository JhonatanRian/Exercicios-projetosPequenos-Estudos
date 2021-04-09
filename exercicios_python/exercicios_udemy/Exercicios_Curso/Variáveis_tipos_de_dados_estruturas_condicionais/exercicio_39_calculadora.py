'''
    Implemente uma calculadora simples com as operações aritméticas básicas.
    O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamen-
    te inserir dois valores. Caso, o usuário escolha divisão e insira o valor
    do denominar 0 mostre uma mensagem personalizada. Para os demais casos,
    mostre na tela o resultado da operação desejada.
'''
#  Titulo do programa
print('\n{c:-^50}\n'.format(c="Calculadora"))

#  verifica qual operação será ultilizada
op = str(input('Indique a opearção a ser realizada (+) (x) (/) (-) \n »» ')).strip()

#  Verifica se foi digitado uma operação corretamente
if op in '+x/-':
    #  entrada de dados
    n1 = float(input('n1: '))
    n2 = float(input('n2: '))
    #  realização do calculo
    if op == "+":
        print(f'{n1} + {n2:} = {n1+n2:.2f}')
    if op == 'x':
        print(f'{n1} x {n2:} = {n1*n2:.2f}')
    if op == '/':
        print(f'{n1} / {n2:} = {n1/n2:.2f}')
    if op == '-':
        print(f'{n1} - {n2:} = {n1-n2:.2f}')
else:
    print('Opção invalida')
