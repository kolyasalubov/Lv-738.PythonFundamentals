import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

WHITE_COLOR = (255, 255, 255)
ORANGE_COLOR = (255, 150, 100)
BLACK_COLOR = (0, 0, 0)

COORD_X = 50
COORD_Y = 50
WIDTH_RECT = 40
HEIGHT_RECT = 60
DELTA_STEP = 5

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True

clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < 450:
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > DELTA_STEP:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < 425:
        COORD_Y = COORD_Y + DELTA_STEP

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, (255, 0, 0), [COORD_X, COORD_Y, WIDTH_RECT, HEIGHT_RECT])

    pygame.display.update()


    clock.tick(FPS)

#Спершу написав таким чином:
#    if keys[pygame.K_LEFT]:
#        if COORD_X <= 0:
#            pass
#        else:
#            COORD_X = COORD_X - DELTA_STEP
#    if keys[pygame.K_RIGHT]:
#        if COORD_X > 450:
#            pass
#        else:
#            COORD_X = COORD_X + DELTA_STEP
#    if keys[pygame.K_UP]:
#        if COORD_Y <= 0:
#            pass
#        else:
#            COORD_Y = COORD_Y - DELTA_STEP
#    if keys[pygame.K_DOWN]:
#        if COORD_Y > 400:
#            pass
#        else:
#            COORD_Y = COORD_Y + DELTA_STEP


