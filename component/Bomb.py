import pygame.sprite


class Bomb(pygame.sprite.Sprite):
    def __init__(self, image, owner, position):
        self.image = image
        self.range = owner.bomb_range
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.size = image.get_size()
        pygame.sprite.Sprite.__init__(self)
    def kaboom(self, range):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
