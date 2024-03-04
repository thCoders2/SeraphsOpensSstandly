import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing")

# Create the turtle
t = turtle.Turtle()

# Function to move the turtle forward by a certain distance
def move_forward():
    t.forward(10)

# Function to move the turtle backward by a certain distance
def move_backward():
    t.backward(10)

# Function to turn the turtle left by a certain angle
def turn_left():
    t.left(30)

# Function to turn the turtle right by a certain angle
def turn_right():
    t.right(30)

# Function to draw a star at the current turtle position
def draw_star():
    t.penup()
    t.goto(t.pos())
    t.pendown()
    
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(30)  # Adjust the size of the star
        t.right(144)
    t.end_fill()

# Function to lift the pen (pen up)
def pen_up():
    t.penup()

# Function to lower the pen (pen down)
def pen_down():
    t.pendown()

# Set up event listeners for WASD and arrow keys
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(draw_star, "space")
screen.onkeypress(pen_up, "u")  # Pen up
screen.onkeypress(pen_down, "n")  # Pen down

setInter

# Set up event listeners for arrow keys
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

# Start listening for events
screen.listen()
screen.mainloop()
