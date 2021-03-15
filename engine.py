import pygame
import random
import time

pygame.init()
width, height = 400, 400
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Pong")

while True:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()


