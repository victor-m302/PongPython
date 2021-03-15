import pygame
import random
import time
'''
INICIALIZA PYGAMES
'''
pygame.init() 

#DEFINE ALTURA, LAGURA
width, height = 400, 400
game_screen = pygame.display.set_mode((width, height))
#CRIA O TÍTULO DA JANELA
pygame.display.set_caption("Game Pong")

#LOOP PRINCIPAL
while True:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT): #SAI DO JOGO SE CLICAR NO X DE FECHAR
            pygame.quit()
            quit()


