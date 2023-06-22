import pygame


class KeyboardControl:
    def __init__(self, move_left_bt, move_right_bt, move_up_bt, move_down_bt, set_bomb):
        try:
            self.LEFT = move_left_bt
            self.RIGHT = move_right_bt
            self.UP = move_up_bt
            self.DOWN = move_down_bt
            self.SET_BOMB = set_bomb
        except TypeError:
            print(TypeError)
            exit(-1)

    def _check_valid_type(self, bt):
        if not isinstance(bt, pygame.key.__class__):
            raise TypeError("Dopuszczalne tylko pygame.key.KeyType")
