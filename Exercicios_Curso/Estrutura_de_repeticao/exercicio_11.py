'''
    Em um único loop escreva um programa que mostre na tela de 0-5, cinco vezes e
    ao final mostre a mensagem Fim . Utilize apenas for em sua implementação.
'''

for i in range(0, 6):
    print(i)

    if i == 5:
        for j in range(0, 6):
            print(j)

            if j == 5:
                for k in range(0, 6):
                    print(k)

                    if k == 5:
                        for l in range(0, 6):
                            print(l)

                            if l == 5:
                                for m in range(0, 6):
                                    print(m)

                                    if m == 5:
                                        print('Fim')
