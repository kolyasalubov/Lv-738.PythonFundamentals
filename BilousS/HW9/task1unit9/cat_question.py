 # Rules:
# The cat has a secret number in range 0-100
# You have to guess this number
# You have 10 attempts
# The cat will help you (you will see his clue in the purple rect in the left corner)
# Print your number (you will see it in the blue rect in the right corner) and
# press space-button to put it in program

import pygame
from random import randint, choice
pygame.init()

FPS = 60
clock = pygame.time.Clock()

W = 800
H = 600
speed = 5
cat_x = W//2
cat_y = H//2
alice_x =0
alice_y = 0
cat_number = randint(0, 100)
text = "Tell me a secret number, Alice"
PURPLE = (255, 0, 255)
AQUA = (0, 255, 255)
FONT = pygame.font.SysFont('arial', 12)
counter = 0

sc = pygame.display.set_mode((W, H))

pygame.display.set_caption('Guess the number, Alice')
pygame.display.set_icon(pygame.image.load("smiling_cat.png"))

cat_surf = pygame.image.load("cat_wonderland.png")
cat_rect = cat_surf.get_rect(center=(cat_x, cat_y))

alice_surf = pygame.Surface((300, 20))
number_surf = pygame.Surface((100, 20))

bg_surf = pygame.image.load("mashroom_forrest.jpg")
bg_rect = bg_surf.get_rect(center=(cat_x, cat_y))

a = pygame.draw
secret_number = ""

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(bg_surf, bg_rect)
    sc.blit(cat_surf, cat_rect)
    number_surf.fill(AQUA)
    sc.blit(number_surf, ((W-50), (H-20)))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        secret_number += "1"
        pygame.time.delay(200)
    elif keys[pygame.K_2]:
        secret_number += "2"
        pygame.time.delay(200)
    elif keys[pygame.K_3]:
        secret_number += "3"
        pygame.time.delay(200)
    elif keys[pygame.K_4]:
        secret_number += "4"
        pygame.time.delay(200)
    elif keys[pygame.K_5]:
        secret_number += "5"
        pygame.time.delay(200)
    elif keys[pygame.K_6]:
        secret_number += "6"
        pygame.time.delay(200)
    elif keys[pygame.K_7]:
        secret_number += "7"
        pygame.time.delay(200)
    elif keys[pygame.K_8]:
        secret_number += "8"
        pygame.time.delay(200)
    elif keys[pygame.K_9]:
        secret_number += "9"
        pygame.time.delay(200)
    elif keys[pygame.K_0]:
        secret_number += "0"
        pygame.time.delay(200)
    if keys[pygame.K_BACKSPACE]:
        secret_number = secret_number[0:(len(secret_number) - 1)]
        pygame.time.delay(200)
    elif keys[pygame.K_SPACE]:
        pygame.time.delay(200)
        counter += 1
        if counter >= 10:
            text = "You lost the time. Run!"
            cat_surf = pygame.image.load("cats2.com (7).png")
            cat_rect = cat_surf.get_rect(center=(cat_x, (cat_y+70)))
            sc.blit(cat_surf, cat_rect)
        else:
            if int(secret_number) > cat_number:
                text = f"Your number is too big, honey...Try again. {counter} "
            elif int(secret_number) < cat_number:
                text = f"Your number is too small, honey...Try again. {counter}"
            elif int(secret_number) == cat_number:
                text = "You are right! You are win!"
                cat_surf = pygame.image.load("black_cat_in_hat.png")
                cat_rect = cat_surf.get_rect(center=(cat_x, cat_y))
                sc.blit(cat_surf, cat_rect)

        secret_number = ""

    secret_text = FONT.render(secret_number, True, (0, 0, 0))
    post_secret = secret_text.get_rect(center=(50, 10))
    number_surf.blit(secret_text, post_secret)

    sc.blit(number_surf, ((W - 100), (H - 20)))
    alice_surf.fill(PURPLE)
    alice_text = FONT.render(text, True, (0, 0, 0))
    post = alice_text.get_rect(center=(95, 10))
    alice_surf.blit(alice_text, post)
    sc.blit(alice_surf, (alice_x, alice_y))

    pygame.display.update()
    clock.tick(FPS)
