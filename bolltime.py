import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definição do tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bolas Inc.")

# Classe para representar a bola
class Ball:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.growth_cost = 10
        self.earnings = size * 2

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

    def grow(self):
        if self.growth_cost <= grana:
            self.size += 5
            self.growth_cost += 10

    def check_collision(self, other_ball):
        dx = self.x - other_ball.x
        dy = self.y - other_ball.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.size + other_ball.size:
            earn_grana(other_ball.earnings)

# Variável para armazenar a grana do jogador
grana = 0

# Lista para armazenar as bolas no jogo
balls = []

def create_ball():
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    size = random.randint(20, 50)
    ball = Ball(x, y, size)
    balls.append(ball)

def earn_grana(earnings):
    global grana
    grana += earnings

# Loop principal do jogo
running = True
while running:
    screen.fill(BLACK)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                create_ball()

    # Desenha as bolas
    for ball in balls:
        ball.draw()

    # Verifica colisões
    for ball in balls:
        for other_ball in balls:
            if ball != other_ball:
                ball.check_collision(other_ball)

    # Exibe a grana na tela
    font = pygame.font.Font(None, 36)
    text = font.render(f"Grana: {grana}", True, WHITE)
    screen.blit(text, (20, 20))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
