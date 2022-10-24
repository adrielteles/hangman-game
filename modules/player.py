class Player:

    def __init__(self, name: str, score:float) -> None:
        
        self.__name = name
        self.__score = score

    #Methods

    @property
    def name(self):
        return self.__name
    
    @property
    def score(self):
        return self.__score
