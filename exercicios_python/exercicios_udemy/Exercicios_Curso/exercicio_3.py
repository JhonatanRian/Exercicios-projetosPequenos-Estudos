'''
Escreva um programa que solicite o nome
sobrenome do usuário. Ao final o programa
deverá apresentar o nome completo do usuário na
tela.
'''
nome = str(input("Qual seu primeiro nome?\n》 ")).strip().title()
sobrenome = str(input("Qual seu sobrenome?\n》")).strip().title()
print(f"Seu nome é {nome} {sobrenome}")