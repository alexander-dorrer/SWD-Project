import pygame
import math
pygame.init()

tower_base_image = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Base.png')
tower_head_image = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Head.png')

class Tower:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 2
        self.width = 1
        self.price = [0]
        self.sell_cost = [1]
        self.tower_base_img = tower_base_image
        self.tower_head_img = tower_head_image
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

