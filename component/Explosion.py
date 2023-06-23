import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self,image, position):
        pygame.sprite.Sprite.__init__()

        self.position=position