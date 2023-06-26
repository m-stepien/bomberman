import pygame


class Button:
    BUTTON_COLOR = (200, 200, 200)
    BUTTON_HOVER_COLOR = (150, 150, 150)
    BUTTON_TEXT_COLOR = (0, 0, 0)
    BUTTON_TEXT_HOVER_COLOR = (255, 255, 255)
    FONT_SIZE = 24

    def __init__(self, x, y, width, height, text, on_click=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.on_click = on_click
        self.clicked = False
        self.hover = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
            self.hover = self.rect.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hover:
                self.clicked = True
                try:
                    self.on_click()
                except TypeError:
                    if not self.on_click:
                        pass
                    else:
                        raise TypeError()

    def draw(self, screen):
        if self.hover:
            button_color = Button.BUTTON_HOVER_COLOR
            text_color = Button.BUTTON_TEXT_HOVER_COLOR
        else:
            button_color = Button.BUTTON_COLOR
            text_color = Button.BUTTON_TEXT_COLOR

        pygame.draw.rect(screen, button_color, self.rect)
        font = pygame.font.Font(None, Button.FONT_SIZE)
        text_surface = font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)
