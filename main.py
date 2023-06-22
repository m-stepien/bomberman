import pygame
import controler.ImageControler
import component.Player
import component.AnimationHandler
import component.KeyboardControl
import component.Block
import component.Map
temp_tup = (60,60)
pygame.init()
SCREENSIZE = WIDTH, HEIGHT = 780, 660
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
image_controler = controler.ImageControler.ImageControler("resources/assets")
player1_control = component.KeyboardControl.KeyboardControl(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,
                                                         pygame.K_SLASH)
icon = image_controler.get_image('bomb_screen_icon')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
bg = image_controler.get_image('background')
player1IMG = image_controler.get_image('character1_walk_down_0', temp_tup)
player2_control = component.KeyboardControl.KeyboardControl(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s,
                                                            pygame.K_SPACE)
player2IMG = image_controler.get_image('character2_walk_down_0', temp_tup)
anime11 = image_controler.get_sequance_of_image_for_animation("character2_walk_down", temp_tup)
anime22 = image_controler.get_sequance_of_image_for_animation("character2_walk_up", temp_tup)
anime33 = image_controler.get_sequance_of_image_for_animation("character2_walk_left", temp_tup)
anime44 = image_controler.get_mirror_sequance_for_animation("character2_walk_left",temp_tup)

window_open = True
# do zmiany na szybko
anime1 = image_controler.get_sequance_of_image_for_animation("character1_walk_down", temp_tup)
anime2 = image_controler.get_sequance_of_image_for_animation("character1_walk_up", temp_tup)
anime3 = image_controler.get_sequance_of_image_for_animation("character1_walk_left", temp_tup)
anime4 = image_controler.get_mirror_sequance_for_animation("character1_walk_left", temp_tup)
animationHanderP1 = component.AnimationHandler.AnimationHandler([anime1, anime2, anime3, anime4])
animationHanderP2 = component.AnimationHandler.AnimationHandler([anime11, anime22, anime33, anime44])

player = component.Player.Player(3, 1, 5, 15, player1IMG, temp_tup, animationHanderP1, player1_control,
                                 False)
player2 = component.Player.Player(3, 1, 5, 15, player2IMG, (400, 300), animationHanderP2, player2_control,
                                  False)
blockIMG = image_controler.get_image("block", temp_tup)
block = component.Block.Block(blockIMG, (temp_tup[0]/2, temp_tup[1]/2))
map = component.Map.Map()
map.block_initialize(blockIMG)
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
    player2.update(keys_pressed)
    player.draw(screen)
    player2.draw(screen)
    block.draw(screen)
    map.draw(screen)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
