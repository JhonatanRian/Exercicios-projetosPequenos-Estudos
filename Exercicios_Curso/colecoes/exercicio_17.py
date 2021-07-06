"""
    Mude a chave 'valor' do dicionário produto1 para 99.98.

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
produto1['valor']=98.98
print(produto1)
