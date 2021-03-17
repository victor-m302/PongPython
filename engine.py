import pygame
import sys
import random
import settings

class Block(pygame.sprite.Sprite): # classe base para criar os sprites dos objetos do jogo
    def __init__(self, image_path, x_pos, y_pos):
        super().__init__()
        # carrega uma imagem a partir da variavel image_path
        self.image = pygame.image.load(image_path)
        # cria um retângulo em volta da imagem que foi adicionada e já define
        # a posição dele na tela
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Player(Block): # classe responsável por criar o jogador(es)
    def __init__(self, image_path, x_pos, y_pos, speed):
        super().__init__(image_path, x_pos, y_pos)
        self.speed = speed # define a velocidade do jogador
        self.movement = 0 # define para onde o jogador irá se movimentar
    
    
    # função para atualizar a raquete, no caso o ball_group não será utilizado
    # mas ele é colocado para generalizar a função update() para que o paddle_group 
    # possa atualizar o jogador e o oponente ao mesmo tempo, sem precisar fazer cada um separadamente
    def update(self, ball_group):
        # aqui vai o código para atualizar o jogador
        self.screen_constrain() # é chamado para impedir o jogador de sair da tela
    
    
    # função para impor limites na raquete, para que ela não
    # saia da tela
    def screen_constrain(self):
        print("")

class Opponent(Block):
    def __init__(self, image_path, x_pos, y_pos, speed):
        super().__init__(image_path, x_pos, y_pos)
        self.speed = speed # velocidade do oponente

    # função para atualizar o oponente
    def update(self, ball_group):
        # aqui vai o código para atualizar o oponente
        self.screen_constrain() # é chamado para impedir que o oponente saia da tela 

    # função para impedir que o oponente saia da tela
    def screen_constrain(self):
        print("")

class Ball(Block):
    def __init__(self, image_path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(image_path, x_pos, y_pos)
        # define aleatóriamente para qual direção a bola vai ir
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles # armazena os dados das raquetes
        self.active = False # variavel para saber quando a bola está se movimentando ou não
        self.score_time = 0 # utilizada para pegar o tempo quando a bola resetar

    # função para definir as colisões da bola com as raquetes, e a própria tela
    def collisions(self):
        print("")

    # função para resetar a bola sempre que alguém marca um ponto
    # que será chamada no game manager
    def reset_ball(self):
        print("")
    
    # função para resetar o contador, que é chamado sempre
    # que alguém marca um ponto
    def restart_counter(self):
        print("")

class GameManager(Block): # função que será responsável por gerenciar o jogo
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0 # pontuação do jogador
        self.opponent_score = 0 # pontuação do oponente
        # tanto ball_group quanto paddle_group serão utilizados para
        # realizar as atualizações do jogo conforme determinados
        # eventos ocorrem
        self.ball_group = ball_group 
        self.paddle_group = paddle_group

    # função responsável 
    #por inicializar o jogo
    def run_game(self):
        # desenha os elementos do jogo na tela
        self.paddle_group.draw(settings.screen)
        self.ball_group.draw(settings.screen)

        # atualiza os elementos do jogo
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    
    # função para verificar se a bola saiu da tela, para então resetar a bola
    # e adicionar uma pontuação para o jogador ou oponente
    def reset_ball(self):
        print("")
    
    # desenha na tela o score do jogador e oponente
    def draw_score(self):
        print("")



