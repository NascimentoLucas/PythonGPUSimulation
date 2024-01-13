import math

class RenderTriangule:
    def __init__(self,p1,p2,p3):
        self.p = [p1,p2,p3]

        self.arrX = [p1[0],p2[0],p3[0]]
        self.arrX.sort()
        self.arrY = [p1[1],p2[1],p3[1]]
        self.arrY.sort()

    def get_min_x(self):
        return self.arrX[0]
    def get_max_x(self):
        return self.arrX[len(self.arrX) - 1]
    
    def get_min_y(self):
        return self.arrY[0]
    def get_max_y(self):
        return self.arrY[len(self.arrY) - 1]

    def get_distance(self, p1, p2):
        return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

    def get_area(self, p1,p2,p3):
        #print(f'{p1};{p2};{p3}', end= '#')
        v1 = self.get_distance(p1 , p2)
        v2 = self.get_distance(p2 , p3)
        v3 = self.get_distance(p3 , p1)
        p = (v1 + v2 + v3) /2
                      
        return math.sqrt(p * (p - v1) * (p - v2) * (p - v3))

    def is_inside(self, x, y):
        tri = self.get_area(self.p[0], self.p[1], self.p[2])
        sum = 0
        for i in range(len(self.p)):
            r = self.get_area([x,y], self.p[i], self.p[(i+1) % len(self.p)])
            print(f'{r} + ', end='')
            sum += r

        print(f' = {[x,y]}: {sum}/{tri}')
        return sum == tri

    def draw_bound(self, screen):

        startX = self.get_min_x()
        endX = self.get_max_x()

        startY = self.get_min_y()
        endY = self.get_max_y()


        x = startX
        y = startY
        while(x <= endX):

            y = startY
            while(y <= endY):  
                if(self.is_inside(x, y)):                
                    screen[x][y] = " ^ "
                else:
                    screen[x][y] = " . "
                y+=1

            x+=1



   
