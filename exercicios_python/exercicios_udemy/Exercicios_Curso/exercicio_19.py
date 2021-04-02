'''
Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. Ao fim, calcule seu novo salário considerando cenários hipotéticos, com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá seguir o seguinte padrão:

"Olá, [nome] [sobrenome]"

"Seu salário atual é : [salário]"

"Seu salário com 10% de aumento é: [salário]"

"Seu salário com 25% de aumento é: [salário]"

"Seu salário com 30% de aumento é: [salário]"

"Seu salário com 50% de aumento é: [salário]"

No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e após a string, enquanto que o último permite colocar a string no formato titlecased (capitaliza string).
'''
nome = str(input('Nome: ')).strip().title()
sobrenome = str(input('Sobrenome: ')).strip().title()
salario = float(input(f'{nome} {sobrenome}, por favor informe seu salario: '))

print(f'Olá {nome} {sobrenome}\n')
print(f"Seu salário com 10% de aumento é: {(salario*0.10)+salario}")
print(f"Seu salário com 25% de aumento é: {(salario*0.25)+salario}")
print(f"Seu salário com 30% de aumento é: {(salario*0.30)+salario}")
print(f"Seu salário com 50% de aumento é: {(salario*0.50)+salario}")