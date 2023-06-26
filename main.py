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


def game():
    while (player.life > 0 and player2.life > 0):
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
                thred = threading.Thread(target=bomb_clock, args=(bomb, map, explosion_img), daemon=True)
                thred.start()
                player.increase_used_bomb()
        planting2 = player2.planting_bomb_event(keys_pressed)
        if planting2:
            bomb = component.Bomb.Bomb(bombIMG, planting2[0], planting2[1])
            if map.add_bomb(bomb):
                thred = threading.Thread(target=bomb_clock, args=(bomb, map, explosion_img), daemon=True)
                thred.start()
                player2.increase_used_bomb()
        map.draw(screen)
        player.draw(screen)
        player2.draw(screen)
        pygame.display.flip()
        clock.tick(30)


def main_menu():
    menu_on = True
    while menu_on:
        screen.blit(bg, (0, 0))
        mouse_position = pygame.mouse.get_pos()
        title = pygame.get_font(100).render("BOMBERMAN", True, "#b58f40")
        title.getRect(center=(WIDTH, HEIGHT))


# for i in range(self.player.lives):
#     surface.blit(IMAGES['PLAYERLIFE'], [20 + 40 * i, 15])
def bomb_clock(bomb, map, explosionIMG, time_to_explode=1.5):
    time.sleep(time_to_explode)
    bomb.owner.bomb_used -= 1
    position = bomb.rect.center
    range = bomb.range
    map.add_explosions(explosionIMG, range, position)
    bomb.kill()


character_size = (50, 50)
box_size = (60, 60)
pygame.init()
SCREENSIZE = WIDTH, HEIGHT = 780, 660
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
image_controler = controler.ImageControler.ImageControler("resources/assets")
icon = image_controler.get_image('bomb_screen_icon')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
bg = image_controler.get_image('background')

player1IMG = image_controler.get_image('character1_walk_down_0', character_size)
player2IMG = image_controler.get_image('character2_walk_down_0', character_size)
bombIMG = image_controler.get_image("game_bomb", (30, 30))
explosion_img = image_controler.get_image("explosion", character_size)

player1_control = component.KeyboardControl.KeyboardControl(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,
                                                            pygame.K_SLASH)
player2_control = component.KeyboardControl.KeyboardControl(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s,
                                                            pygame.K_SPACE)
anime1 = image_controler.get_sequance_of_image_for_animation("character1_walk_down", character_size)
anime2 = image_controler.get_sequance_of_image_for_animation("character1_walk_up", character_size)
anime3 = image_controler.get_sequance_of_image_for_animation("character1_walk_left", character_size)
anime4 = image_controler.get_mirror_sequance_for_animation("character1_walk_left", character_size)

anime11 = image_controler.get_sequance_of_image_for_animation("character2_walk_down", character_size)
anime22 = image_controler.get_sequance_of_image_for_animation("character2_walk_up", character_size)
anime33 = image_controler.get_sequance_of_image_for_animation("character2_walk_left", character_size)
anime44 = image_controler.get_mirror_sequance_for_animation("character2_walk_left", character_size)

anime_box = image_controler.get_sequance_of_image_for_animation("box", box_size)

box_img = image_controler.get_image("box1", box_size)
animation_handler_p1 = component.AnimationHandler.AnimationHandler([anime1, anime2, anime3, anime4])
animation_handler_p2 = component.AnimationHandler.AnimationHandler([anime11, anime22, anime33, anime44])
animation_handler_box = component.AnimationHandler.AnimationHandler([anime_box])
player = component.Player.Player(3, 3, 5, 150, player1IMG, (690, 570), animation_handler_p1, player1_control)
player2 = component.Player.Player(3, 3, 5, 150, player2IMG, (90, 90), animation_handler_p2, player2_control)
blockIMG = image_controler.get_image("block", box_size)
map = component.Map.Map()
map.block_initialize(blockIMG)
map.box_initialize(box_img, animation_handler_box)

window_open = True
while window_open:
    # main_menu()
    game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

pygame.quit()
