import pygame
from random import randint

pygame.init()
DISPLAY_COLOR = (127, 219, 116)
TEXT_COLOR = (7, 11, 247)
GREETING_FONT = pygame.font.SysFont('Calibri', 40, True, False)
RESULT_FONT = pygame.font.SysFont('Calibri', 20, True, False)

GREETING_TEXT = GREETING_FONT.render("Lets play the game", True, TEXT_COLOR)
GAME_RULE_TEXT1 = GREETING_FONT.render("I will generate natureal number from 1 to 10", True, TEXT_COLOR)
GAME_RULE_TEXT2 = GREETING_FONT.render("You have only 10 tries to check if you are right", True, TEXT_COLOR)
GAME_RULE_TEXT3 = GREETING_FONT.render("Enter your number and press Enter", True, TEXT_COLOR)

RANDOM_NUMBER = randint(1, 100)                                                 # random number

# input field CONSTANTS

INPUT_FIELD_FONT = pygame.font.Font(None, 30)                                      
INPUT_FIELD = pygame.Rect(150, 250, 140, 38)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

# input field variables

counter = 0                                                                     # how many times user tryes to check the number
gameDisplay = pygame.display.set_mode((800, 600))                               # Create the screen
done = False                                                                    # Loop until the user clicks the close button.
input_field_color = COLOR_INACTIVE                                              # input field color in realtime
input_field_active = False                                                      # input_field_active status
input_field_text = ''                                                           # input_field_text when field is empty
text_to_check = ''                                                              # text, which will be checked by function check_is_number
result = RESULT_FONT.render('', True, TEXT_COLOR)                               # result of Function check_is_number       