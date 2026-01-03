class StatusVariable():
    def __init__(self, name: str, default=None, valid:list=None):
        self.__name = name
        self.__value = default
        self.__valid = valid

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def value(self):
        return self.__value
    
    @property
    def isset(self) -> bool:
        return self.__value is not None
    
    def __str__(self) -> str:
        value = self.value if self.isset else "NIL"
        options = "[" + " | ".join(self.__valid) + "]" if self.__valid is not None else ""
        return f"{self.name}: {value} {options}"