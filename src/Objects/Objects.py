from Render.DrawAble import DrawAble
import numpy as np

class Square(DrawAble):
       
    def get_vertexs(self):
        return np.array([
            (5, 5, 0),
            (10, 5, 0),
            (10, 10, 0),
            (5,10, 0),
        ])
    
class Diamond(DrawAble):
       
    def get_vertexs(self):
        x = 5
        y = 5
        return np.array([
            (x + 0, y + 6, 0),
            (x + 3, y + 9, 0),
            (x + 6, y + 6, 0),            
            
            (x + 6, y + 6, 0),
            (x + 3, y + 3, 0),
            (x + 0, y + 6, 0),

        ])

    