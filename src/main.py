import time
import os
from Render.Screen import Screen
from Objects.Objects import Square,Diamond
import numpy as np

screen = Screen()
square = Square()
diamond = Diamond()
diamond.get_vertexs()

#screen.paint(square.get_vertexs())
screen.paint(diamond.get_vertexs())

for i in range(1):
    screen.draw()