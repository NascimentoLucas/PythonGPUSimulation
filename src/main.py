import time
import os
from Render.Screen import Screen
from Objects.Objects import Square,Diamond,Cross 
import numpy as np

screen = Screen()
square = Square()
diamond = Diamond()
cross = Cross ()
item = diamond


screen.paint(item.get_transform(3,3))
screen.draw()