import component.Block


class Box(component.Block.Block):
    def __init__(self, image, position, animation_handler, bonus=None):
        self.animation_handler = animation_handler
        self.bonus = bonus
        component.Block.Block.__init__(self, image, position)
