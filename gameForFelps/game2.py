import tkinter as tk
from tkinter import font

# Cores
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"

# Variáveis do jogo
coins = 0
lil_coins = 0
big_coins = 0

# Função para atualizar a tela
def draw_screen():
    canvas.delete("all")  # Limpar o canvas

    # Desenhar informações do jogo
    coins_label.config(text=f"Moedas: {coins}")

    # Desenhar lilMoedas
    for i in range(lil_coins):
        coin_text = canvas.create_text(
            50, 150 + i * 30, text="lilMoeda", fill=BLACK, font=coin_font
        )

    # Desenhar bigMoedas
    canvas.create_text(50, 400, text="bigMoeda", fill=RED, font=big_coin_font)

# Função chamada quando o jogador clica na tela
def on_click(event):
    global coins, lil_coins
    coins += 1
    lil_coins += 1
    draw_screen()

# Função chamada quando o jogador pressiona o botão de upgrade
def on_upgrade_click():
    global lil_coins, big_coins
    if lil_coins >= 5:
        lil_coins -= 5
        big_coins += 1
        draw_screen()

# Configuração da janela principal
root = tk.Tk()
root.title("Tkinter Clicker")

# Fontes
coin_font = font.Font(size=12)
big_coin_font = font.Font(size=24, weight="bold")

# Labels
coins_label = tk.Label(root, text=f"Moedas: {coins}", fg=BLACK)
coins_label.pack(pady=20)

# Canvas para desenhar as moedas
canvas = tk.Canvas(root, width=200, height=500, bg=WHITE)
canvas.pack()

# Eventos do canvas
canvas.bind("<Button-1>", on_click)

# Botão de upgrade
upgrade_button = tk.Button(
    root, text="Upgrade (5 lilMoedas -> 1 bigMoeda)", command=on_upgrade_click
)
upgrade_button.pack(pady=10)

# Loop principal da aplicação
root.mainloop()