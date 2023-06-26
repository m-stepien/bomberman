import pygame
import controler.ImageControler
import component.Player
import component.AnimationHandler
import component.KeyboardControl
import component.Map
import component.Bomb
import component.Explosion
import component.Button
import component.HeartManager
import threading
import time
import os


def add_bomb_to_map(planting, player):
    bomb = component.Bomb.Bomb(bombIMG, planting[0], planting[1])
    if map.add_bomb(bomb):
        thred = threading.Thread(target=bomb_clock, args=(bomb, map, explosion_img), daemon=True)
        thred.start()
        player.increase_used_bomb()


def end_menu(event, winner):
    screen.blit(bg, (0, 0))
    state = 2
    font = pygame.font.Font(None, 30)
    text_surface = font.render("The winner is {}".format(winner), True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH / 2, 100),
    screen.blit(text_surface, text_rect)
    button_back = component.Button.Button(WIDTH / 2 - 75, 300, 150, 50, "BACK")
    button_quit = component.Button.Button(WIDTH / 2 - 75, 375, 150, 50, "END")
    button_back.handle_event(event)
    button_quit.handle_event(event)
    button_back.draw(screen)
    button_quit.draw(screen)
    if button_back.clicked:
        state = 0
    elif button_quit.clicked:
        state = -1
    return state


def game():
    global window_open

    while player.life > 0 and player2.life > 0:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        keys_pressed = pygame.key.get_pressed()
        player.update(keys_pressed, map.set_of_block, map.set_of_box, map.set_of_explosion)
        player2.update(keys_pressed, map.set_of_block, map.set_of_box, map.set_of_explosion)
        planting = player.planting_bomb_event(keys_pressed)
        planting2 = player2.planting_bomb_event(keys_pressed)
        heart_manager.update(player.life, player2.life)
        if planting:
            add_bomb_to_map(planting, player)

        if planting2:
            add_bomb_to_map(planting2, player2)
        map.draw(screen)
        player.draw(screen)
        player2.draw(screen)
        heart_manager.draw(screen)

        pygame.display.flip()
        clock.tick(30)
    if player.life > 0:
        return "Player1"
    else:
        return "Player2"


def main_menu(event):
    screen.blit(main_menu_img, (0, 0))
    state = 0
    button_start = component.Button.Button(WIDTH / 2 - 75, 300, 150, 50, "START")
    button_quit = component.Button.Button(WIDTH / 2 - 75, 375, 150, 50, "END")
    button_start.handle_event(event)
    button_quit.handle_event(event)
    button_start.draw(screen)
    button_quit.draw(screen)
    if button_start.clicked:
        state = 1
    elif button_quit.clicked:
        state = -1
    return state


def bomb_clock(bomb, map, explosionIMG, time_to_explode=1.5):
    bomb_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "resources/music/kabum.wav"))
    time.sleep(time_to_explode)
    bomb.owner.bomb_used -= 1
    position = bomb.rect.center
    range = bomb.range
    bomb_sound.play()
    map.add_explosions(explosionIMG, range, position)
    bomb.kill()


CHARACTER_SIZE = (50, 50)
BOX_SIZE = (60, 60)
SMALL_ELEMENT_SIZE = (30, 30)
PLAYER_SPEED = 5
BOMB_NUM = 3
LIFE = 3
BOMB_RANGE = 150
pygame.init()
SCREENSIZE = WIDTH, HEIGHT = 780, 660
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
image_controler = controler.ImageControler.ImageControler("resources/assets")
icon = image_controler.get_image('bomb_screen_icon')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bomberman')
bg = image_controler.get_image('background')

player1IMG = image_controler.get_image('character1_walk_down_0', CHARACTER_SIZE)
player2IMG = image_controler.get_image('character2_walk_down_0', CHARACTER_SIZE)
bombIMG = image_controler.get_image("game_bomb", SMALL_ELEMENT_SIZE)
explosion_img = image_controler.get_image("explosion", CHARACTER_SIZE)
main_menu_img = image_controler.get_image("main_menu_screen")
player1_control = component.KeyboardControl.KeyboardControl(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,
                                                            pygame.K_SLASH)
player2_control = component.KeyboardControl.KeyboardControl(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s,
                                                            pygame.K_SPACE)
anime1 = image_controler.get_sequance_of_image_for_animation("character1_walk_down", CHARACTER_SIZE)
anime2 = image_controler.get_sequance_of_image_for_animation("character1_walk_up", CHARACTER_SIZE)
anime3 = image_controler.get_sequance_of_image_for_animation("character1_walk_left", CHARACTER_SIZE)
anime4 = image_controler.get_mirror_sequance_for_animation("character1_walk_left", CHARACTER_SIZE)
anime5 = image_controler.get_sequance_of_image_for_animation("character_1_get_hit", CHARACTER_SIZE)

anime11 = image_controler.get_sequance_of_image_for_animation("character2_walk_down", CHARACTER_SIZE)
anime22 = image_controler.get_sequance_of_image_for_animation("character2_walk_up", CHARACTER_SIZE)
anime33 = image_controler.get_sequance_of_image_for_animation("character2_walk_left", CHARACTER_SIZE)
anime44 = image_controler.get_mirror_sequance_for_animation("character2_walk_left", CHARACTER_SIZE)
anime55 = image_controler.get_sequance_of_image_for_animation("character_2_get_hit", CHARACTER_SIZE)

anime_box = image_controler.get_sequance_of_image_for_animation("box", BOX_SIZE)
heart_img = image_controler.get_image("heart", SMALL_ELEMENT_SIZE)
box_img = image_controler.get_image("box1", BOX_SIZE)
animation_handler_p1 = component.AnimationHandler.AnimationHandler([anime1, anime2, anime3, anime4, anime5])
animation_handler_p2 = component.AnimationHandler.AnimationHandler([anime11, anime22, anime33, anime44, anime55])
animation_handler_box = component.AnimationHandler.AnimationHandler([anime_box])
blockIMG = image_controler.get_image("block", BOX_SIZE)

pygame.mixer.music.load(os.path.join(os.getcwd(), "resources/music/background_music.wav"))

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

window_open = True
state = 0
winner = None
while window_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

        elif state == 0:
            state = main_menu(event)

        elif state == -1:
            window_open = False
        elif state == 1:
            player = component.Player.Player(LIFE, BOMB_NUM, PLAYER_SPEED, BOMB_RANGE, player1IMG, (690, 570),
                                             animation_handler_p1,
                                             player1_control)
            player2 = component.Player.Player(LIFE, BOMB_NUM, PLAYER_SPEED, BOMB_RANGE, player2IMG, (90, 90),
                                              animation_handler_p2, player2_control)
            heart_manager = component.HeartManager.HeartManager(heart_img, (20, 20), 3, SCREENSIZE)
            map = component.Map.Map()
            map.block_initialize(blockIMG, WIDTH, HEIGHT)
            map.box_initialize(box_img, animation_handler_box)
            winner = game()

    if winner:
        state = end_menu(event, winner)
        if state != 2:
            winner = None

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
