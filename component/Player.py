import pygame.sprite
import time
import threading


class Player(pygame.sprite.Sprite):
    def __init__(self, life, defualt_bomb_num, defualt_speed, defualt_bomb_range, image, initial_position,
                 animation_handler, control):
        self.image = image
        self.life = life
        self.bomb_number = defualt_bomb_num
        self.speed = defualt_speed
        self.bomb_range = defualt_bomb_range
        self.rect = self.image.get_rect()
        self.rect.center = initial_position[0], initial_position[1]
        self.animation_handler = animation_handler
        self.size = image.get_size()
        self.control = control
        self.bomb_used = 0
        self.move_unblock = True
        super().__init__()

    def update(self, keys_pressed, block_group, box_group, explosion_group):
        self._handle_movement_events(keys_pressed, block_group, box_group)
        self.life_update(explosion_group)

    def _handle_movement_events(self, keys_pressed, block_group, box_group):
        movement = None
        if self.move_unblock:
            if keys_pressed[self.control.LEFT]:
                movement = [-self.speed, 0]
                self.image = self.animation_handler.run(2)
            elif keys_pressed[self.control.RIGHT]:
                movement = [self.speed, 0]
                self.image = self.animation_handler.run(3)

            elif keys_pressed[self.control.DOWN]:
                movement = [0, self.speed]
                self.image = self.animation_handler.run(0)
            elif keys_pressed[self.control.UP]:
                movement = [0, -self.speed]
                self.image = self.animation_handler.run(1)
        if movement:
            self.rect.move_ip(movement)
            self.colide(block_group, box_group, movement)

    def planting_bomb_event(self, keys_pressed):
        if keys_pressed[self.control.SET_BOMB] and self.bomb_number - self.bomb_used > 0:
            return self, self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def increase_used_bomb(self):
        self.bomb_used += 1

    def colide(self, block_group, box_group, movement):
        block_colide_list_sprite = pygame.sprite.spritecollide(self, block_group, False)
        if block_colide_list_sprite \
                or pygame.sprite.spritecollide(self, box_group, False):
            self.rect.move_ip([-movement[0], -movement[1]])

    def life_update(self, explosion_g):
        if pygame.sprite.spritecollide(self, explosion_g, True):
            self.life -= 1
            self.move_unblock = False
            threading_get_hit = threading.Thread(target=self._get_hit_animation_run, daemon=True)
            threading_get_hit.start()

    def _get_hit_animation_run(self):
        n = 4
        img_at_start = self.image
        for _ in range(0, self.animation_handler.get_len_of_animation(n)):
            self.image = self.animation_handler.run(n)
            time.sleep(0.06)
        self.move_unblock = True
        self.image = img_at_start
