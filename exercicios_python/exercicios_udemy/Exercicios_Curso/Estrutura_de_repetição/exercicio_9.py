'''
    Em um único loop escreva um programa que mostre na tela de 1 a 10 três vezes e
    ao final mostre a mensagem Fim . No primeiro loop utilize for e nos dois loops
    seguintes while.
'''

 #solução 1
x = 1
    for i in range(1, 11):
        print(i)
        if i == 10:
            while x <= 10:
                print(x)
                x += 1
                if x == 11:
                    y = 1
                    while y <= 10:
                        print(y)
                        y += 1
                        if y == 11:
                            print('Fim')

#solução 2
x = 11
for a in range(1, 4):
    for x in range(1, 11):
        print(x)
