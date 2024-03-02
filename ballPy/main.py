import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu Jogo Simples")

# Cores
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Classe para guardar informações do jogador
class Player:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed = 5
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 50
        self.skills = {
            "sword": 10,
            "magic": 5
        }
        self.experience = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def attack(self, target):
        damage = self.skills["sword"]
        target.health -= damage
        if target.health <= 0:
            self.experience += 10
            target.health = 0

# Classe para guardar informações de inimigos
class Enemy:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.speed = 2
        self.health = 30
        self.max_health = 30

    def move(self):
        self.x += random.choice([-self.speed, self.speed])
        self.y += random.choice([-self.speed, self.speed])

# Instanciar o jogador
player = Player()

# Lista de inimigos
enemies = [Enemy() for _ in range(5)]

# Fonte para exibir informações na tela
font = pygame.font.Font(None, 36)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Movimentar inimigos
    for enemy in enemies:
        enemy.move()

        # Verificar colisões e realizar ataques
        if abs(player.x - enemy.x) < 30 and abs(player.y - enemy.y) < 30:
            player.attack(enemy)

    # Preencher a tela com a cor branca
    screen.fill(white)

    # Desenhar o jogador
    pygame.draw.rect(screen, red, (player.x, player.y, 50, 50))

    # Desenhar inimigos
    for enemy in enemies:
        pygame.draw.rect(screen, blue, (enemy.x, enemy.y, 40, 40))

    # Exibir informações do jogador
    player_info = f"Level: {player.level} | HP: {player.health}/{player.max_health} | MP: {player.mana}/{player.max_mana} | Exp: {player.experience}"
    text = font.render(player_info, True, red)
    screen.blit(text, (10, 10))

    # Atualizar a tela
    pygame.display.flip()
