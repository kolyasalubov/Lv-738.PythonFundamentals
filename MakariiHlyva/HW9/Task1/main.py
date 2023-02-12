import pygame
from variables_and_constants import *
from functions import *


pygame.display.set_caption('Guess the number')

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------

while not done:

    # --- Main event loop

    for event in pygame.event.get():                                                                # User did something
        if event.type == pygame.QUIT:                                                               # If user clicked close
            done = True                                                                             # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if INPUT_FIELD.collidepoint(event.pos):                                                 # if user clecked on the input_field rect
                input_field_active = not input_field_active
            else:
                input_field_active = False

            input_field_color = COLOR_ACTIVE if input_field_active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:                                                            # if user pushings any buttons on keyboard
            if input_field_active:
                if event.key == pygame.K_RETURN:                                                    # if user have finished with writing input number
                    result = RESULT_FONT.render(check_is_number(input_field_text, RANDOM_NUMBER, counter), True, TEXT_COLOR)
                    counter += 1                                                                    # how many tries user did
                    input_field_text = ''
                elif event.key == pygame.K_BACKSPACE:                                               # if user deleting something
                    input_field_text = input_field_text[:-1]
                else:                                                                               # adding symbols to string
                    input_field_text += event.unicode
                    if len(input_field_text) > 3:                                                   # if user  add more then 3 symbols
                        input_field_text = input_field_text[:-1]

    # Greeting part

    gameDisplay.fill(DISPLAY_COLOR)
    gameDisplay.blit(GREETING_TEXT, [(800 - GREETING_TEXT.get_width()) / 2, 50])
    gameDisplay.blit(GAME_RULE_TEXT1, [(800 - GAME_RULE_TEXT1.get_width()) / 2, 100])
    gameDisplay.blit(GAME_RULE_TEXT2, [(800 - GAME_RULE_TEXT2.get_width()) / 2, 150])
    gameDisplay.blit(GAME_RULE_TEXT3, [(800 - GAME_RULE_TEXT3.get_width()) / 2, 200])

    #input field part

    ready_text = INPUT_FIELD_FONT.render(input_field_text, True, TEXT_COLOR)
    input_field_width = max(100, ready_text.get_width() + 10)
    INPUT_FIELD.w = input_field_width
    gameDisplay.blit(ready_text, (INPUT_FIELD.x + 5, INPUT_FIELD.y + 5))
    pygame.draw.rect(gameDisplay, input_field_color, INPUT_FIELD, 2)

    # printing result of function check_is_number

    gameDisplay.blit(result, [(800 - result.get_width()) / 2, 300])

    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.update()

    # --- Limit to 60 frames per second

    clock.tick(60)