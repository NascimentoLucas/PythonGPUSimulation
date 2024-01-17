import time
import os
from Render.Screen import Screen
from Objects.Objects import Square,Diamond,Cross 
import numpy as np

screen = Screen()

square = Square()
diamond = Diamond()
cross = Cross ()
item = cross


delta = 1
rot = 0
for i in range(int(360/delta)):
    item.get_rotation(rot)
    item.get_transform(20,7)
    rot+= delta
    screen.paint(item.world)
    screen.draw()
    print(rot)
    item.world = item.get_world()