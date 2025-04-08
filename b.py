import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.title("Dynamic Cityscape")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)

# Function to draw a rectangle (used for buildings and windows)
def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw windows on a building, now blinking
def draw_windows(x, y, width, height, rows, columns):
    window_width = width / columns
    window_height = height / rows
    for i in range(rows):
        for j in range(columns):
            window_x = x + j * window_width
            window_y = y + i * window_height
            draw_rectangle(window_x, window_y, window_width - 5, window_height - 5, "yellow")
            time.sleep(0.05)
            draw_rectangle(window_x, window_y, window_width - 5, window_height - 5, "black")

# Function to draw a road with cars
def draw_road():
    # Road background
    draw_rectangle(-300, -250, 600, 50, "gray")
    # Road stripes
    for i in range(-300, 300, 40):
        draw_rectangle(i, -225, 30, 5, "white")
    # Draw cars
    car = turtle.Turtle()
    car.speed(2)
    car.shape("square")
    car.color("red")
    car.penup()
    for _ in range(5):
        car.goto(-300, -230)
        for i in range(-300, 300, 20):
            car.goto(i, -230)

# Function to draw stars in the sky
def draw_star(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(10)
        pen.left(144)
    pen.end_fill()

# Draw the ground
pen.penup()
pen.goto(-300, -200)
pen.pendown()
pen.color("green")
pen.begin_fill()
pen.forward(600)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(600)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.end_fill()

# Draw the road with cars
draw_road()

# Draw buildings with blinking windows
draw_rectangle(-250, -200, 100, 300, "gray")
draw_windows(-250, -200, 100, 300, 5, 3)

draw_rectangle(-100, -200, 100, 200, "lightgray")
draw_windows(-100, -200, 100, 200, 4, 3)

draw_rectangle(50, -200, 100, 250, "darkgray")
draw_windows(50, -200, 100, 250, 5, 2)

draw_rectangle(200, -200, 100, 150, "silver")
draw_windows(200, -200, 100, 150, 3, 2)

# Draw the moon and stars
pen.penup()
pen.goto(200, 150)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

for i in range(-250, 250, 50):
    draw_star(i, 200)

# Hide the turtle
pen.hideturtle()

# Keep the screen open
screen.mainloop()
