from abc import abstractmethod
import numpy as np
import math

class DrawAble:
    def __init__(self):
        self.world = self.get_world()
        self.x = 0
        self.y = 0
        
    @abstractmethod
    def get_world(self):
        pass
       

    def get_transform(self, dX, dY):
        translation_matrix = np.array([
            (1, 0, dX),
            (0, 1, dY),
            (0, 0, 1), 
        ]) 

        for i in range(int(len(self.world))):
            world = np.array([
                    (1, 0, self.world[i][0]),
                    (0, 1, self.world[i][1]),
                    (0, 0, self.world[i][2]), 
                ]) 
           
            dot = np.dot(world, translation_matrix)
            self.world[i][0] = dot[0][2]
            self.world[i][1] = dot[1][2]
            self.world[i][2] = dot[2][2]

    def get_scale(self, dX, dY):
        scale_matrix = np.array([
            (dX, 0, 0),
            (0, dY, 0),
            (0, 0, 1), 
        ]) 

        for i in range(int(len(self.world))):
            world = np.array([
                    (self.world[i][0], self.world[i][1], self.world[i][2]),
                ]) 
           
            dot = np.dot(world, scale_matrix)
            self.world[i][0] = dot[0][0]
            self.world[i][1] = dot[0][1]
            self.world[i][2] = dot[0][2]
        
    
    def get_rotation(self, rotation):
        theta = math.radians(rotation)
        
        rotation_matrix_x = np.array([
            [1, 0, 0],
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 1]])
        
        rotation_matrix_y = np.array([
            [np.cos(theta), 0, np.sin(theta)],
            [0,  1, 0],
            [-np.sin(theta), 0, np.cos(theta)]])
        
        rotation_matrix_z = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta),  np.cos(theta), 0],
            [0, 0, 1]])


        for i in range(int(len(self.world))):
            world = np.array([
                    (self.world[i][0], self.world[i][1], self.world[i][2]),
                ]) 
           
            dot = np.dot(world, rotation_matrix_z)
            self.world[i][0] = dot[0][0]
            self.world[i][1] = dot[0][1]
            self.world[i][2] = dot[0][2]
        







    
        

