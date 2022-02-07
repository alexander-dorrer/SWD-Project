import pygame


class Main:
    def __init__(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()





