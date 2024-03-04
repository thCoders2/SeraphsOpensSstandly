import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, x, y, velX, velY, color, size):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.color = color
        self.size = size
        self.colisions = 0
        self.borda = random.randint(0, 1)
        self.zero_ou_um = random.randint(0, 1)

        self.ball_id = canvas.create_oval(
            self.x - size, self.y - size, self.x + size, self.y + size, fill=color
        )

    def multiply(self, b1, b2):
        pass

    def banana_draw(self):
        self.canvas.create_arc(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            start=0,
            extent=180,
            fill=self.color,
        )

    def draw(self):
        if self.borda:
            self.canvas.create_oval(
                self.x - self.size,
                self.y - self.size,
                self.x + self.size,
                self.y + self.size,
                outline=self.color,
            )
        else:
            self.canvas.create_oval(
                self.x - self.size,
                self.y - self.size,
                self.x + self.size,
                self.y + self.size,
                fill=self.color,
            )

    def update(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if (self.x + self.size) >= width:
            self.velX = -self.velX
            self.x = width - self.size - 1
            self.cannabrick()

        if (self.x - self.size) <= 0:
            self.velX = -self.velX
            self.x = self.size + 1
            self.cannabrick()

        if (self.y + self.size) >= height:
            self.velY = -self.velY
            self.y = height - self.size - 1
            self.cannabrick()

        if (self.y - self.size) <= 0:
            self.velY = -self.velY
            self.y = self.size + 1
            self.cannabrick()

        self.x += self.velX
        self.y += self.velY

    def collision_detect(self):
        balls = self.canvas.balls
        for j in range(len(balls)):
            if self is not balls[j]:
                dx = self.x - balls[j].x
                dy = self.y - balls[j].y
                distance = (dx ** 2 + dy ** 2) ** 0.5

                if distance < self.size + balls[j].size:
                    self.muda_rota_muda_cor(balls[j])
                    self.colisioned()
                    self.add_ball_colision_counter(balls[j])

    def muda_rota_muda_cor(self, ball1, ball2):
    # if not is_cannabied:
        self.change_color(ball1, ball2)

        ball1.velX = -ball1.velX
        ball2.velX = -ball2.velX
        ball1.velY = -ball1.velY
        ball2.velY = -ball2.velY

        ball1.x += 2 * ball1.velX
        ball2.x += 2 * ball2.velX
        ball1.y += 2 * ball1.velY
        ball2.y += 2 * ball2.velY
    # else:
    #     self.cannabis_rota(ball1, ball2)

    # def cannabrick(self):
    #     if is_cannabied and is_ghosted:
    #         self.color = self.ghost_cor(self.cannabis_cor())
    #     elif is_cannabied:
    #         self.color = self.cannabis_cor()

    def ghost_cor(self, string_color):
        return string_color[:-1] + ",0.25)"

    def random_rgb(self):
        return f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"

    def colisioned(self):
        pass

    def add_ball_colision_counter(self, ball):
        pass

    def change_color(self, b1, b2):
        # if not is_bananed and not is_hackied:
        b1.color = b2.color = self.random_rgb()

class Square(Ball):
    def __init__(self, canvas, x, y, velX, velY, color, size):
        super().__init__(canvas, x, y, velX, velY, color, size)

    def draw(self):
        if self.borda:
            self.canvas.create_rectangle(
                self.x - self.size,
                self.y - self.size,
                self.x + self.size,
                self.y + self.size,
                outline=self.color,
            )
        else:
            self.canvas.create_rectangle(
                self.x - self.size,
                self.y - self.size,
                self.x + self.size,
                self.y + self.size,
                fill=self.color,
            )

class Hackier(Ball):
    def __init__(self, canvas, x, y, velX, velY, color, size):
        super().__init__(canvas, x, y, velX, velY, color, size)

    def draw(self):
        self.canvas.create_text(
            self.x,
            self.y,
            text="0" if self.zero_ou_um == 0 else "1",
            fill="rgb(0,255,0)",
            font=f"bold {self.size * 2}",
        )

    def collision_detect(self):
        balls = self.canvas.balls
        for j in range(len(balls)):
            if self is not balls[j]:
                dx = self.x - balls[j].x
                dy = self.y - balls[j].y
                distance = (dx ** 2 + dy ** 2) ** 0.5

                if distance < self.size + balls[j].size:
                    self.ball_hacked(balls[j])
                    self.muda_rota_muda_cor(balls[j])
                    self.colisioned()
                    self.add_ball_colision_counter(balls[j])

    def ball_hacked(self, ball):
        if not hasattr(ball, "hacked_level"):
            ball.hacked_level = 0
        ball.hacked_level += 1
        print(ball.hacked_level)
        if ball.hacked_level == 1:
            ball.color = "rgb(0,255,0)"
            ball.borda = True
        elif ball.hacked_level == 2:
            self.turn_to_hacked(ball)

    def turn_to_hacked(self, ball):
        ball_hack = Hackier(
            self.canvas,
            ball.x,
            ball.y,
            random.randint(1, 8),
            random.randint(1, 8),
            "rgb(0,255,0)",
            ball.size + 1.2,
        )
        # if is_ghosted:
        #     ball.color = self.ghost_cor(ball.color)

        self.canvas.balls = [b for b in self.canvas.balls if b != ball]
        self.canvas.balls.append(ball_hack)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bouncing Balls")
        self.geometry("500x500")

        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        self.balls = []
        self.create_widgets()
        self.loop()

    def create_widgets(self):
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        while len(self.balls) < 5:
            self.add_ball(Square)
            self.add_ball()

    def add_ball(self, ball_class=Ball):
        size = random.randint(10, 20)
        x = random.randint(size, self.canvas.winfo_width() - size)
        y = random.randint(size, self.canvas.winfo_height() - size)
        velX = random.randint(1, 8)
        velY = random.randint(1, 8)
        color = self.random_rgb()

        ball = ball_class(self.canvas, x, y, velX, velY, color, size)
        self.balls.append(ball)

    def random_rgb(self):
        return f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"

    def on_canvas_resize(self, event):
        self.canvas.config(width=event.width, height=event.height)

    def loop(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(
            0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill="rgba(0, 0, 0, 0.275)"
        )

        for ball in self.balls:
            # if is_bananed:
            #     ball.banana_draw()
            # else:
            #     ball.draw()

            # if not is_ghosted:
            #     ball.collision_detect()

            ball.update()

        self.after(16, self.loop)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
