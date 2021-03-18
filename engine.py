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
        self.active = True # variavel para saber quando a bola está se movimentando ou não
        self.score_time = 0 # utilizada para pegar o tempo quando a bola resetar

    # função para atualizar o movimento da bola
    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        else:
            self.restart_counter()

    # função para definir as colisões da bola com as raquetes, e a própria tela
    def collisions(self):
        print("")

    # função para resetar a bola sempre que alguém marca um ponto
    # que será chamada no game manager
    def reset_ball(self):
        # Desativa a bola e guarda o tempo
        self.active = False
        self.score_time = pygame.time.get_ticks()
        # Define a direção da bola
        self.speed_x = self.speed_x * random.choice((-1, 1))
        self.speed_y = self.speed_y * random.choice((-1, 1))
        # Move a bola para o centro
        self.rect.center = settings.screen_width/2, settings.screen_height/2
    
    # função para resetar o contador, que é chamado sempre
    # que alguém marca um ponto
    def restart_counter(self):
        # Pega o tempo atual do jogo
        current_time = pygame.time.get_ticks()

        # Contador de 3 segundos para reiniciar o jogo
        countdown_number = 3
        if current_time - self.score_time <= 700:
            countdown_number = 3
        elif 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
        elif 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        elif current_time - self.score_time >= 2100:
            self.active = True

        # Desenhar tempo para reiniciar o jogo
        time_counter = settings.font.render(str(countdown_number), True, settings.accent_color)
        # Posição do texto
        time_counter_rect = time_counter.get_rect(center = (settings.screen_width/2, settings.screen_height/2 - 50))
        # Colocar este texto como preferencia na tela
        pygame.draw.rect(settings.screen, settings.bg_color, time_counter_rect)
        # Desenhar na tela o tempo
        settings.screen.blit(time_counter, time_counter_rect)


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
        # Se a bola passar da direita da tela, ponto para o player
        if self.ball_group.sprite.rect.right >= settings.screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()

        # Se a bola passar da esquerda da tela, ponto para o oponente 
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()
    
    # desenha na tela o score do jogador e oponente
    def draw_score(self):
        print("")
        player_score = settings.font.render(str(self.player_score), True, settings.accent_color)
        opponent_score = settings.font.render(str(self.opponent_score), True, settings.accent_color)

        # posição dos score
        player_score_rect = player_score.get_rect(midleft = (settings.screen_width / 2 + 40, settings.screen_height/2))
        opponent_score_rect = opponent_score.get_rect(midright = (settings.screen_width/2 - 40, settings.screen_height/2))

        # desenhar na tela os dois scores
        settings.screen.blit(player_score, player_score_rect)
        settings.screen.blit(opponent_score, opponent_score_rect)



