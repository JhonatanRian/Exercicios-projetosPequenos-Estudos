"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir.

    [1, 3, 5, 7, 9]
"""

# Sem List Comprehension:

lista1=list()
for numero in range(1,11):
    if numero%2!=0:
        lista1.append(numero)

# Com List Comprehension:


lista2=[numero for numero in range(1,11) if numero%2!=0]