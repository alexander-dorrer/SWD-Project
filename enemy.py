from calendar import c
from distutils.spawn import spawn
import pygame



class Enemy:

    def __init__(self, window, path):
        self.animation_count = 0
        self.width = 55
        self.height = 55
        self.window = window
        self.enemy_animation_imgs = [
            pygame.image.load('Assets/Enemy/WALK_000.png'),
            pygame.image.load('Assets/Enemy/WALK_001.png'),
            pygame.image.load('Assets/Enemy/WALK_002.png'),
            pygame.image.load('Assets/Enemy/WALK_003.png'),
            pygame.image.load('Assets/Enemy/WALK_004.png'),
            pygame.image.load('Assets/Enemy/WALK_005.png'),
            pygame.image.load('Assets/Enemy/WALK_006.png')
        ]
        self.path = path
        self.step = 1
        self.x = 0
        self.y = 0
        self.next_step = [self.path[self.step][0] * 60, self.path[self.step][1] * 60]
        self.enemy_mask_image = pygame.image.load('Assets/Enemy/WALK_000.png')
        #self.enemy_sprite.image = self.enemy_mask_image
        self.enemy_mask = pygame.mask.from_surface(self.enemy_mask_image)



    def draw_enemy(self, spawn_point_x, spawn_point_y):
        self.x, self.y = spawn_point_x, spawn_point_y
        self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[0], (self.width, self.height)),
                         (self.x, self.y))

    def move(self):
        goal_position = [self.path[len(self.path) - 1][0] * 60, self.path[len(self.path) - 1][1] * 60]
        current_position = [self.y, self.x]
        if current_position != goal_position:
            if current_position == self.next_step:
                self.step += 1
                self.next_step = [self.path[self.step][0] * 60, self.path[self.step][1] * 60]

            if current_position[0] != self.next_step[0]:
                if current_position[0] > self.next_step[0]:
                    self.y -= 4
                    self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                            (self.width, self.height)), (self.x, self.y))
                elif current_position[0] < self.next_step[0]:
                    self.y += 4
                    self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                            (self.width, self.height)), (self.x, self.y))
            elif current_position[1] != self.next_step[1]:
                if current_position[1] > self.next_step[1]:
                    self.x -= 4
                    self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                            (self.width, self.height)), (self.x, self.y))
                elif current_position[1] < self.next_step[1]:
                    self.x += 4
                    self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                            (self.width, self.height)), (self.x, self.y))
        if self.animation_count >= 6:
            self.animation_count = 0
        else:
            self.animation_count += 1
