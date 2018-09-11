import pygame

class GOLButton:
    def __init__(self, rect, text, onclick_handler):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = (0, 200, 0)
        self.hover_color = (150, 255, 150)
        self.font = pygame.font.Font(None, 16)
        self.font_color = (0, 100, 0)
        self.on_click = onclick_handler

    def draw(self, surface):
        buttoncolor = self.hover_color if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color
        pygame.draw.rect(surface, buttoncolor, self.rect, 0)
        
        buttontext = self.font.render(self.text, True, self.font_color)
        surface.blit(buttontext, buttontext.get_rect(center=self.rect.center))

    def check_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            self.on_click()


if __name__ == "__main__":
    pass