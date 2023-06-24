import pygame
import time
import threading


class Explosion(pygame.sprite.Sprite):
    def __init__(self, image, position, time_of_exist=0.3):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.size = image.get_size()
        self.time_of_exist = time_of_exist
        thred = threading.Thread(target=self.destroy, daemon=True)
        thred.start()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def destroy(self):
        time.sleep(self.time_of_exist)
        self.kill()
