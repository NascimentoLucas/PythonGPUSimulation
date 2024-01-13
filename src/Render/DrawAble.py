from abc import abstractmethod

class DrawAble:
    def __init__(self):
        self.vertexs = []
        
    @abstractmethod
    def get_vertexs(self):
        pass

    
        

