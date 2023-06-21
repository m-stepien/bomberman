import os
import pygame


class ImageControler(pygame.image):
    def __init__(self, image_folder_name):
        self.path = os.path.join(os.getcwd(), image_folder_name)
        self.images = {}
        self._create_image_dic()

    def _create_image_dic(self):
        names = sorted(os.listdir(self.path))
        self.images['BACKGROUND'] = self.load(os.path.join(self.path, 'background.jpg')).convert()
        names.remove('background.jpg')
        for name in names:
            image_name = name[:-4].upper()
            self.images[image_name] = self.load(os.path.join(self.path, name)).convert_alpha(self.images['BACKGROUND'])

    def get_image(self, image_name):
        try:
            image_to_return = self.images[image_name.upper()]
        except Exception:
            print(Exception)
            # TODO dorób obsługę wyjątków
            return -1
        return image_to_return
