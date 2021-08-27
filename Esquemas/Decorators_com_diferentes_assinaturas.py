"""
Decorators com diferentes assinaturas (Diferentes parametros de entrada)

Ultilizaremos um padrão de projeto chamado decorators pattern

Para multiparametros será usado args* e kargs**

#  A assinatura de uma função é representada pelo seu retorno, nome e parametros de entrada


def gritar(funcao):  # Esse função é generators functions que sera usada para decorar outras funções
    def aumentar(*args, **kargs):
        return funcao(*args, **kargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá eu sou o/a {nome}'

@gritar
def pedir(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor'

#  testando

print(pedir('Picanha', 'Batata frita'))
"""


#  Decorators com argumento

def verifica_primeiro_argumento(valor):
    def var(funcao):
        def outra(*args, **kargs):
            if args and args[0] != valor:
                return f'Valor incorreto! O primeiro valor precisa ser {valor}'
            return funcao(*args, **kargs)
        return outra
    return var

@verifica_primeiro_argumento("pizza")
def comida(*args):
    print(args)
    
@verifica_primeiro_argumento(10)
def soma_dez(nun1, num2):
    return nun1 + num2

print(comida('macarrao', 'goiba'))

print(soma_dez(10, 99))