# Importando o módulo Tkinter
import tkinter as tk
from tkinter import ttk

# Criando a janela principal
window = tk.Tk()
window.title("Customizador de Porta")
window.geometry("1200x900")

# Criando os widgets
label_tamanho = tk.Label(window, text="Tamanho da porta (em mm):")
label_largura = tk.Label(window, text="Largura:")
label_altura = tk.Label(window, text="Altura:")
entry_largura = tk.Entry(window)
entry_altura = tk.Entry(window)
button_largura_mais = tk.Button(window, text="+")
button_largura_menos = tk.Button(window, text="-")
button_altura_mais = tk.Button(window, text="+")
button_altura_menos = tk.Button(window, text="-")
label_tipo_vidro = tk.Label(window, text="Tipo de vidro:")
combo_tipo_vidro = ttk.Combobox(window, values=["Reflecta Fumê 4mm", "Reflecta Bronze 4mm", "Reflecta Prata 4mm", "Reflecta Verde 4mm"])
label_perfil = tk.Label(window, text="Perfil:")
combo_perfil = ttk.Combobox(window, values=["Alumínio Branco", "Alumínio Preto", "Alumínio Natural", "Alumínio Bronze"])
label_buscar = tk.Label(window, text="Buscar:")
entry_buscar = tk.Entry(window)
button_buscar = tk.Button(window, text="Buscar")
canvas_porta = tk.Canvas(window, width=800, height=800)
canvas_porta.create_rectangle(50, 50, 250, 250, fill="white", outline="black")

# Posicionando os widgets
label_tamanho.grid(row=0, column=0, sticky=tk.W)
label_largura.grid(row=1, column=0, sticky=tk.W)
entry_largura.grid(row=1, column=1)
button_largura_mais.grid(row=1, column=2)
button_largura_menos.grid(row=1, column=3)
label_altura.grid(row=2, column=0, sticky=tk.W)
entry_altura.grid(row=2, column=1)
button_altura_mais.grid(row=2, column=2)
button_altura_menos.grid(row=2, column=3)
label_tipo_vidro.grid(row=3, column=0, sticky=tk.W)
combo_tipo_vidro.grid(row=3, column=1)
label_perfil.grid(row=4, column=0, sticky=tk.W)
combo_perfil.grid(row=4, column=1)
label_buscar.grid(row=5, column=0, sticky=tk.W)
entry_buscar.grid(row=5, column=1)
button_buscar.grid(row=5, column=2)
canvas_porta.grid(row=0, column=4, rowspan=6)

# Definindo os valores padrão
entry_largura.insert(0, "1400")
entry_altura.insert(0, "2100")
combo_tipo_vidro.set("Reflecta Fumê 4mm")
combo_perfil.set("Alumínio Branco")

# Definindo as funções dos botões
def aumentar_largura():
    # Aumenta a largura da porta em 100 mm
    largura = int(entry_largura.get())
    largura += 100
    entry_largura.delete(0, tk.END)
    entry_largura.insert(0, str(largura))
    # Redimensiona o retângulo no canvas
    canvas_porta.coords(1, 50 + (1500 - largura) / 2 , 50 , 350 - (1500 - largura) / 2 , 250)

def diminuir_largura():
    # Diminui a largura da porta em 100 mm
    largura = int(entry_largura.get())
    largura -= 100
    entry_largura.delete(0, tk.END)
    entry_largura.insert(0, str(largura))
    # Redimensiona o retângulo no canvas
    canvas_porta.coords(1 , 50 + (1500 - largura) / 2 , 50 , 350 - (1500 - largura) / 2 , 250)

def aumentar_altura():
    # Aumenta a altura da porta em 100 mm
    altura = int(entry_altura.get())
    altura += 100
    entry_altura.delete(0 , tk.END)
    entry_altura.insert(0 , str(altura))
    # Redimensiona o retângulo no canvas
    canvas_porta.coords(1 , 50 , 50 + (2300 - altura) / 2 , 250 , 350 - (2300 - altura) / 2)

def diminuir_altura():
    # Diminui a altura da porta em 100 mm
    altura = int(entry_altura.get())
    altura -= 100
    entry_altura.delete(0 , tk.END)
    entry_altura.insert(0 , str(altura))
    # Redimensiona o retângulo no canvas
    canvas_porta.coords(1 , 50 , 50 + (2300 - altura) / 2 , 250 , 350 - (2300 - altura) / 2)

def buscar():
    # Busca a imagem do tipo de vidro selecionado na pasta /images/vidros/
    tipo_vidro = combo_tipo_vidro.get()
    imagem = tk.PhotoImage(file=f"/images/vidros/{tipo_vidro}.png")
    # Coloca a imagem no canvas
    canvas_porta.create_image(150, 150, image=imagem)
    # Mantém uma referência da imagem para evitar que seja apagada pelo coletor de lixo
    canvas_porta.imagem = imagem

# Associando as funções aos botões
button_largura_mais.config(command=aumentar_largura)
button_largura_menos.config(command=diminuir_largura)
button_altura_mais.config(command=aumentar_altura)
button_altura_menos.config(command=diminuir_altura)
button_buscar.config(command=buscar)

# Iniciando o loop principal
window.mainloop()
