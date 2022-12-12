"""
A partir das listas

linguagens=['php','JavaScript']
frases=['Eu amo ','Eu odeio ']

Use List Comprehension e obtenha a seguinte lista:

['Eu amo php !', 'Eu odeio php !', 'Eu amo JavaScript !', 'Eu odeio JavaScript !']

Por fim, tente implementar uma solução sem List Comprehension.
"""

# Sem List Comprehension:

lista=[]
linguagens=['php','JavaScript']
frases=['Eu amo ','Eu odeio ']
for linguagem in linguagens:
    for frase in frases:
        lista.append(frase+linguagem+' !')


# Com List Comprehension:

lista2=[frase+linguagem+' !' for linguagem in linguagens for frase in frases]
