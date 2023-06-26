import pygame

import component.Block
import component.Box
import component.Explosion
import threading
import time


class Map:
    def __init__(self):
        self.set_of_block = pygame.sprite.Group()
        self.set_of_box = pygame.sprite.Group()
        self.set_of_bomb = pygame.sprite.Group()
        self.set_of_explosion = pygame.sprite.Group()

    def block_initialize(self, block_img, width, height):
        x, y = 30, 30
        while x < width:
            self.set_of_block.add(component.Block.Block(block_img, (x, y)))
            x += 60
        x = 30
        i = 0
        y += 60
        while y < height - 60:
            self.set_of_block.add(component.Block.Block(block_img, (x, y)))
            self.set_of_block.add(component.Block.Block(block_img, (width - x, y)))
            if i % 2:
                x += 60 * 2
                while x < width - 60:
                    self.set_of_block.add(component.Block.Block(block_img, (x, y)))
                    x += 60 * 2

                x = 30
            i += 1
            y += 60
        while x < width:
            self.set_of_block.add(component.Block.Block(block_img, (x, y)))
            x += 60

    def box_initialize(self, box_img, animation_hander_box):
        positions_list = [(210, 90), (330, 90), (510, 90), (570, 90), (690, 90),
                          (210, 150), (450, 150), (570, 150),
                          (150, 210), (270, 210), (330, 210), (450, 210), (630, 210),
                          (90, 270), (210, 270), (450, 270), (690, 270),
                          (90, 330), (270, 330), (330, 330), (510, 330), (570, 330), (690, 330),
                          (210, 390), (450, 390), (570, 390),
                          (150, 450), (210, 450), (330, 450), (450, 450), (630, 450), (690, 450),
                          (90, 510), (330, 510), (570, 510),
                          (90, 570), (210, 570), (390, 570), (510, 570), (570, 570)]
        for position in positions_list:
            self.set_of_box.add(component.Box.Box(box_img, position, animation_hander_box.copy()))

    def draw(self, surface):
        self.set_of_block.draw(surface)
        self.set_of_box.draw(surface)
        self.set_of_bomb.draw(surface)
        self.set_of_explosion.draw(surface)

    def add_bomb(self, bomb):
        if not pygame.sprite.spritecollide(bomb, self.set_of_bomb, False):
            self.set_of_bomb.add(bomb)
            return True
        else:
            return False

    def add_explosions(self, explosion_img, bomb_range, position):
        new_position = self._calculate_position_for_explosion(position)
        a, b = new_position
        step = 30
        self.set_of_explosion.add(component.Explosion.Explosion(explosion_img, new_position))
        a += step
        while a - new_position[0] < bomb_range:
            explosion = component.Explosion.Explosion(explosion_img, (a, new_position[1]))
            colide_box = pygame.sprite.spritecollide(explosion, self.set_of_box, False)
            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif len(colide_box) > 0:
                thred = threading.Thread(target=self._destruction_of_box, args=(colide_box[0],), daemon=True)
                thred.start()
                break
            else:
                self.set_of_explosion.add(explosion)
            a += step
        a = new_position[0] - step
        while a - new_position[0] > bomb_range * -1:
            explosion = component.Explosion.Explosion(explosion_img, (a, new_position[1]))
            colide_box = pygame.sprite.spritecollide(explosion, self.set_of_box, False)
            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif len(colide_box) > 0:
                thred = threading.Thread(target=self._destruction_of_box, args=(colide_box[0],), daemon=True)
                thred.start()
                break
            else:
                self.set_of_explosion.add(explosion)
            a -= step
        b += step
        while b - new_position[1] < bomb_range:
            explosion = component.Explosion.Explosion(explosion_img, (new_position[0], b))
            colide_box = pygame.sprite.spritecollide(explosion, self.set_of_box, False)

            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif len(colide_box) > 0:
                thred = threading.Thread(target=self._destruction_of_box, args=(colide_box[0],), daemon=True)
                thred.start()
                break
            else:
                self.set_of_explosion.add(explosion)
            b += step
        b = new_position[1] - step
        while b - new_position[1] > bomb_range * -1:
            explosion = component.Explosion.Explosion(explosion_img, (new_position[0], b))
            colide_box = pygame.sprite.spritecollide(explosion, self.set_of_box, False)

            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif len(colide_box) > 0:
                thred = threading.Thread(target=self._destruction_of_box, args=(colide_box[0],), daemon=True)
                thred.start()
                break
            else:
                self.set_of_explosion.add(explosion)
            b -= step

    def _destruction_of_box(self, box):
        for _ in range(0, box.animation_handler.get_len_of_animation(0) - 1):
            box.image = box.animation_handler.run(0)
            time.sleep(0.05)
        box.kill()

    def _calculate_position_for_explosion(self, position):
        x = (position[0] // 60) * 60 + 30
        y = (position[1] // 60) * 60 + 30
        return x, y
