import pygame


class Player:
    """Player Class"""

    def __init__(self, window, height: int, width: int):
        self.health_points = 100
        self.window = window
        self.height = height
        self.width = width

    def enemy_finished(self, enemy_hp: float):
        if enemy_hp != 0:
            print('Enemy health = ' + str(enemy_hp))
            self.health_points -= enemy_hp

    def display_hp(self):
        hearth = pygame.image.load("Assets/UI/Icon_Hearth.png")
        color = (255, 255, 255)
        smallfont_player_hp = pygame.font.SysFont('Comic Sans MS', 34)
        self.window.blit(pygame.transform.scale(hearth, (30, 30)), (self.width - 125, 10))
        hp_value = smallfont_player_hp.render(" " + str(self.health_points), True, color)
        self.window.blit(hp_value, (self.width - 95, 0))

    def player_hp(self) -> float:
        return self.health_points
