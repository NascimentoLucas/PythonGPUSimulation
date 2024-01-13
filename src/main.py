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


delta = 90
rot = 0
for i in range(int(360/delta)):
    item.get_rotation(rot)
    rot+= delta
    screen.paint(item.world)
    screen.draw()
    print(rot)
    time.sleep(1)
    item.world = item.get_world()