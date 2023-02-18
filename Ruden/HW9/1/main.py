import pygame
import random


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Number Guessing Game')

font = pygame.font.Font(None, 30)

number_to_guess = random.randint(1, 100)
attempts_left = 10
guess = None
input_box = pygame.Rect(100, 70, 200, 50)
input_text = ''

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() and len(input_text) < 2:
                input_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_text:
                    guess = int(input_text)
                    input_text = ''
                    attempts_left -= 1

    window.fill(WHITE)
   
    pygame.draw.rect(window, BLACK, input_box, 2)
    input_surface = font.render(input_text, True, BLACK)
    window.blit(input_surface, (input_box.x + 5, input_box.y + 5))
    
    if guess is None:
        start_surface = font.render('Press Enter to start', True, BLACK)
        window.blit(start_surface, (100, 30))

    else:
        guesses_surface = font.render(f'Attempts left: {attempts_left}', True, BLACK)
        window.blit(guesses_surface, (50, 30))        
        if guess == number_to_guess:
            message_surface = font.render('You guessed the number!', True, BLACK)
            window.blit(message_surface, (10, 130))
            pygame.draw.rect(window, WHITE, input_box)
            pygame.event.set_blocked(pygame.KEYDOWN)
            pygame.event.set_blocked(pygame.KEYUP)          
              
            
        
        elif attempts_left == 0:
            message_surface = font.render(f'Sorry, you did not guess the number. The number was {number_to_guess}.', True, BLACK)
            window.blit(message_surface, (10, 130))
            pygame.draw.rect(window, WHITE, input_box)
            pygame.event.set_blocked(pygame.KEYDOWN)
            pygame.event.set_blocked(pygame.KEYUP)
            

        else:
            hint = 'lower' if guess > number_to_guess else 'higher'
            hint_surface = font.render(f'Wrong! Try a {hint} number.', True, BLACK)
            window.blit(hint_surface, (10, 130))

    
    pygame.display.update()

