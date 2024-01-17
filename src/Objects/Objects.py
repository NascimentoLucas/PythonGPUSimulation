from Render.DrawAble import DrawAble
import numpy as np

class Square(DrawAble):
       
    def get_world(self):
        l = 2
        a = (l, l, 0)
        b = (l, -l, 0)
        c = (-l, -l, 0)
        d = (-l, l, 0)
        return np.array([
            a,b,d,
            b,c,d,
        ])
    
class Diamond(DrawAble):
       
    def get_world(self):
        l = 5
        a = (0, l, 0)
        b = (l, 0, 0)
        c = (0, -l, 0)
        d = (-l, 0, 0)
        return np.array([
            a,b,d,
            b,c,d,
        ])
    

class triangle (DrawAble):
       
    def get_world(self):
        l = 2
        a = (-l, 0, 0)
        b = (0, l, 0)
        c = (l, 0, 0)
        return np.array([
            a,b,c,
        ])

    