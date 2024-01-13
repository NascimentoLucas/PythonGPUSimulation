from Render.DrawAble import DrawAble
import numpy as np

class Square(DrawAble):
       
    def get_world(self):
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
       
    def get_world(self):
        x = 0
        y = 0
        return np.array([
            (x + 0, y + 6, 0),
            (x + 3, y + 9, 0),
            (x + 6, y + 6, 0),            
            
            (x + 6, y + 6, 0),
            (x + 3, y + 3, 0),
            (x + 0, y + 6, 0),

        ]) 
    

class Cross (DrawAble):
       
    def get_world(self):
        a= (0, 1, 0)
        b=(0, 2, 0)
        c=(1, 2, 0)
        d=(1, 3, 0)
        e=(2, 3, 0)
        f=(2, 2, 0)
        g=(3, 2, 0)
        h=(3, 1, 0)
        i=(2, 1, 0)
        j=(2, 0, 0)
        k=(1, 0, 0)
        l=(1, 1, 0)


        return np.array([
            a,b,c,
            c,l,a,

            c,d,e,
            e,f,c,

            f,g,h,
            h,i,f,

            i,j,k,
            k,l,i,

            l,c,f,
            f,i,l,

        ])

    