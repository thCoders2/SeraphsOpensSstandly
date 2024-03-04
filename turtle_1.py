import turtle

# Cria uma tela para desenho
tela = turtle.Screen()

# Cria uma tartaruga
tartaruga = turtle.Turtle()

# Desenha um quadrado
for _ in range(15):
    tartaruga.forward(100)  # Move para a frente por 100 unidades
    for _ in range(3):
        tartaruga.forward(100)  # Move para a frente por 100 unidades
        tartaruga.left(80)     # Vira a tartaruga 90 graus à direita
    tartaruga.right(130)     # Vira a tartaruga 90 graus à direita

# Fecha a janela ao clicar nela
tela.exitonclick()
