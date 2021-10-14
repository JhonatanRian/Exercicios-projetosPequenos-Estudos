"""
Utilize Compreensão em Lista (List Comprehensions) para criar as listas a seguir.

Lembre que:

    [f(x) for x in sequence if condition]
    [f(x) if condition else g(x) for x in sequence]
"""

par=[numero for numero in range(1,101) if numero%2==0]

impar=[numero for numero in range(1,101) if numero%2!=0]