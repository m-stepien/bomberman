import pygame
import controler.ImageControler
pygame.init()

SCREENSIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
image_controler = controler.ImageControler.ImageControler("assets")

icon = image_controler.get_image('bomb_screen_icon')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
bg = image_controler.get_image('background')
window_open = True
while window_open:
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
