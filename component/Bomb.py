import pygame.sprite
import pygame.mixer


class Bomb(pygame.sprite.Sprite):

    def __init__(self, image, owner, position):
        self.image = image
        self.owner = owner
        self.range = owner.bomb_range
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.size = image.get_size()
        pygame.sprite.Sprite.__init__(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
