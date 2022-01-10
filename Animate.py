# These two lines should be at the top of all Pygame programs
import pygame, sys
from pygame.locals import *

import Bounce

pygame.init() # usually first command
main_surface = pygame.display.set_mode((400, 600))
main_surface.fill((255, 255, 255))
b = Bounce.Bounce(main_surface)


# Standard starting while loop for Pygame programs.
# Much more can be added to this as needed.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main_surface.fill((255, 255, 255))
    b.move()
    main_surface.blit(b.image, b.rect)
    pygame.display.update()  # must put in this command to see everything