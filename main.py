import pygame
import controler.ImageControler
import component.Player
import component.AnimationHandler

pygame.init()
SCREENSIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
image_controler = controler.ImageControler.ImageControler("resources/assets")

icon = image_controler.get_image('bomb_screen_icon')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
bg = image_controler.get_image('background')
playerIMG = image_controler.get_image('character1_walk_down_0', (75, 75))
player = component.Player.Player(3, 1, 5, 15, playerIMG, (70, 70),
                                 False)
window_open = True
# do zmiany na szybko
anime1 = image_controler.get_sequance_of_image_for_animation("character1_walk_down", (75, 75))
anime2 = image_controler.get_sequance_of_image_for_animation("character1_walk_up", (75, 75))
anime3 = image_controler.get_sequance_of_image_for_animation("character1_walk_left", (75, 75))
anime4 = image_controler.get_mirror_sequance_for_animation("character1_walk_left", (75, 75))
animationHanderP1 = component.AnimationHandler.AnimationHandler([anime1, anime2, anime3, anime4])
player = component.Player.Player(3, 1, 5, 15, playerIMG, (70, 70), animationHanderP1,
                                 False)
while window_open:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)
    player.draw(screen)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
