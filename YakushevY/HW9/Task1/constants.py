import pygame
from random import randint

pygame.init()
DISPLAY_COLOR = (127, 219, 1)
TEXT_COLOR = (0,0,0)
GREETING_FONT = pygame.font.SysFont('Calibri', 30, True, False)
RESULT_FONT = pygame.font.SysFont('Calibri', 25, True, False)

GREETING_TEXT = GREETING_FONT.render("Lets play the game", True, TEXT_COLOR)
GAME_TEXT1 = GREETING_FONT.render("I will generate natureal number from 1 to 100", True, TEXT_COLOR)
GAME_TEXT2 = GREETING_FONT.render("You have 10 attempts to test your luck", True, TEXT_COLOR)
GAME_TEXT3 = GREETING_FONT.render("Enter your number and press Enter", True, TEXT_COLOR)

RANDOM_NUMBER = randint(1, 100)                                                


INPUT_FIELD_FONT = pygame.font.Font(None, 30)                                      
INPUT_FIELD = pygame.Rect(150, 250, 140, 38)
COLOR_INACTIVE = pygame.Color('red')
COLOR_ACTIVE = pygame.Color('green2')

counter = 0                                                                     
gameDisplay = pygame.display.set_mode((800, 600),pygame.RESIZABLE)                               
done = False                                                                    
input_field_color = COLOR_INACTIVE                                              
input_field_active = False                                                      
input_field_text = ''                                                           
text_to_check = ''                                                              
result = RESULT_FONT.render('', True, TEXT_COLOR)    