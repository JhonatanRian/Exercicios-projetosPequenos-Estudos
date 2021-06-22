'''
    Considere um número inteiro positivo n especificado pelo usuário. Elabore um programa que calcule e mostre na tela:

    A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;

    A soma dos n primeiros números pares;

    A soma dos n primeiros números ímpares.
'''
soma_par = 0
soma_impar = 0
contar = 0
n = int(input('Digite um numero: '))

if n > 0:
    for i in range(n):
        contar += i
        if i % 2 == 0:
            soma_par += i
        elif i % 2 == 1:
            soma_impar += i
    
print(contar, soma_par, soma_impar)