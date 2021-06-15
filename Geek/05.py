'''
    Faça um programa que leia uma matrix de 5 linhas e 4 colunas, contendo sobre
    as seguintes informações sobre os alunos de uma diciplina, sendo todas as 
    informações do tipo inteiro: 
    
    - Primeira coluna: Numero de matricula
    - Segunda coluna: Media das provas 
    - terceira coluna: Media dos trabalhos
    - quarta coluna: Nota final
    
    Elabore um programa que: 
    - Leia as 3 primeiras informações de cada aluno
    - Calcule a nota final que é mediaprovas+mediatrabalhos
    - Imprima a matricula do aluno que obteve a maior nota final
    - imnprima a media das notas finais
'''

from time import sleep
from os import system as tela
from copy import deepcopy as copiar

def converter_numero(funcao):
    '''
    Essa é uma decorators functions que converte o argumento da "função ler_numeros"
    para numeros, caso não dê de fazer isso retorna 0.
    '''
    def interna(*args, **kargs):
        try:
            int(args[0])
            return funcao(*args, **kargs)
        except ValueError:
            try:
                float(args[0])
                return funcao(*args, **kargs)
            except ValueError:
                return False
    return interna

@converter_numero
def ler_numeros(digitados):
    '''
    Função usada para ler a string colocada como parametro
    '''
    str(digitados)
    return digitados

matrix = list()
linhas = list()
num_valor = dict()

for linha in range(1, 6):
    while True:
        linhas.append(ler_numeros(input('Digite o numero de matricula do aluno: ')))
        linhas.append(ler_numeros(input('Digite o numero de Media das provas: ')))
        linhas.append(ler_numeros(input('Media dos trabalhos: ')))
        print('Verificando...')
        sleep(2.5)
        tela('clear')
        if False in linhas:
            print('Algum numero saio errado. Refaça novamente por favor em 3 segundos...')
            linhas.clear()
            sleep(3)
        else:
            valor_total = float(linhas[1])+float(linhas[2])
            linhas.append(str(valor_total))
            linhas = [float(x) for x in linhas]
            matrix.append(linhas[:])
            break
    num_valor[linhas[3]] = linhas[0]
    linhas.clear()

maior = max([x for x in num_valor.keys()])
media = sum([x for x in num_valor.keys()]) / len(num_valor)

print(f'Matricula do aluno com maior nota: {num_valor[maior]:.0f}')
print(f'A media das notas finais: {media:.1f}')