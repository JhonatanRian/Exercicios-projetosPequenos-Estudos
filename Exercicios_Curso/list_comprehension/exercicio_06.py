"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Condição: eleve o número ao quadrado se for par; se o número for ímpar calcule a raiz quadrada - utilize round() para arredondar as casas decimais.


    [1.0, 4, 1.73, 16, 2.24, 36, 2.65, 64, 3.0, 100, 3.32, 144, 3.61, 196, 3.87]
"""

#Sem List Comprehension:


lista1=[]
for numero in range(1,51):
    if numero%2==0:
        lista1.append(numero**2)
    else:
        lista1.append(round(numero**0.5,2))
print(lista1)

#Com List Comprehension:


lista2=[numero**2 if numero%2==0 else round(numero**0.5,2) for numero in range(1,51)]
print(lista2)