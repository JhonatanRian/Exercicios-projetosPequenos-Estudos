"""
    A partir da lista abaixo obtenha apenas a string "Python".
    lista=[
        'a','b','c',([
            [[[[['a'],[-90,33,33,['Python']],[0,1,2]],[4,4]],[],'u'],[]]
        ]),{'a':1,'c':2},3
    ]
"""

lista=[
'a','b','c',([
    [[[[['a'],[-90,33,33,['Python']],[0,1,2]],[4,4]],[],'u'],[]]
]),{'a':1,'c':2},3
]

print(lista[3][0][0][0][0][1][3][0])