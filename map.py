import pygame

"""
0 = grass
1 = water
2 = sand
3 = spawn point
4 = enemy goal
"""


class Map:
    def __init__(self):
        self.level1 = [
            [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 4],
            [0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 2, 2, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
            [0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.level1_path = [[11, 0], [11, 1], [10, 1], [9, 1], [8, 1], [7, 1], [7, 2], [7, 3], [8, 3], [9, 4],
                            [9, 5], [9, 6], [8, 6], [7, 6], [6, 6], [5, 6], [4, 6], [3, 6], [3, 5], [3, 4],
                            [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                            [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [5, 10],
                            [5, 9], [5, 8], [6, 8], [7, 8], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13],
                            [8, 14], [8, 15], [8, 16], [8, 17], [7, 17], [6, 17], [5, 17], [4, 17], [4, 18], [4, 19]]

    def get_spawn_point(self, map):
        # returns spawnpoint as a list
        spawn_point = []
        current_row = -1
        for row in map:
            current_row += 1
            current_tile = 0
            for tile in row:
                if tile == 3:
                    spawn_point.append(current_tile * 60)
                    spawn_point.append(current_row * 60)
        return spawn_point

    def draw_map(self, map, window):
        grass_tile = pygame.image.load("Assets/grass_tile.png")
        sand_tile = pygame.image.load("Assets/sand_tile.png")
        water_tile = pygame.image.load("Assets/water_tile.png")
        enemy_goal = pygame.image.load('Assets/Towers&Projectiles/Tower_12/Tower_12.png')
        current_row = -1
        for row in map:
            current_row += 1
            current_tile = 0
            for tile in row:
                if tile == 0:
                    window.blit(pygame.transform.scale(grass_tile, (60, 60)), (current_tile * 60, current_row * 60))
                    current_tile += 1
                elif tile == 1:
                    window.blit(pygame.transform.scale(water_tile, (60, 60)), (current_tile * 60, current_row * 60))
                    current_tile += 1
                elif tile == 4:
                    window.blit(pygame.transform.scale(sand_tile, (60, 70)), (current_tile * 60, current_row * 60))
                    window.blit(pygame.transform.scale(enemy_goal, (55, 55)), (current_tile * 60, current_row * 60))
                else:
                    window.blit(pygame.transform.scale(sand_tile, (60, 60)), (current_tile * 60, current_row * 60))
                    current_tile += 1
