import tkinter as tk
import random

# Criar a janela
window = tk.Tk()
window.title("Bolas e Quadrados")

# Criar o canvas
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Criar as variáveis globais
balls = []
isCannabied = False
isGhosted = False
isBananed = False
isHackied = False

# Criar a classe Ball
class Ball:
    def __init__(self, x, y, vx, vy, color, size):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.shape = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)

    def move(self):
        # Atualizar a posição da bola
        self.x += self.vx
        self.y += self.vy

        # Verificar se a bola bateu nas bordas da tela
        if self.x - self.size < 0 or self.x + self.size > 800:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > 600:
            self.vy = -self.vy

        # Mover o shape no canvas
        canvas.move(self.shape, self.vx, self.vy)

    def collide(self, other):
        # Verificar se a bola colidiu com outra bola
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx**2 + dy**2)**0.5
        return distance < (self.size + other.size)

# Criar a classe Square que herda de Ball
class Square(Ball):
    def __init__(self, x, y, vx, vy, color, size):
        super().__init__(x, y, vx, vy, color, size)
        # Apagar o shape oval e criar um shape retangular
        canvas.delete(self.shape)
        self.shape = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color)

# Criar a classe Hackier que herda de Ball e tem um atributo extra hackedLevel
class Hackier(Ball):
    def __init__(self, x, y, vx, vy, color, size):
        super().__init__(x, y, vx, vy, color, size)
        # Adicionar uma borda preta ao shape oval
        canvas.itemconfig(self.shape, outline="black")
        # Inicializar o nível de hackeamento como 0
        self.hackedLevel = 0

    def hack(self):
        # Incrementar o nível de hackeamento
        self.hackedLevel += 1

# Criar uma função para gerar um número aleatório entre min e max
def random(min, max):
    return random.randint(min, max)

# Criar uma função para adicionar uma bola ou um quadrado mais rápido
def addQuicker(type=Ball):
    global balls

    # Verificar se o tipo é válido (Ball ou Square)
    if type not in [Ball, Square]:
        return

    # Gerar os atributos aleatórios da bola ou do quadrado
    size = random(10, 20)
    x = random(0 + size, 800 - size)
    y = random(0 + size, 600 - size)
    vx = random(1, 8)
    vy = random(1 ,8)
    color = 'rgb(' + str(random(0 ,255)) + ',' + str(random(0 ,255)) + ',' + str(random(0 ,255)) + ')'

    # Criar uma nova instância da classe Ball ou Square e adicionar à lista de bolas
    ball = type(x ,y ,vx ,vy ,color ,size)
    balls.append(ball)

    # Atualizar o texto do label qtdBall com o número de bolas na tela
    qtdBall["text"] = len(balls)

# Criar uma função para mudar a cor de todas as bolas na tela
def changeAllColor():
    global balls

    # Gerar uma nova cor aleatória
    newColor = 'rgb(' + str(random(0 ,255)) + ',' + str(random(0 ,255)) + ',' + str(random(0 ,255)) + ')'

    # Mudar a cor de cada bola na lista de bolas e no canvas
    for ball in balls:
        ball.color = newColor
        canvas.itemconfig(ball.shape, fill=newColor)

# Criar uma função para ativar o modo Thanos e eliminar metade das bolas na tela
def thanosMode():
    global balls

    # Escolher um número aleatório entre 0 e 1
    imparOuPar = random(0, 1)

    # Filtrar as bolas que têm índice ímpar ou par, dependendo do número sorteado
    newBalls = [ball for index, ball in enumerate(balls) if index % 2 == imparOuPar]

    # Apagar as bolas que foram eliminadas do canvas
    for ball in balls:
        if ball not in newBalls:
            canvas.delete(ball.shape)

    # Atualizar a lista de bolas com as que sobreviveram
    balls = newBalls

    # Atualizar o texto do label qtdBall com o número de bolas na tela
    qtdBall["text"] = len(balls)

# Criar uma função para ativar o modo Banana e mudar a cor de todas as bolas para amarelo
def bananaMode():
    global balls, isBananed

    # Alternar o valor da variável isBananed entre True e False
    isBananed = not isBananed

    # Mudar a cor de cada bola na lista de bolas e no canvas para amarelo
    for ball in balls:
        ball.color = 'rgb(255, 255, 0)'
        canvas.itemconfig(ball.shape, fill=ball.color)

# Criar uma função para ativar o modo Ghost e tornar todas as bolas transparentes
def ghostMode():
    global balls, isGhosted

    # Alternar o valor da variável isGhosted entre True e False
    isGhosted = not isGhosted

    # Se isGhosted é True, adicionar um fator de transparência à cor de cada bola na lista de bolas e no canvas
    if isGhosted:
        for ball in balls:
            ball.color = ball.color[:-1] + ',0.25)'
            canvas.itemconfig(ball.shape, fill=ball.color)
    
    # Se isGhosted é False, remover o fator de transparência à cor de cada bola na lista de bolas e no canvas
    else:
        for ball in balls:
            ball.color = ball.color[:-6] + ')'
            canvas.itemconfig(ball.shape, fill=ball.color)

# Criar uma função para ativar o modo Hacker e adicionar uma bola hacker na tela
def hackerMode():
    global balls, isHackied

    # Mudar o valor da variável isHackied para True
    isHackied = True

    # Adicionar uma bola hacker na tela usando a função addQuicker com o tipo Hackier
    addQuicker(Hackier)

# Criar uma função para transformar uma bola em uma bola hacker
def turnToHacked(ball):
    global balls

    # Criar uma nova instância da classe Hackier com os mesmos atributos da bola original, exceto a cor e o tamanho
    ballHack = Hackier(
        ball.x,
        ball.y,
        ball.vx,
        ball.vy,
        'rgb(0, 255, 0)',
        ball.size + (1.2)
      )

    # Apagar a bola original do canvas e da lista de bolas
    canvas.delete(ball.shape)
    balls.remove(ball)

    # Atualizar o texto do label qtdBall com o número de bolas na tela
    qtdBall["text"] = len(balls)

    # Adicionar a bola hacker à lista de bolas
    balls.append(ballHack)

# Criar uma função para mudar a cor de duas bolas que colidiram na tela
def changeColor(b1, b2):
    
    # Verificar se os modos Banana ou Hacker estão ativados, se sim, não mudar a cor das bolas
    if isBananed or isHackied:
        return

    # Gerar uma nova cor aleatória
    newColor = 'rgb(' + str(random(0 ,255)) + ',' + str(random(0 ,255)) + ',' + str(random(0 ,255)) + ')'

    # Mudar a cor das duas bolas na lista de bolas e no canvas para a nova cor
    b1.color = b2.color = newColor
    canvas.itemconfig(b1.shape, fill=newColor)
    canvas.itemconfig(b2.shape, fill=newColor)

# Criar um label para mostrar a quantidade de bolas na tela
qtdBall = tk.Label(window, text="0", font=("Arial", 20))
qtdBall.pack()

# Criar um botão para adicionar uma bola na tela
addBall = tk.Button(window, text="Adicionar Bola", command=lambda: addQuicker(Ball), font=("Arial", 20))
addBall.pack()

# Criar um botão para adicionar um quadrado na tela
addSquare = tk.Button(window, text="Adicionar Quadrado", command=lambda: addQuicker(Square), font=("Arial", 20))
addSquare.pack()

# Criar um botão para mudar a cor de todas as bolas na tela
changeColor = tk.Button(window, text="Mudar Cor", command=changeAllColor, font=("Arial", 20))
changeColor.pack()

# Criar um botão para ativar o modo Thanos e eliminar metade das bolas na tela
thanosButton = tk.Button(window, text="Modo Thanos", command=thanosMode, font=("Arial", 20))
thanosButton.pack()

# Criar um botão para ativar o modo Banana e mudar a cor de todas as bolas para amarelo
bananaButton = tk.Button(window, text="Modo Banana", command=bananaMode, font=("Arial", 20))
bananaButton.pack()

# Criar um botão para ativar o modo Ghost e tornar todas as bolas transparentes
ghostButton = tk.Button(window, text="Modo Ghost", command=ghostMode, font=("Arial", 20))
ghostButton.pack()

# Criar um botão para ativar o modo Hacker e adicionar uma bola hacker na tela
hackerButton = tk.Button(window, text="Modo Hacker", command=hackerMode, font=("Arial", 20))
hackerButton.pack()

# Criar uma função para atualizar a tela a cada frame
def update():
    global balls

    # Mover cada bola na lista de bolas
    for ball in balls:
        ball.move()

    # Verificar se há colisões entre as bolas na lista de bolas
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            # Se houver colisão, mudar a cor das bolas e aumentar o nível de hackeamento se forem bolas hacker
            if balls[i].collide(balls[j]):
                changeColor(balls[i], balls[j])
                if isinstance(balls[i], Hackier):
                    balls[i].hack()
                if isinstance(balls[j], Hackier):
                    balls[j].hack()
    
    # Verificar se há bolas hacker com nível de hackeamento igual a 2 e transformá-las em novas bolas hacker
    for ball in balls:
        if isinstance(ball, Hackier) and ball.hackedLevel == 2:
            turnToHacked(ball)

    # Chamar a função update novamente após 10 milissegundos
    window.after(10, update)

# Chamar a função update pela primeira vez
update()

# Iniciar o loop principal da janela
window.mainloop()
