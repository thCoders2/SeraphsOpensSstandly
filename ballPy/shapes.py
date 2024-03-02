import tkinter as tk

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

# Criar a classe HealthBall que herda de Ball e tem um atributo extra health
class HealthBall(Ball):
    def __init__(self, x ,y ,vx ,vy ,color ,size):
        super().__init__(x ,y ,vx ,vy ,color ,size)
        # Inicializar a saúde como 100
        self.health = 100

    def heal(self ,other):
        # Aumentar a saúde da outra bola em 5 pontos por segundo
        other.health += 5 * (1/60) # Assumindo que o frame rate é 60 fps

    def collisionDetect(self):
        for j in range(len(balls)):
            if not (self == balls[j]):
                const dx = this.x - balls[j].x;
                const dy = this.y - balls[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
        
                if distance < this.size + balls[j].size:
                    # Se houver colisão ,curar a outra bola 
                    this.heal(balls[j])
