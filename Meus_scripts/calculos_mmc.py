from itertools import count

cont = 0
inicia = 2
primo = 0
numeros = []
lista1 = []
comparar = []
lista_primos = []


while True:
    try:
        quant_num = int(input('Quantos numeros voce quer verificar? \n-- '))
        quant_num = abs(quant_num)
        break
    except ValueError:
        print('Erro de digitacao, tente novamente.')

for numero in range(quant_num):
    while True:
        try:
            num = int(input('- '))
            break
        except ValueError:
            print('Digite um numero inteiro para dar certo.')
        
    numeros.append(num)
    
for nu in range(len(numeros)):
    comparar.append(1)
    
while True:
    divisiveis = 0
    nuns = next(count(start=inicia))
    for n in range(1, nuns+1):
        if nuns % n == 0:
            divisiveis += 1
        
    if divisiveis == 2:
        primo = nuns
        inicia = primo
        inicia +=1
        break
    else:
        inicia += 1
        
while True:
    cont = 0
    for numero in numeros:
        if numero % primo == 0:
            cont += 1
            lista1.append(numero/primo)
        elif numero % primo != 0:
            lista1.append(numero)

    if numeros == comparar:
        break
    else:
        for numero in numeros:
            if numero % primo == 0:
                cont += 1
        for nn in range(len(numeros)):
            numeros.pop()
        for nn in lista1:
            numeros.append(nn)
        for nn in range(len(lista1)):
            lista1.pop()
        if cont > 0:
            lista_primos.append(primo)
        if cont == 0:
            while True:
                divisiveis = 0
                nuns = next(count(start=inicia))
                for n in range(1, nuns+1):
                    if nuns % n == 0:
                        divisiveis += 1
                    
                if divisiveis == 2:
                    primo = nuns
                    inicia = primo
                    inicia +=1
                    break
                else:
                    inicia += 1

resultado = 1
for l in lista_primos:
    resultado = resultado * l
    
print('= {re} '.format(re=resultado))