import pygame, sys
from pygame.locals import *

# Always call pygame.init() after import
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            # Call pygame.quit() before sys.exit()
            pygame.quit()
            sys.exit()
    pygame.display.update()