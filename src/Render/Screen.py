import os

class Screen:
    def __init__(self):
        self.width =  10
        self.height = 10
        self.screen = []
        for x in range(self.width):
            row = ['.'] * self.height
            self.screen.append(row)

    def draw(self):
        os.system('cls')
        print('-' * 10)
        for x in range(self.width):
            for y in range(self.height):
                print(self.screen[x][y], end = '')

            print('\n')
            
        print('-' * 10)


