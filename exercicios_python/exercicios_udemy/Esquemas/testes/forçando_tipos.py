'''
Forçando tipod de dados com decoradores
'''

def forca(*tipos):
    def decorador(funcao):
        def converte(*args, **kargs):
            novo_arg = []
            for (valor, tipo) in zip(args, tipos):
                novo_arg.append(tipo(valor))
                return funcao(novo_arg, **kargs)
            return converte
        return decorador

@forca
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)