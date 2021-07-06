"""
    Considere a lista abaixo. Escreva um programa que obtenha uma 
    lista ordenada a partir da lista1. A ordenação deverá ser 
    efetuada em ordem crescente pelo último elemento de cada tupla.


    lista1=[('a',21,10),('q',44,99),
           ('z',321,11),('w',91,33),
           ('f',33,-9),('h',88,42),
           ('j',-100,1),('n',74,93),
           ('k',11,7),('m',923,-10),
           ('l',2,23),('v',612,57),
           ('j',130,51),('x',40,88),
           ('b',99,67),('u',30,49),
           ('e',-120,-4),('i',40,21),
          ]
"""

lista1=[('a',21,10),('q',44,99),
           ('z',321,11),('w',91,33),
           ('f',33,-9),('h',88,42),
           ('j',-100,1),('n',74,93),
           ('k',11,7),('m',923,-10),
           ('l',2,23),('v',612,57),
           ('j',130,51),('x',40,88),
           ('b',99,67),('u',30,49),
           ('e',-120,-4),('i',40,21),
          ]

lista = sorted(lista1, key=lambda elemento:elemento[2])

print(lista)