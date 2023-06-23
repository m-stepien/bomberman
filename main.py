import pygame
import controler.ImageControler
import component.Player
import component.AnimationHandler
import component.KeyboardControl
import component.Map
import component.Bomb
import component.Explosion
import threading
import time


def bomb_clock(bomb, map, explosionIMG, time_to_explode=3):
    time.sleep(time_to_explode)
    bomb.owner.bomb_used -= 1
    position = bomb.rect.center
    range = bomb.range
    map.add_explosions(explosionIMG, range, position)
    bomb.kill()


temp_tup = (60, 60)
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
temp_tup2 = (50, 50)
player1IMG = image_controler.get_image('character1_walk_down_0', temp_tup2)
player2_control = component.KeyboardControl.KeyboardControl(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s,
                                                            pygame.K_SPACE)
player2IMG = image_controler.get_image('character2_walk_down_0', temp_tup2)
anime11 = image_controler.get_sequance_of_image_for_animation("character2_walk_down", temp_tup2)
anime22 = image_controler.get_sequance_of_image_for_animation("character2_walk_up", temp_tup2)
anime33 = image_controler.get_sequance_of_image_for_animation("character2_walk_left", temp_tup2)
anime44 = image_controler.get_mirror_sequance_for_animation("character2_walk_left", temp_tup2)

window_open = True
anime1 = image_controler.get_sequance_of_image_for_animation("character1_walk_down", temp_tup2)
anime2 = image_controler.get_sequance_of_image_for_animation("character1_walk_up", temp_tup2)
anime3 = image_controler.get_sequance_of_image_for_animation("character1_walk_left", temp_tup2)
anime4 = image_controler.get_mirror_sequance_for_animation("character1_walk_left", temp_tup2)
anime_box = image_controler.get_sequance_of_image_for_animation("box", temp_tup)
boxIMG = image_controler.get_image("box1", (70, 70))
animationHanderP1 = component.AnimationHandler.AnimationHandler([anime1, anime2, anime3, anime4])
animationHanderP2 = component.AnimationHandler.AnimationHandler([anime11, anime22, anime33, anime44])
animationHandler = component.AnimationHandler.AnimationHandler(anime_box)
player = component.Player.Player(3, 3, 5, 150, player1IMG, (90, 90), animationHanderP1, player1_control)
player2 = component.Player.Player(3, 3, 5, 150, player2IMG, (690, 570), animationHanderP2, player2_control)
blockIMG = image_controler.get_image("block", temp_tup)
map = component.Map.Map()
map.block_initialize(blockIMG)
map.box_initialize(boxIMG, animationHandler)
bombIMG = image_controler.get_image("game_bomb", (30, 30))

explosionIMG = image_controler.get_image("explosion", (50, 50))
while window_open and (player.life > 0 and player2.life > 0):
    print(player.life)
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed, map.set_of_block, map.set_of_box, map.set_of_explosion)
    player2.update(keys_pressed, map.set_of_block, map.set_of_box, map.set_of_explosion)
    planting = player.planting_bomb_event(keys_pressed)
    if planting:
        bomb = component.Bomb.Bomb(bombIMG, planting[0], planting[1])
        if map.add_bomb(bomb):
            thred = threading.Thread(target=bomb_clock, args=(bomb, map, explosionIMG), daemon=True)
            thred.start()

    planting2 = player2.planting_bomb_event(keys_pressed)
    if planting2:
        bomb = component.Bomb.Bomb(bombIMG, planting2[0], planting2[1])
        if map.add_bomb(bomb):
            thred = threading.Thread(target=bomb_clock, args=(bomb, map, explosionIMG), daemon=True)
            thred.start()
    player.draw(screen)
    player2.draw(screen)
    map.draw(screen)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
