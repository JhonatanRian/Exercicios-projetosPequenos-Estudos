'''
    Escreva um programa que mostre na tela o tipo de cada dado
    da lista a seguir. Utilize a função built-in type.
    
        lista=[
        (1,),
        [1,2,3],
        (1),
        {4,5},
        {'nome':'A','value':2},
        10,
        [],
        1+3j,
        1.2,
        True,
        False,
        None,
        'Hello World!',
    ]
'''

lista=[
    (1,),
    [1,2,3],
    (1),
    {4,5},
    {'nome':'A','value':2},
    10,
    [],
    1+3j,
    1.2,
    True,
    False,
    None,
    'Hello World!',
]
    
for elemento in lista:
    print(elemento,type(elemento))