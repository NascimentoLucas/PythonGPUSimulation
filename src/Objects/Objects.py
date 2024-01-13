from Render.DrawAble import DrawAble
import numpy as np

class Square(DrawAble):
       
    def get_vertexs(self):
        x = 0
        y = 0
        l = 5
        return np.array([
            (x, y, 0),
            (x, y + l, 0),
            (x + l, y + l, 0),
            
            (x + l, y + l, 0),
            (x + l, y, 0),
            (x, y, 0),
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

    