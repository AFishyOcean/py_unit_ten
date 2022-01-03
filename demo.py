# These two lines should be at the top of all Pygame programs
import pygame, sys
from pygame.locals import *

import snowbeing

pygame.init() # usually first command
main_surface = pygame.display.set_mode((600, 400)) # sets window size
main_surface.fill((135, 206, 235))

snow = snowbeing.Snowbeing(main_surface)
snow.body()
snow.hat()

pygame.display.update() # must put in this command to see everything

# Standard starting while loop for Pygame programs.
# Much more can be added to this as needed.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
