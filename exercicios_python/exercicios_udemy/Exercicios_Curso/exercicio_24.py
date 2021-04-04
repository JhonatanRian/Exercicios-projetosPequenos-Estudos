'''
O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.

    IMC<17 - Muito abaixo do peso ideal

    17<=IMC<18,5 - Abaixo do peso

    18,5<=IMC<25 - Peso normal

    25<=IMC<30 - Acima do peso

    30<=IMC<35 - Obesidade I

    35<=IMC<40 - Obesidade II (severa)

    IMC>=40 - Obesidade III (mórbida)
    
Lembre que: IMC=massa/(altura*altura)
Fonte: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal
'''
print('\nCalculo do IMC\n')
nome = str(input(f'Qual seu nome?\n»»')).strip().title()
idade = int(input(f'\nQual a sua idade?\n»»'))
peso = float(input(f'\nQual seu peso?\n»»'))
alt = float(input(f'\nIndique sua altura: '))
imc = peso / (alt*alt)

if imc < 17:
    print(f'{nome}, você com {idade} anos de idade está muito abaixo do peso ideal')
elif imc > 17 and imc < 18.5:
    print(f'{nome}, você com {idade} anos de idade está abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'{nome}, você com {idade} anos de idade está com peso normal')
elif 25 <= imc < 30:
    print(f'{nome}, você com {idade} anos de idade está acima do peso')
elif 30 <= imc < 35:
    print(f'{nome}, você com {idade} anos de idade está com obesidade I')
elif 35 <= imc < 40:
    print(f'{nome}, você com {idade} anos de idade está com obesidade II (severa)')
elif imc >= 40:
    print(f'{nome}, você com {idade} anos de idade está com obesidade III (mórbida)')
