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

#=======================================================================
class SingletonClass:

    def __new__(cls):
        if not cls.__dict__.get('_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()


if __name__ == '__main__':
    s1 = SingletonClass()
    s2 = SingletonClass.get_instance()

    print(s1)
    print(s2)
    
#===========================================================================
class SingletonDecorator:

    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def get_instance(self, *args, **kwargs):
        if not self._instance:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

    def __call__(self, *args, **kwargs):
        raise RuntimeError('Classes Singleton têm o construtor privado')


@SingletonDecorator
class Foo:

    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == '__main__':
    # s1 = Foo(a=10, b=20)
    s1 = Foo.get_instance(a=10, b=20)
    s2 = Foo.get_instance(a=10, b=20)

    print(s1 == s2)