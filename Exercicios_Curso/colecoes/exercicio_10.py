"""
    Considere a lista a seguir e escreva um programa para remover os elementos duplicados.


    lista=[
        'a','a','a',
        'b','c','k',
        'a',1,2,3,4,
        'j','l','m',
    ]

"""

lista=[
    'a','a','a',
    'b','c','k',
    'a',1,2,3,4,
    'j','l','m',
]
    
lista=list(set(lista))
print(lista)