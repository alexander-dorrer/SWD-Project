import pygame

class Enemy:

    def __init__(self, window):
        self.width = 65
        self.height = 65
        self.win = window
        self.enemy_animation_imgs = [
            pygame.image.load('Assets/Enemy/WALK_000.png'),
            pygame.image.load('Assets/Enemy/WALK_001.png'),
            pygame.image.load('Assets/Enemy/WALK_002.png'),
            pygame.image.load('Assets/Enemy/WALK_003.png'),
            pygame.image.load('Assets/Enemy/WALK_004.png'),
            pygame.image.load('Assets/Enemy/WALK_005.png'),
            pygame.image.load('Assets/Enemy/WALK_006.png')
    ]
        
    def draw_enemy(self):
        self.win.blit(pygame.transform.scale(self.enemy_animation_imgs[1], (self.width, self.height)), (0, 770))

