import pygame
import time
import random
import sys
import settings
import singleplayer
import multiplayer
import instructions


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
purple = (105,94,147)
bright_purple = (162,151,195)
block_color = (53,115,255)
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Titulo')
clock = pygame.time.Clock()


bgImg = pygame.image.load('images/bg.jpg')

bgImg2 = pygame.image.load('images/instructions.png')

keys1 = pygame.image.load('images/player1.png')
keys2 = pygame.image.load('images/player2.png')
 
def bgImage(x,y,scaleX,scaleY):
    bgScaled = pygame.transform.scale(bgImg, (scaleX, scaleY))
    gameDisplay.blit(bgScaled,(x,y))

def keysA(x,y):
    #bgScaled = pygame.transform.scale(bgImg, (scaleX, scaleY))
    gameDisplay.blit(keys1,(x,y))

def keysB(x,y):
    #bgScaled = pygame.transform.scale(bgImg, (scaleX, scaleY))
    gameDisplay.blit(keys2,(x,y)) 


def car(x,y):
    gameDisplay.blit(carImg,(x,y))
 
def bgImage2(x,y,scaleX,scaleY):
    bgScaled = pygame.transform.scale(bgImg2, (scaleX, scaleY))
    gameDisplay.blit(bgScaled,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
 

def text_objects1(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
 
def crash():
    message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
            return True       
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("fonts/RetroGaming.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    pygame.mixer.Sound.play(settings.menu_sound)
    intro = True
    a = 2110
    b = 600
    x = 0
    y = 0
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        bgImage(x, y, a, b)
        if(x<=-1000):
            x=0
        else:
            x-=2
        #print(x)
        
        largeText = pygame.font.Font("fonts/VampireWars.ttf", 50)
        TextSurf, TextRect = text_objects("Pong - Century Edition", largeText)
        TextRect.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf, TextRect)

        button("Single Player",275,170,250,60,purple,bright_purple,single_player)
        
        button("Multiplayer",275,250,250,60,purple,bright_purple,multi_player)

        button("Neko Player",275,330,250,60,purple,bright_purple,nekoPlayer)

        button("Instru????es",275,410,250,60,purple,bright_purple,instrucao)

        button("SAIR",275,490,250,60,purple,bright_purple,quitgame)

        pygame.display.update()
        clock.tick(15)




def single_player():
    pygame.mixer.Sound.stop(settings.menu_sound)
    pygame.mixer.Sound.play(settings.singleP_sound)
    gameDisplay = pygame.display.set_mode((1024,display_height))
    singleplayer.start_game()

def multi_player():
    pygame.mixer.Sound.stop(settings.menu_sound)
    pygame.mixer.Sound.play(settings.multiP_sound)
    gameDisplay = pygame.display.set_mode((1024,display_height))
    multiplayer.start_game()

def nekoPlayer():
    crash()

def instrucao():
    loop = True
    a = 800
    b = 600
    x = 0
    y = 0
    while loop:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                print("permit")
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        bgImage2(x, y, a, b)
        keysA(120, 250)
        keysB(500, 250)
        #print(x)

        largeText = pygame.font.Font("fonts/VampireWars.ttf", 50)
        TextSurf, TextRect = text_objects1("Pong - Instru????es", largeText, black)
        TextRect.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf, TextRect)


        subTitle = pygame.font.Font("fonts/Gazelle.ttf", 30)
        TextSurf, TextRect = text_objects1("Jogador 1", subTitle, black)
        TextRect.center = (250,(200))
        gameDisplay.blit(TextSurf, TextRect)


        subTitle1 = pygame.font.Font("fonts/Gazelle.ttf", 30)
        TextSurf, TextRect = text_objects1("Jogador 2", subTitle1, black)
        TextRect.center = (600,(200))
        gameDisplay.blit(TextSurf, TextRect)

        button("Voltar",275,490,250,60,purple,bright_purple,game_intro)

        pygame.display.update()
        clock.tick(15)



def quitgame():
    pygame.quit()
    quit()

def game_loop():
    print("game on")




