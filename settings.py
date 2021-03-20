import pygame
import sys
import random

# esse arquivo responsável por definir as variaveis globais
# que serão utilizadas entre arquivos

# é utilizado para impedir lag de audio
pygame.mixer.pre_init(44100, -16, 2, 512)
# inicializa o pygame
pygame.init()
clock = pygame.time.Clock()

# define algumas cores que serão utilizadas
bg_color = pygame.Color("#0D0A0B")
accent_color = pygame.Color("#E2FCEF")

# cria fonte para score
font = pygame.font.Font("fonts/RetroGaming.ttf", 32)

# define a altura e largura da janela
screen_width, screen_height = 1024, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# define o titulo da janela
pygame.display.set_caption("Pong")



bg_color_mult = pygame.Color("#8b1851")  # bg color
bg_color = pygame.Color("#29398e")  # bg color
accent_color = (253, 255, 252)  # cor das letras e linha no meio
basic_font = pygame.font.Font("fonts/RetroGaming.ttf", 32)  # carrega a fonte

hit_sound = pygame.mixer.Sound("sounds/pong.wav")  
score_sound = pygame.mixer.Sound("sounds/score.wav")  
destroy_sound = pygame.mixer.Sound("sounds/destroy.wav")  
button_sound = pygame.mixer.Sound("sounds/button.wav") 


menu_sound = pygame.mixer.Sound("sounds/flight.mp3") 
singleP_sound = pygame.mixer.Sound("sounds/make_a_run.mp3") 
multiP_sound = pygame.mixer.Sound("sounds/as_midnight.mp3")


# cria uma linha para ser desenhada no meio da tela
middle_strip = pygame.Rect(screen_width/2 - 2, 0, 4, screen_height) 