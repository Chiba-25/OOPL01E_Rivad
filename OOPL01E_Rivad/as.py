import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball Animation")
screen.setup(width=800, height=600)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("lime")
ball.penup()
ball.speed(0)
ball.goto(0, 0)

# Ball speed and direction
ball.dx = 3  # Change in x
ball.dy = 3  # Change in y

# Create the boundary
boundary = turtle.Turtle()
boundary.color("white")
boundary.penup()
boundary.goto(-390, -290)
boundary.pendown()
boundary.pensize(3)
for _ in range(2):
    boundary.forward(780)
    boundary.left(90)
    boundary.forward(580)
    boundary.left(90)
boundary.hideturtle()

# Animation loop
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with walls
    if ball.xcor() > 380 or ball.xcor() < -380:  # Right and left walls
        ball.dx *= -1  # Reverse direction
    if ball.ycor() > 280 or ball.ycor() < -280:  # Top and bottom walls
        ball.dy *= -1  # Reverse direction

    time.sleep(0.01)  # Pause for smoother animation
