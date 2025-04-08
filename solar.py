import turtle
import math
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System with Traveling Spaceship")

# Create the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)


# Function to create a planet
def create_planet(color, size, distance, name):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.goto(distance, 0)
    planet.name = name  # Adding a name attribute to each planet
    return planet


# Function to simulate orbital motion
def orbit(planet, distance, angle):
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    planet.goto(x, y)


# Function to draw stars
def draw_stars(num_stars):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    for _ in range(num_stars):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        star.goto(x, y)
        star.dot(random.randint(2, 4))  # Stars with varying sizes


# Create planets
planets = [
    create_planet("gray", 0.3, 50, "Mercury"),
    create_planet("orange", 0.6, 80, "Venus"),
    create_planet("blue", 0.7, 110, "Earth"),
    create_planet("red", 0.5, 150, "Mars"),
    create_planet("brown", 1.2, 200, "Jupiter"),
    create_planet("gold", 1.0, 250, "Saturn"),
    create_planet("lightblue", 0.8, 300, "Uranus"),
    create_planet("purple", 0.8, 350, "Neptune")
]

# Create the spaceship
spaceship = turtle.Turtle()
spaceship.shape("triangle")
spaceship.color("white")
spaceship.shapesize(1)
spaceship.penup()

# Draw stars in the background
draw_stars(100)

# Simulate the Solar System with a traveling spaceship
angle = 0
planet_index = 0  # Track which planet the spaceship is traveling towards
while True:
    for i, planet in enumerate(planets):
        orbit(planet, (i + 1) * 50, angle * (1 / (i + 1)))  # Slow down outer orbits

    # Travel towards the next planet
    target_planet = planets[planet_index]
    spaceship.setheading(spaceship.towards(target_planet.xcor(), target_planet.ycor()))
    spaceship.forward(2)

    # Check if the spaceship has reached the target planet
    if spaceship.distance(target_planet) < 10:
        planet_index = (planet_index + 1) % len(planets)  # Move to the next planet

    angle += 1
    time.sleep(0.02)  # Adjust speed for smooth motion
