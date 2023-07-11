from databases import karms, lilFearArr, fearArr
import tkinter as tk
root = tk.Tk()

# Criar a classe Personagem
class Personagem:
    # Inicializar os atributos comuns
    def __init__(self, nome, animacao, velocidade, chapeu):
        self.nome = nome
        self.animacao = animacao
        self.velocidade = velocidade
        self.chapeu = chapeu

    def blablabla(self):
        print('blablabla')

    # Definir um método para atualizar a animação
    def atualizar_animacao(self, canvas, char):
        proximo_item = self.animacao.pop(0) # Obter o próximo item na lista de animação
        canvas.itemconfig(char, text=proximo_item)  # Atualizar o objeto de texto no canvas
        self.animacao.append(proximo_item)  # Colocar o item de volta na lista de animação
        root.after(self.velocidade, self.atualizar_animacao, canvas, char)  # Agendar a próxima atualização após a velocidade definida

# Criar a subclasse Fear que herda da classe Personagem
class Fear(Personagem):
    # Inicializar os atributos específicos de Fear
    def __init__(self, nome, animacao , velocidade, chapeu, medo):

        animacao = fearArr
        # Chamar o método __init__ da classe pai
        super().__init__(nome, animacao, velocidade, chapeu)
        # Adicionar o atributo medo
        self.medo = medo

    # Definir um método específico de Fear
    def gritar(self):
        print("Ahhhh!")

# Criar a subclasse Karms que herda da classe Personagem
class Karms(Personagem):
    # Inicializar os atributos específicos de Karms
    def __init__(self, nome, animacao, velocidade, chapeu, karma):
        # Chamar o método __init__ da classe pai
        animacao = karms
        super().__init__(nome, animacao, velocidade, chapeu)
        # Adicionar o atributo karma
        self.karma = karma

    # Definir um método específico de Karms
    def sorrir(self):
        print(":)")

# Criar a subclasse LilFear que herda da classe Personagem
class LilFear(Personagem):
    # Inicializar os atributos específicos de LilFear
    def __init__(self, nome, animacao, velocidade, chapeu, lilFear):
        # Chamar o método __init__ da classe pai
        animacao = lilFearArr
        super().__init__(nome, animacao, velocidade, chapeu)
        # Adicionar o atributo lilFear
        self.lilFear = lilFear

    # Definir um método específico de LilFear
    def chorar(self):
        print("Buááá!")
