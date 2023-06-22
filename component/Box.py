import pygame.sprite


class Box(pygame.sprite.Sprite):
    def __init__(self, image, position):
        self.image = image
        self.position = position
        pygame.sprite.Sprite.__init__()

