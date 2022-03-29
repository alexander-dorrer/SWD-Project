import pygame


class Player:
    """Player Class"""

    def __init__(self, window, height, width):
        self.health_points = 100
        self.window = window
        self.height = height
        self.width = width

    def enemy_finished(self, enemy_hp):
        if enemy_hp != 0:
            print('Enemy health = ' + str(enemy_hp))
            self.health_points -= enemy_hp

    def display_hp(self):
        color = (255, 255, 255)
        smallfont_player_hp = pygame.font.SysFont('Comic Sans MS', 34)
        main_menu_text = smallfont_player_hp.render('Player HP: ' + str(self.health_points), True, color)
        self.window.blit(main_menu_text, (self.width - 250, 0))

    def player_hp(self):
        return self.health_points
