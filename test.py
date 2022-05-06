import pygame
import tower
import enemy
pygame.init()


# class TowerCircle(pygame.sprite.Sprite):
#     def __init__(self, centerx, centery,Tower):
#         super().__init__()
#         self.image = pygame.image.load('assets/Towers&Projectiles/Collision_Circle/collision_circle.png')
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect = self.image.get_rect(center = (centerx, centery))
#
#
#
#
# class Enemy(pygame.sprite.Sprite,Enemy):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.image.load('Assets/Enemy/WALK_000.png')
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect = self.image.get_rect(topleft = (x, y))
#
#
#
# pygame.display.set_caption("Tower Defense")
# width = 1200
# height = 840
# display_surface = pygame.display.set_mode((width, height))
#
# my_enemy = Enemy(50,50)
# my_tower = TowerCircle(50,50)
#
# while True:
#     enemy_sprite = pygame.sprite.GroupSingle(my_enemy.mask)
#     tower_sprite = pygame.sprite.GroupSingle(my_tower.mask)
#     if pygame.sprite.spritecollide(enemy_sprite.sprite,tower_sprite,False,pygame.sprite.collide_mask()):
#         print("collision")


# def draw_range(self):
#     for tower in self.positions:
#         surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
#         pygame.draw.circle(surface, (50, 50, 50, 100), (self.range, self.range), self.range, 0)
#         self.window.blit(surface, (tower[0] - self.range, tower[1] - self.range))
#     self.draw_towers()
