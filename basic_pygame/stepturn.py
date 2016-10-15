import pygame, sys, random
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 4  # number of columns in the board
BOARDHEIGHT = 4 # number of rows in the board
TILESIZE = 80
WINWIDTH = 800 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
FPS = 30
BLANK = None

#              R    G    B
GRAY       = (100, 100, 100)
NAVYBLUE   = ( 60,  60, 100)
WHITE      = (255, 255, 255)
RED        = (255,   0,   0)
GREEN      = (  0, 255,   0)
BLUE       = (  0,   0, 255)
BRIGHTBLUE = (  0, 170, 255)
YELLOW     = (255, 255,   0)
ORANGE     = (255, 128,   0)
PURPLE     = (255,   0, 255)
CYAN       = (  0, 255, 255)


BGCOLOR = NAVYBLUE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
# BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Step and Turn')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    IMAGESDICT = {'title': pygame.image.load('star_pusher/star_title.png')}

    startScreen()

    direction = 'right'
    catImg = pygame.image.load('cat.png')
    catx = 10
    caty = 10
    BGCOLORLOOP = (GRAY, NAVYBLUE, WHITE, RED, GREEN, BLUE, BRIGHTBLUE, YELLOW, ORANGE, PURPLE, CYAN)
    NUMOFBGCOLOR = len(BGCOLORLOOP)
    count = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    count = count + 1
                    if count >= NUMOFBGCOLOR:
                        count = 0

        DISPLAYSURF.fill(BGCOLORLOOP[count])

        if direction == 'right':
            catx += 5
            if catx == 280:
                direction = 'down'
        elif direction == 'down':
            caty += 5
            if caty == 220:
                direction = 'left'
        elif direction == 'left':
            catx -= 5
            if catx == 10:
                direction = 'up'
        elif direction == 'up':
            caty -= 5
            if caty == 10:
                direction = 'right'

        DISPLAYSURF.blit(catImg, (catx, caty))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def startScreen():
    """Display the start screen (which has the title and instructions)
    until the player presses a key. Returns None."""

    # Position the title image.
    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = 50 # topCoord tracks where to position the top of the text
    titleRect.top = topCoord
    titleRect.centerx = HALF_WINWIDTH
    topCoord += titleRect.height

    # Unfortunately, Pygame's font & text system only shows one line at
    # a time, so we can't use strings with \n newline characters in them.
    # So we will use a list with each line in it.
    instructionText = ['Push the stars over the marks.',
                       'Arrow keys to move, WASD for camera control, P to change character.',
                       'Backspace to reset level, Esc to quit.',
                       'N for next level, B to go back a level.']

    # Start with drawing a blank color to the entire window:
    DISPLAYSURF.fill(BGCOLOR)

    # Draw the title image to the window:
    DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)

    # Position and draw the text.
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10 # 10 pixels will go in between each line of text.
        instRect.top = topCoord
        instRect.centerx = HALF_WINWIDTH
        topCoord += instRect.height # Adjust for the height of the line.
        DISPLAYSURF.blit(instSurf, instRect)

    while True: # Main loop for the start screen.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return # user has pressed a key, so return.

        # Display the DISPLAYSURF contents to the actual screen.
        pygame.display.update()
        FPSCLOCK.tick()


if __name__ == '__main__':
    main()