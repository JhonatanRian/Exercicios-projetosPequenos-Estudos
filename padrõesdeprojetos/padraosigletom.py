class Singletom(object):
    
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singletom, cls).__new__(cls)
            print(f"Criando o objeto {cls.instance}")
        return cls.instance
    
s1 = Singletom()
print(f'Instancia: {id(s1)}')

s2 = Singletom()
print(f'Instancia: {id(s2)}')