import pygame
import controler.ImageControler
import component.Player
pygame.init()

SCREENSIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
image_controler = controler.ImageControler.ImageControler("resources/assets")

icon = image_controler.get_image('bomb_screen_icon')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
bg = image_controler.get_image('background')
playerIMG = image_controler.get_image('character1_walk_down_0')
# player = component.Player.Player(3, 1, 5, 15, playerIMG, (WIDTH // 2, HEIGHT // 2),
#                  False)
window_open = True
while window_open:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

    keys_pressed = pygame.key.get_pressed()
    pygame.display.flip()
    clock.tick(30)
    # player.draw(screen)
pygame.quit()
