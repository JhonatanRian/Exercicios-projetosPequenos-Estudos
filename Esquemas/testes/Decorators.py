"""
    Decorators (Decoradores)
    
    - Decorators são funções
    - Decorators envolvem outras funções e aprimoram seus comportamentos
    - Decorators tbm são exemplos de funções aninhadas
    - Decorators tem uma sintax propia usando "@" (Syntax Sugar/ açucar sintatico)
    
"""

#  Decorators como funções (Sintax não recomendada / Sem açucar sintatico)
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voçê!')
        funcao()
        print('Tenha um otimo dia')
    return sendo

def saudacao():
    print('Seja bem vindo pessoa')
    
teste = seja_educado(saudacao)

#  teste 1
teste() #  Foi passado para o "teste()" um comando/funcao que a saúde a pessoa mas, seja educado

#  teste 2
def raiva():
    print('Não gosto de você!')

raiva_educada = seja_educado(raiva)

raiva_educada()

#  Decorators com sintax sugar (SINTAX RECOMENDADA)
def seja_mesmo_educado(funcao):
    def sendoo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um exelente dia!!')
        
@seja_mesmo_educado
def apresentando():
    print('Meu nome é Marcos')
    
#  testando 1

apresentando()
