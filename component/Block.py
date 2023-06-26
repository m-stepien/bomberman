import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.size = image.get_size()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
