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
        if self.rect.top <= 0:  # raquete-tela superior
            self.rect.top = 0
        if self.rect.bottom >= settings.screen_height:  # raquete-tela interior
            self.rect.bottom = settings.screen_height

    #update da raquete
    def update(self, ball_group):
        self.rect.y += self.movement  # movimenta a raquete
        self.screen_constrain()  # limite da raquete

class Opponent(Block):
    def __init__(self, image_path, x_pos, y_pos, speed):
        super().__init__(image_path, x_pos, y_pos)
        self.speed = speed # velocidade do oponente

    # função para atualizar o oponente
    def update(self, ball_group):
        # aqui vai o código para atualizar o oponente (AI BÁSICA)
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed #percebe bola para cima, se move para cima
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed #percebe bola para baixo, se move para baixo
        self.screen_constrain() # é chamado para impedir que o oponente saia da tela 
    # função para atualizar o oponente


    def IA(self, ball_group): #paddle AI
        if (self.rect.y < ball_group.sprite.rect.y and ball_group.sprite.rect.y < self.rect.y + self.rect.h):
            self.speed = 0
            self.rect.y += self.speed
        elif (self.rect.y + (self.rect.h / 2) < ball_group.sprite.rect.y):
            self.speed = 4
        
        elif (self.rect.y + (self.rect.h / 2) > ball_group.sprite.rect.y):
            self.speed = -4
        
        self.rect.update()



    # função para impedir que o oponente saia da tela
    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= settings.screen_height:
            self.rect.bottom = settings.screen_height


class Ball(Block):
    def __init__(self, image_path, x_pos, y_pos, speed_x, speed_y, paddles, blocks):
        super().__init__(image_path, x_pos, y_pos)
        # define aleatóriamente para qual direção a bola vai ir
        self.initial_speed_x = speed_x
        self.initial_speed_y = speed_y

        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles # armazena os dados das raquetes
        self.blocks = blocks # armazena os dados de blocks
        self.active = True # variavel para saber quando a bola está se movimentando ou não
        self.score_time = 0 # utilizada para pegar o tempo quando a bola resetar
        self.reset_paddle = False

    # função para atualizar o movimento da bola
    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()  # chama a função de colisões
        else:
            self.restart_counter()


    #####################

        # função para definir as colisões da bola com as raquetes, e a própria tela
    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= settings.screen_height: 
        #som de hit quando a bola colide com o limite inferior e superiror da tela
            pygame.mixer.Sound.play(settings.hit_sound)
            self.speed_y *= -1 # reflete a bola
        #if's para sprite
        if pygame.sprite.spritecollide(self, self.blocks, False):
            collision_block = pygame.sprite.spritecollide(self, self.blocks, True)[0].rect
            increase_speed_x = 0
            increase_speed_y = 0
            pygame.mixer.Sound.play(settings.destroy_sound)
            if self.initial_speed_x * 2 > self.speed_x:
                increase_speed_x = -0.02
            if self.initial_speed_y * 2 < self.speed_y:
                increase_speed_y = -0.02
            if abs(self.rect.right - collision_block.left) < 10 and self.speed_x > 0:
                self.speed_x *= (-1 + increase_speed_x)
            if abs(self.rect.left - collision_block.right) < 10 and self.speed_x < 0:
                self.speed_x *= (-1 + increase_speed_x)
            if abs(self.rect.top - collision_block.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_block.bottom
                self.speed_y *= (-1 + increase_speed_y)
            if abs(self.rect.bottom - collision_block.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_block.top
                self.speed_y *= (-1 + increase_speed_y)
            # (self, self.paddles, False)
            # bola(self), raquetes(self.paddles) , bool => The True flag will remove the sprite in block_list
                                                        #The False flag will keep the sprite in block_list
        #colisão ball-raquete com sprite
        if pygame.sprite.spritecollide(self, self.paddles, False): #toca o som de hit
            pygame.mixer.Sound.play(settings.hit_sound)# como retorna uma lista de elementos, é pego# somente o primeiro elemento, que pode ser a raquete# do jogador ou do oponente
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            # agora que sabemos qual raquete está ocorrendo# a colisão, basta utilizar as condições a seguir# para mudar a posição da bola
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
                print("x-1")
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
                print("x-1")
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
                print("y-1")
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1# função para resetar a bola sempre que algúem marca# um ponto
                print("y-1")

    ##########################


    def reset_ball(self, start_game):
        self.reset_paddle = True
        self.active = False  # a bola não esta movimentando
        # define de forma aleatória a direção que irá iniciar
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        # pega o tempo quando a bola foi resetada
        self.score_time = pygame.time.get_ticks()
        # joga a bola para o centro da tela
        self.rect.center = (settings.screen_width/2, settings.screen_height/2)
        # ativa um som quando a bola sai pra fora da tela
        if(not start_game):
            pygame.mixer.Sound.play(settings.score_sound)
        # função para resetar o contador, que é chamado sempre
        # que alguém marca algum ponto, ou no inicio do jogo


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
    def __init__(self, ball_group, paddle_group, block_group):
        self.player_score = 0 # pontuação do jogador
        self.opponent_score = 0 # pontuação do oponente
        # tanto ball_group quanto paddle_group serão utilizados para
        # realizar as atualizações do jogo conforme determinados
        # eventos ocorrem
        self.ball_group = ball_group 
        self.paddle_group = paddle_group
        self.block_group = block_group

    # função responsável 
    #por inicializar o jogo
    def run_game(self):
        # desenha os elementos do jogo na tela
        self.paddle_group.draw(settings.screen)
        self.ball_group.draw(settings.screen)
        self.block_group.draw(settings.screen)

        # atualiza os elementos do jogo
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.block_group.update()
        self.reset_ball()
        self.draw_score()

    
    # função para verificar se a bola saiu da tela, para então resetar a bola
    # e adicionar uma pontuação para o jogador ou oponente
    def reset_ball(self):
        # Se a bola passar da direita da tela, ponto para o player
        if self.ball_group.sprite.rect.right >= settings.screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball(False)

        # Se a bola passar da esquerda da tela, ponto para o oponente 
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball(False)
    
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


##bonus classes

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([1, 1])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
class Button(pygame.sprite.Sprite):
    def __init__(self, base_images_path, number_of_images, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        for i in range(number_of_images):
            image_path = base_images_path + str(i + 1) + ".png"
            self.sprites.append(pygame.image.load(image_path))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        self.current_sprite += 0.07
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
class Text(pygame.sprite.Sprite):
    def __init__(self, base_images_path, number_of_images, sprite_velocity, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprite_velocity = sprite_velocity
        for i in range(number_of_images):
            image_path = base_images_path + str(i + 1) + ".png"
            self.sprites.append(pygame.image.load(image_path))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        self.current_sprite += self.sprite_velocity
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
