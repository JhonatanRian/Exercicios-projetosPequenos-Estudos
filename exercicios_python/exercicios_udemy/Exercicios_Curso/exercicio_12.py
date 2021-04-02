'''
Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:

"Seja bem-vindo [nome] [sobrenome]."

"Você possui [idade] anos de idade."
'''
nome = str(input('nome: ')).strip().capitalize()
sobrenome = str(input('sobrenome: ')).strip().capitalize()
idade = str(input('idade: '))
print(f'Bem vindo {nome} {sobrenome}.\nVocê possui {idade} anos de idade.')