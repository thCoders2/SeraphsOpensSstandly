from databases import karms, lilFearArr, fearArr
import tkinter as tk

class Personagem:
    def __init__(self, nome, animacao, velocidade, chapeu):
        self.nome = nome
        self.animacao = animacao
        self.velocidade = velocidade
        self.chapeu = chapeu
        self.speed = 4
        self.jump = 3

    def blablabla(self):
        print('blablabla')

    def atualizar_animacao(self, canvas, char):
        proximo_item = self.animacao.pop(0)
        canvas.itemconfig(char, text=proximo_item)
        self.animacao.append(proximo_item)
        root.after(self.velocidade, self.atualizar_animacao, canvas, char)

class Fear(Personagem):
    def __init__(self, nome, animacao, velocidade, chapeu, medo):
        animacao = fearArr
        super().__init__(nome, animacao, velocidade, chapeu)
        self.medo = medo

    def gritar(self):
        print("Ahhhh!")

class Karms(Personagem):
    def __init__(self, nome, animacao, velocidade, chapeu, karma):
        animacao = karms
        super().__init__(nome, animacao, velocidade, chapeu)
        self.karma = karma

    def sorrir(self):
        print(":)")

class LilFear(Personagem):
    def __init__(self, nome, animacao, velocidade, chapeu, lilFear):
        animacao = lilFearArr
        super().__init__(nome, animacao, velocidade, chapeu)
        self.lilFear = lilFear

    def chorar(self):
        print("Buááá!")

root = tk.Tk()

fear = Fear("Fear", fearArr, 200, "Chapeu1", "Medo1")
karm = Karms("Karms", karms, 200, "Chapeu2", "Karma1")
lilF = LilFear("LilFear", lilFearArr, 200, "Chapeu3", "LilFear1")

characteres = [fear, karm, lilF]

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()



char_text = canvas.create_text(150, 100, text=fear.animacao[0], font=("Courier", 32), fill="blue")
name_text = canvas.create_text(150, 150, text=fear.nome, font=("Courier", 16), fill="black")

def update_char(char, char_text):
    next_item = char.animacao.pop(0)
    canvas.itemconfig(char_text, text=next_item)
    char.animacao.append(next_item)
    root.after(char.velocidade, update_char, char, char_text)

# update_char(char1, char_text)

def switchChar():
    update_char(karm)
    # global current
    # increment the current index by one modulo the length of the array
    # current = (current + 1) % len(possiblesPerson)
    # update the name text object
    # canvas.itemconfig(name, text=names[current])

    # create the button widget for switching characters
    button = tk.Button(root, text="Next Character", command=switchChar)
    button.pack()


root.mainloop()
