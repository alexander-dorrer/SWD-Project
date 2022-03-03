class Player:
    """Player Class"""
    def __init__(self):
        pass

    def build_tower(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            Tower.position = pygame.mouse.get_pos()
