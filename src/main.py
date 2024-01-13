import time
import os
from Render.Screen import Screen
from Objects.Objects import Square,Sphere
import numpy as np

screen = Screen()
square = Square()
sphere = Sphere()
sphere.get_vertexs()

screen.paint(square.get_vertexs())
screen.paint(sphere.get_vertexs())

for i in range(1):
    screen.draw()