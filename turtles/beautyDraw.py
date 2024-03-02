import turtle

# Set up the screen
screen = turtle.Screen()

# Create three turtle objects with different attributes
t1 = turtle.Turtle()
t1.fillcolor("yellow")

t2 = turtle.Turtle()
t2.fillcolor("red")

t3 = turtle.Turtle()
t3.fillcolor("blue")

# Define a function to draw a star
def draw_star(turtle, size):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Set initial positions for each turtle
t1.penup()
t1.goto(-150, 0)
t1.pendown()

t2.penup()
t2.goto(0, 0)
t2.pendown()

t3.penup()
t3.goto(150, 0)
t3.pendown()

# Draw stars using the defined function
draw_star(t1, 100)
draw_star(t2, 150)
draw_star(t3, 75)

# Close the graphics window when clicked
screen.exitonclick()
