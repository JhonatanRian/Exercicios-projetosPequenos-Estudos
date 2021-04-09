'''
    Elabore um progama para verificar se um ano é bissexto ou não. 
    A condição para ser um ano bissexto é: o ano deve ser divisível
     por 400; ou se for divisível por 4 e não for divisível por 100.
'''

ano = int(input('Ano : '))
if ano % 400 == 0 or (ano % 4 == 0 and not ano % 100 == 0):
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')
