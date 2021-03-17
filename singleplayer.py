import pygame
import sys
import random
import engine
import settings

# define o loop principal do jogo single player
def start_game():
    # cria as raquetes do jogador e do oponente
    player = engine.Player("images/Paddle.png", settings.screen_width - 20, settings.screen_height/2, 5)
    opponent = engine.Opponent("images/Paddle.png", 20, settings.screen_height/2, 5)

    # cria um sprite group para que dessa forma sempre que precisar atualizar
    # ou desenhar as raquetes, todas sejam realizadas ao mesmo tempo, além
    # de ser utilizado para facilitar as colisões
    singleplayer_paddle_group = pygame.sprite.Group()
    singleplayer_paddle_group.add(player)
    singleplayer_paddle_group.add(opponent)

    # cria a bola do jogo, e também um sprite group para ela
    ball = engine.Ball("images/Ball.png", settings.screen_width/2,
            settings.screen_height/2, 4, 4, singleplayer_paddle_group)
    ball_group = pygame.sprite.GroupSingle()
    ball_group.add(ball)

    # cria o gerenciador do jogo para poder inicializa-lo no loop principal
    singleplayer_game_manager = engine.GameManager(ball_group, singleplayer_paddle_group)

    # loop principal do jogo single_player
    while True:
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.QUIT): # sai do jogo se clicar no X
                pygame.quit()
                quit()

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