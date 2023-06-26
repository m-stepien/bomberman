import os
import pygame


class ImageControler:
    def __init__(self, image_folder_name):
        self.path = os.path.join(os.getcwd(), image_folder_name)
        self.images = {}
        self._create_image_dic()

    def _create_image_dic(self):
        names = sorted(os.listdir(self.path))
        self.images['BACKGROUND'] = pygame.image.load(os.path.join(self.path, 'background.png')).convert()
        names.remove('background.png')
        for name in names:
            image_name = name[:-4].upper()
            self.images[image_name] = pygame.image.load(os.path.join(self.path, name)).convert_alpha(
                self.images['BACKGROUND'])

    def get_image(self, image_name, size=None):
        try:
            image_to_return = self.images[image_name.upper()]
            if size:
                image_to_return = pygame.transform.scale(image_to_return, size)
            return image_to_return
        except Exception:
            exit(-1)

    def get_sequance_of_image_for_animation(self, sequance_name, size=None):
        animation = []
        sequance_name = sequance_name.upper()
        name_list = list(self.images.keys())
        name_list.sort()
        for key in name_list:
            if sequance_name.upper() in key:
                if size:
                    anime = pygame.transform.scale(self.images[key], size)
                else:
                    anime = self.images[key]
                animation.append(anime)

        return animation

    def get_mirror_sequance_for_animation(self, sequance_name, size=None):
        base_animation = self.get_sequance_of_image_for_animation(sequance_name, size)
        mirror_animation = []
        for surface in base_animation:
            mirror_animation.append(pygame.transform.flip(surface, True, False))

        return mirror_animation
