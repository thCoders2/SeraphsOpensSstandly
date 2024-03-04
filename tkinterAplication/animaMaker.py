import tkinter as tk
from tkinter import messagebox

# Função para adicionar um novo quadro à animação
def adicionar_quadro():
    caracter = entrada_caracter.get()
    if caracter:
        lista_quadros.insert(tk.END, caracter)
        entrada_caracter.delete(0, tk.END)

# Função para remover o quadro selecionado
def remover_quadro():
    try:
        selecionado = lista_quadros.curselection()
        lista_quadros.delete(selecionado)
    except:
        pass

# Função para criar a animação
def criar_animacao():
    animacao = lista_quadros.get(0, tk.END)
    messagebox.showinfo("Animação Criada", "Animação: " + " -> ".join(animacao))

# Configuração da interface gráfica
app = tk.Tk()
app.title("Criador de Animação de Caracteres")

entrada_caracter = tk.Entry(app)
entrada_caracter.pack()

btn_adicionar = tk.Button(app, text="Adicionar Quadro", command=adicionar_quadro)
btn_adicionar.pack()

btn_remover = tk.Button(app, text="Remover Quadro Selecionado", command=remover_quadro)
btn_remover.pack()

lista_quadros = tk.Listbox(app)
lista_quadros.pack()

btn_criar_animacao = tk.Button(app, text="Criar Animação", command=criar_animacao)
btn_criar_animacao.pack()

app.mainloop()
