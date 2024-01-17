import time
import os
from Render.Screen import Screen
from Objects.Objects import Square,Diamond,triangle 
import numpy as np

screen = Screen(False)

diamond = Diamond()
diamond.world = diamond.get_world()
diamond.get_transform(5,5)
screen.paint(diamond.world)

diamond.world = diamond.get_world()
diamond.get_scale(2,2)
diamond.get_transform(20,10)
screen.paint(diamond.world)

square = Square()
for i in range(4):
    square.world = square.get_world()
    square.get_rotation(45 * i)
    square.get_transform(5,15 + (6 * i))
    screen.paint(square.world)


triangle = triangle ()
row = 3
for i in range(9):
    triangle.world = triangle.get_world()
    triangle.get_rotation(45 * i)
    triangle.get_transform(15 + (10 * (i % row)), 25 + (10 * int(i / row)))
    screen.paint(triangle.world)





screen.draw()