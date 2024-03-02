import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define os arrays de caracteres
karms = ["( '-')", "( '-')", '( "_")', '( -_-)', "( '_')", '( "_")','( "-")','( *_*)', '( *-*)', '( +_+)','( -_-)','#karma','( *_*)',"(*__*)", "(-__-)", '(*_*))', '((*_*)','(*__*)', '(*___*', '*____*', '-____-', '-___-)', '(-__-)', '( -_-)', '( "-")']
fearArr = ['(> oO<)', '(> oO>)', '(> oO)>', '(> Oo)>', '<( o0<)', '<(oO <)']
lilFearArr = ['(>oO<)', '(>oO>)', '(>oO)>', '(>Oo)>', '<(o0<)', '<(oO<)']

# Define a fonte e o tamanho dos caracteres
font = pygame.font.SysFont("Courier", 32)

# Define o tamanho dos caracteres (largura e altura)
char_width, char_height = 32, 32

# Define a quantidade de caracteres na horizontal e vertical
cols, rows = 10, 6

# Define o tamanho da tela baseado na quantidade de caracteres
screen_width, screen_height = cols * char_width, rows * char_height

# Cria uma janela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animação")

# Posição inicial do texto
text_x, text_y = 0, 0

# Define uma variável para controlar o loop principal
running = True

# Define variáveis para controlar a animação
index = 0
max_index = len(karms) + len(fearArr) + len(lilFearArr)

# Inicia o loop principal
while running:
    # Processa os eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        text_y = max(0, text_y - char_height)
    if keys[pygame.K_s]:
        text_y = min(screen_height - char_height, text_y + char_height)
    if keys[pygame.K_a]:
        text_x = max(0, text_x - char_width)
    if keys[pygame.K_d]:
        text_x = min(screen_width - char_width, text_x + char_width)

    # Preenche a tela com branco
    screen.fill(WHITE)

    # Renderiza cada caractere como uma superfície
    if index < len(karms):
        text = font.render(karms[index], True, BLACK)
        text.set_alpha(0.7 * 255)
        screen.blit(text, (text_x, text_y))
    elif index < len(karms) + len(fearArr):
        text = font.render(fearArr[index - len(karms)], True, BLACK)
        text.set_alpha(0.7 * 255)
        screen.blit(text, (text_x + 100, text_y + 50))
    else:
        text = font.render(lilFearArr[index - len(karms) - len(fearArr)], True, BLACK)
        text.set_alpha(0.7 * 255)
        screen.blit(text, (text_x + 150, text_y + 100))

    # Atualiza a tela
    pygame.display.flip()

    # Aumenta o índice para avançar para o próximo caractere
    index = (index + 1) % max_index

# Finaliza o pygame
pygame.quit()
sys.exit()
