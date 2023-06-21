import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, live, defualt_bomb_num, defualt_speed, defualt_bomb_range, image, initial_position,
                 can_move_bomb=False):
        self.image = image
        self.position = initial_position
        self.live = live
        self.bomb_nubmer = defualt_bomb_num
        self.speed = defualt_speed
        self.bomb_range = defualt_bomb_range
        self.can_move_bomb = can_move_bomb
        pygame.sprite.Sprite.__init__()

    def plant_bom(self):
        # TODO decyzja w jaki sposób rozwiązywać kontrolę użytych bomb czy klasa powinna sama o to
        # TODO dbac czy odpowiedzilany powinien byc za to menagerbomb
        return self.position
