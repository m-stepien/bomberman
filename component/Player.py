import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, live, defualt_bomb_num, defualt_speed, defualt_bomb_range, image, initial_position,
                 animation_handler, control, can_move_bomb=False):
        self.image = image
        self.position = initial_position
        self.live = live
        self.bomb_number = defualt_bomb_num
        self.speed = defualt_speed
        self.bomb_range = defualt_bomb_range
        self.can_move_bomb = can_move_bomb
        self.rect = self.image.get_rect()
        self.rect.center = initial_position[0], initial_position[1]
        self.animation_handler = animation_handler
        self.size = image.get_size()
        self.control = control
        super().__init__()

    def update(self, keys_pressed):
        self._handle_events(keys_pressed)
        pass

    def _handle_events(self, keys_pressed):
        if keys_pressed[self.control.LEFT]:
            self.rect.move_ip([-self.speed, 0])
            self.image = self.animation_handler.run(2)
        elif keys_pressed[self.control.RIGHT]:
            self.rect.move_ip([self.speed, 0])
            self.image = self.animation_handler.run(3)

        elif keys_pressed[self.control.DOWN]:
            self.rect.move_ip([0, self.speed])
            self.image = self.animation_handler.run(0)
        elif keys_pressed[self.control.UP]:
            self.rect.move_ip([0, -self.speed])
            self.image = self.animation_handler.run(1)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def plant_bom(self):
        # TODO decyzja w jaki sposób rozwiązywać kontrolę użytych bomb czy klasa powinna sama o to
        # TODO dbac czy odpowiedzilany powinien byc za to menagerbomb
        return self.position
