"""
    Utilize Compreensão em Lista (List Comprehension) para criar a 
    lista a seguir. Observe que esses números são obtidos através 
    da raiz quadrada de cada número no intervalo [1,50]. Utilize 
    round() para arredondar as casas decimais.
"""

lista=[round(numero**0.5,2) for numero in range(1,51)]