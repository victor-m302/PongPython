import pygame
import sys
import random
import engine
import settings

def IA(player2, ball): #paddle AI
    #começo da raquete: y
    #fim da raquete: y+h
    #entre a raquete
    if((player2.rect.y + player2.rect.h)>= ball.sprite.rect.y) and (player2.rect.y <= ball.sprite.rect.y):
        print(False)
        player2.speed = 0
    elif(player2.rect.y >= ball.sprite.rect.y):
        print(True)
        player2.rect.y += -6

    elif((player2.rect.y + player2.rect.h)<= ball.sprite.rect.y):
        #print(True)
        player2.speed = 6
    

# define o loop principal do jogo single player
def start_game():
    xP = 20
    yP = settings.screen_height/2

    xO = settings.screen_width - 20
    yO = settings.screen_height/2

        # cria as raquetes do jogador e do oponente
    player = engine.Player("images/Paddle.png", xP, yP, 0)
    player2 = engine.Player("images/Paddle.png", xO, yO, 0)

    # cria um sprite group para que dessa forma sempre que precisar atualizar
    # ou desenhar as raquetes, todas sejam realizadas ao mesmo tempo, além
    # de ser utilizado para facilitar as colisões
    multiplayer_paddle_group = pygame.sprite.Group()
    multiplayer_paddle_group.add(player)
    multiplayer_paddle_group.add(player2)
    multiplayer_block_group = pygame.sprite.Group()
    # cria a bola do jogo, e também um sprite group para ela
    ball = engine.Ball("images/Ball.png", settings.screen_width/2,
            settings.screen_height/2, 4, 4, multiplayer_paddle_group, multiplayer_block_group)
    ball_group = pygame.sprite.GroupSingle()
    ball_group.add(ball)

    # cria o gerenciador do jogo para poder inicializa-lo no loop principal
    multiplayer_game_manager = engine.GameManager(ball_group, multiplayer_paddle_group, multiplayer_block_group)
    game_start_time = pygame.time.get_ticks()
    previous_player_score = 0


    while True:
        player.rect.y += player.speed
        player2.rect.y += player2.speed
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.QUIT): # sai do jogo se clicar no X
                pygame.quit()
                quit()
                #process input player
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    player.speed = -5
                if(event.key == pygame.K_RIGHT):
                    player.speed = 5
                if(event.key == pygame.K_a):
                    player2.speed = 5
                if(event.key == pygame.K_d):
                    player2.speed = -5
                else:
                    continue
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_LEFT):
                    player.speed = 0
                if(event.key == pygame.K_RIGHT):
                    player.speed = 0
                if(event.key == pygame.K_a):
                    player2.speed = 0
                if(event.key == pygame.K_d):
                    player2.speed = 0
                else:
                    continue
                
        current_time = pygame.time.get_ticks()	
        if current_time - game_start_time >= 3500:	
            game_start_time = current_time
            rand1 = random.randrange(50, settings.screen_width - 50)
            rand2 = random.randrange(50,settings.screen_height - 50)
            new_block = engine.Block("images/Block.png", rand1, rand2)	
            multiplayer_block_group.add(new_block)	



        # Desenha a tela de fundo
        settings.screen.fill(settings.bg_color_mult)
        # desenha a linha no meio da tela
        pygame.draw.rect(settings.screen, settings.accent_color, settings.middle_strip)

        # roda o jogo single player
        multiplayer_game_manager.run_game()

        # atualiza todo o conteúdo da tela
        pygame.display.flip()
        # define a velocidade do jogo
        settings.clock.tick(120)


'''
while true:
            player2.rect.y += player2.speed

            ########
                #process input player2
                elif(event.key == pygame.K_a):
                    player2.speed = 5
                    print("burt reynolds")
                elif(event.key == pygame.K_d):
                    player2.speed = -5    

                #process input player2
                elif(event.key == pygame.K_a):
                    player2.speed = 0
                elif(event.key == pygame.K_d):
                    player2.speed = 0
'''


'''
#original

    # loop principal do jogo single_player
    while True:
        player.rect.y += player.speed
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.QUIT): # sai do jogo se clicar no X
                pygame.quit()
                quit()
            #process input player
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    player.speed = -5
                elif(event.key == pygame.K_RIGHT):
                    player.speed = 5
                else:
                    continue
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_LEFT):
                    player.speed = 0
                elif(event.key == pygame.K_RIGHT):
                    player.speed = 0
                else:
                    continue

#mod


while True:
        player.rect.y += player.speed
        player2.rect.y += player2.speed
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.QUIT): # sai do jogo se clicar no X
                pygame.quit()
                quit()
            #process input player
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    player.speed = -5
                elif(event.key == pygame.K_RIGHT):
                    player.speed = 5
                else:
                    continue
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_LEFT):
                    player.speed = 0
                elif(event.key == pygame.K_RIGHT):
                    player.speed = 0
                else:
                    continue

        #process input player2
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_a):
                    player2.speed = 5
                elif(event.key == pygame.K_d):
                    player2.speed = -5
                else:
                    continue
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_a):
                    player2.speed = 0
                elif(event.key == pygame.K_d):
                    player2.speed = 0
                else:
                    continue'''