class MonoState:
    
    __estado = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls).__new__(cls, *args, *kwargs)
        obj.__dict__ = cls.__estado