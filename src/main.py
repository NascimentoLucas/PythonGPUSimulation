import time
import os
from Render.Screen import Screen

screen = Screen()

for i in range(10):
    screen.draw()
    time.sleep(1)