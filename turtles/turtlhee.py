import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Auto Movement")

# Create the turtle
t = turtle.Turtle()

# Set the initial movement angle and speed
movement_angle = 0
movement_speed = 5

# Function to move the turtle forward
def move_forward():
    t.forward(movement_speed)

# Function to turn the turtle left
def turn_left():
    global movement_angle
    movement_angle += 30
    t.setheading(movement_angle)

# Function to turn the turtle right
def turn_right():
    global movement_angle
    movement_angle -= 30
    t.setheading(movement_angle)

# Update the turtle's position automatically
def update_position():
    move_forward()
    screen.ontimer(update_position, 100)  # Move every 100 milliseconds

# Set up event listeners for turning
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")

# Start listening for events
screen.listen()

# Start the automatic movement
update_position()

# Keep the window open
screen.mainloop()
