from abc import abstractmethod
import numpy as np

class DrawAble:
    def __init__(self):
        self.vertexs = self.get_world()
        self.x = 0
        self.y = 0
        
    @abstractmethod
    def get_world(self):
        pass

    def get_transform(self, dX, dY):
        translation_matrix = np.array([
            (1, 0, dX),
            (0, 1, dY),
            (0, 0, 1), 
        ]) 

        result = self.vertexs
        for i in range(int(len(self.vertexs))):
            world = np.array([
                    (1, 0, self.vertexs[i][0]),
                    (0, 1, self.vertexs[i][1]),
                    (0, 0, self.vertexs[i][2]), 
                ]) 
           
            dot = np.dot(world, translation_matrix)
            result[i][0] = dot[0][2]
            result[i][1] = dot[1][2]
            result[i][2] = dot[2][2]

        print(result)
        return result




    
        

