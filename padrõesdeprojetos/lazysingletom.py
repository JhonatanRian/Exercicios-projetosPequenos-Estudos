class Singletom:
    __instance = None
    
    def __init__(self) -> None:
        if not Singletom.__instance:
            print("O metodo __init__ foi chamado")
        else:
            print(f'A instancia já foi criada {self.get_instance()}')
            
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singletom()
        return cls.__instance