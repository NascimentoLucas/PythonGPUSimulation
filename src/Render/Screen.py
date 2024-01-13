import os
import numpy as np

class Screen:
    def __init__(self):
        self.width =  20
        self.height = 20
        self.screen = np.full((self.width, self.height), "   ")

    def draw(self):
        #os.system('cls')
        print('#' * 10)
        for x in range(self.width):
            for y in range(self.height):
                print(self.screen[x][y], end = '')

            print('\n')

        print('#' * 10)

    def paint(self, drawable):
        for v in range(len(drawable)):
            start = [drawable[v][0], drawable[v][1]]
            end = [drawable[(v + 1) % len(drawable)][0], drawable[(v + 1) % len(drawable)][1]]

            lerpX = max(abs(start[0] - end[0]), 1)            
            lerpY = max(abs(start[1] - end[1]), 1)

            if(lerpX > lerpY):
                lerp = lerpX
            else:
                lerp = lerpY
           
            l = 0
            while(l/lerp <= 1 ):
                x = int(np.interp(l/lerp, [0, 1], [start[0], end[0]]))
                y = int(np.interp(l/lerp, [0, 1], [start[1], end[1]]))
                l += 1
                pixel = f'{x}.{y}'
                self.screen[x][y] = ' * '
            
            



