"""
    Crie um script para iterar no dicionário abaixo e mostrar na tela todas as suas chaves, uma a uma.


    produto1={
        'nome':'produto1',
        'tipo':'categoriaA',
        'valor':'50.5',
        'fornecedor':'ABCD',
    }
"""

produto1={
        'nome':'produto1',
        'tipo':'categoriaA',
        'valor':'50.5',
        'fornecedor':'ABCD',
    }

for chave in produto1:
    print(chave)
        
for chave in produto1:
    print(produto1[chave])
    
for chave,valor in produto1.items():
    print(chave,valor)