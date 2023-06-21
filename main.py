import pygame

pygame.init()

SCREENSIZE = WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
icon = pygame.image.load('./assets/bomb_screen_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
window_open = True
while window_open:
    # pygame.display.flip()
    clock.tick(30)

pygame.quit()
