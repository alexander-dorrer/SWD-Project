import pygame
import math
pygame.init()

tower_image = pygame.image.load('assets/tower_image.png')

class Tower:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 2
        self.width = 1
        self.price = [0]
        self.sell_cost = [1]
        self.imgs = []
        self.range = 200
        pass

    def place(self):
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click:
            self.x = Mouse_x
            self.y = Mouse_y
        pass

    def sell(self):
        pass

    def shoot(self):
        pass

    def animate(self):
        pass

