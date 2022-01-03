import pygame

class Snowbeing:

    def __init__(self, surface):
        self.mainsurface = surface

    def body(self):
        pygame.draw.circle(self.mainsurface, (255, 255, 255), (300, 320), 80)
        pygame.draw.circle(self.mainsurface, (255, 255, 255), (300, 200), 60)
        pygame.draw.circle(self.mainsurface, (255, 255, 255), (300, 110), 40)

    def hat(self):
        pygame.draw.rect(self.mainsurface, (0, 0, 0), (270, 5, 60, 60))
        pygame.draw.rect(self.mainsurface, (255, 0, 0), (250, 60, 100, 20))