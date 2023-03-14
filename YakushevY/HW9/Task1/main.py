import pygame
from constants import *
from func import *







pygame.display.set_caption('Game of chance')
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():                                                                
        if event.type == pygame.QUIT:                                                               
            done = True                                                                             
        if event.type == pygame.MOUSEBUTTONDOWN:
            if INPUT_FIELD.collidepoint(event.pos):                                                 
                input_field_active = not input_field_active
            else:
                input_field_active = False

            input_field_color = COLOR_ACTIVE if input_field_active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:                                                            
            if input_field_active:
                if event.key == pygame.K_RETURN:                                                    
                    result = RESULT_FONT.render(check_is_number(input_field_text, RANDOM_NUMBER, counter), True, TEXT_COLOR)
                    counter += 1                                                                    
                    input_field_text = ''
                elif event.key == pygame.K_BACKSPACE:                                               
                    input_field_text = input_field_text[:-1]
                else:                                                                               
                    input_field_text += event.unicode
                    if len(input_field_text) > 3:                                                   
                        input_field_text = input_field_text[:-1]

    

    gameDisplay.fill(DISPLAY_COLOR)
    gameDisplay.blit(GREETING_TEXT, [(800 - GREETING_TEXT.get_width()) / 2, 50])
    gameDisplay.blit(GAME_TEXT1, [(800 - GAME_TEXT1.get_width()) / 2, 100])
    gameDisplay.blit(GAME_TEXT2, [(800 - GAME_TEXT2.get_width()) / 2, 150])
    gameDisplay.blit(GAME_TEXT3, [(800 - GAME_TEXT3.get_width()) / 2, 200])

    ready_text = INPUT_FIELD_FONT.render(input_field_text, True, TEXT_COLOR)
    input_field_width = max(100, ready_text.get_width() + 10)
    INPUT_FIELD.w = input_field_width
    gameDisplay.blit(ready_text, (INPUT_FIELD.x + 5, INPUT_FIELD.y + 5))
    pygame.draw.rect(gameDisplay, input_field_color, INPUT_FIELD, 2)

    gameDisplay.blit(result, [(800 - result.get_width()) / 2, 300])

    pygame.display.update()

    clock.tick(60)