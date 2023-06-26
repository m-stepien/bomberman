class AnimationHandler:
    def __init__(self, list_of_animations=[]):
        self._current_step = 0
        self._list_of_animation = list_of_animations
        self._latest_used_animation = 0

    def add_animation(self, animation):
        self._list_of_animation.append(animation)

    def run(self, animation_number):
        self._latest_used_animation = animation_number
        self._current_step = (self._current_step + 1) % ((len(self._list_of_animation[animation_number]) - 1) + 1)
        return self._list_of_animation[animation_number][self._current_step]

    def set_step_to_zero_state(self):
        self._current_step = 0
        return self._list_of_animation[self._latest_used_animation][0]

    def get_len_of_animation(self, num):
        return len(self._list_of_animation[num])

    def __copy__(self):
        return AnimationHandler(self._list_of_animation)

    def copy(self):
        return self.__copy__()
