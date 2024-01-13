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
    
class Sphere(DrawAble):
       
    def get_vertexs(self):
        return np.array([
            (3, 9, 0),
            (6, 6, 0),
            (3, 3, 0),
            (0, 6, 0),
        ])

    