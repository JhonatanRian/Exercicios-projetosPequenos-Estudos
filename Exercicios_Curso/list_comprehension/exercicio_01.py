"""
    Utilize Compreensão em Lista (List Comprehensions) para criar a lista a seguir.

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

#  Sem List comprehension:

lista=list()
for numero in range(10):
    lista.append(numero)
print(lista)

#  Com List comprehension:

lista=[numero for numero in range(10)]
print(lista)