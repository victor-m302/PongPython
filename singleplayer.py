import pygame
import sys
import random
import engine
import settings

# define o loop principal do jogo single player
def start_game():
    xP = 20
    yP = settings.screen_height/2

    xO = settings.screen_width - 20
    yO = settings.screen_height/2

        # cria as raquetes do jogador e do oponente
    player = engine.Player("images/Paddle.png", xP, yP, 0)
    opponent = engine.Opponent("images/Paddle.png", xO, yO, 0)

    # cria um sprite group para que dessa forma sempre que precisar atualizar
    # ou desenhar as raquetes, todas sejam realizadas ao mesmo tempo, além
    # de ser utilizado para facilitar as colisões
    singleplayer_paddle_group = pygame.sprite.Group()
    singleplayer_paddle_group.add(player)
    singleplayer_paddle_group.add(opponent)

    # cria a bola do jogo, e também um sprite group para ela
    ball = engine.Ball("images/Ball.png", settings.screen_width/2,
            settings.screen_height/2, 4, 4, singleplayer_paddle_group, singleplayer_block_group)
    ball_group = pygame.sprite.GroupSingle()
    ball_group.add(ball)

    # cria o gerenciador do jogo para poder inicializa-lo no loop principal
    singleplayer_game_manager = engine.GameManager(ball_group, singleplayer_paddle_group, singleplayer_block_group)

    '''
    game_start_time = pygame.time.get_ticks()
    previous_player_score = 0
    '''
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
        # Desenha a tela de fundo
        settings.screen.fill(settings.bg_color)
        # desenha a linha no meio da tela
        pygame.draw.rect(settings.screen, settings.accent_color, settings.middle_strip)

        # roda o jogo single player
        singleplayer_game_manager.run_game()

        # atualiza todo o conteúdo da tela
        pygame.display.flip()
        # define a velocidade do jogo
        settings.clock.tick(120)

        '''        
        WHILE tRUE: ...
        opponent.rect.y += opponent.speed
        ...
        #process input opponent
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_a):
                    opponent.speed = 5
                elif(event.key == pygame.K_d):
                    opponent.speed = -5
                else:
                    continue
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_a):
                    opponent.speed = 0
                elif(event.key == pygame.K_d):
                    opponent.speed = 0
                else:
                    continue'''