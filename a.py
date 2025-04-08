import turtle
import random
import math
import time


def ultimate_crazy_art():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("The Ultimate Crazy Art Show")

    # Create multiple turtles (now 10!)
    artists = [turtle.Turtle() for _ in range(10)]
    for artist in artists:
        artist.speed(0)
        artist.width(random.randint(1, 5))
        artist.penup()
        artist.goto(random.randint(-400, 400), random.randint(-400, 400))
        artist.pendown()

    # Random color generator
    def random_color():
        return (random.random(), random.random(), random.random())

    screen.colormode(1.0)

    # Draw shapes with variety and randomness
    def draw_shapes(artist, step):
        sides = random.randint(3, 12)  # Random polygons
        angle = 360 / sides
        size = random.randint(20, 100) + step // 10

        for _ in range(sides):
            artist.color(random_color())
            artist.forward(size)
            artist.left(angle)

    # Draw spirals
    def draw_spiral(artist, step):
        for _ in range(36):
            artist.color(random_color())
            artist.circle(50 + step // 20, 10)

    # Starburst pattern
    def draw_starburst(artist):
        for _ in range(random.randint(8, 20)):
            artist.color(random_color())
            artist.forward(random.randint(50, 150))
            artist.backward(random.randint(50, 150))
            artist.right(360 / random.randint(8, 20))

    # Draw long-loop patterns
    for step in range(1500):  # Longer runtime!
        for artist in artists:
            artist.color(random_color())
            artist.forward(random.randint(20, 60))
            artist.right(random.choice([30, 45, 60, 90, 120, random.randint(10, 360)]))

            if step % 100 == 0:
                draw_shapes(artist, step)  # Add random polygons

            if step % 200 == 0:
                draw_spiral(artist, step)  # Add spirals

            if step % 300 == 0:
                draw_starburst(artist)  # Add starbursts

            # Occasionally reset the position for more randomness
            if step % random.randint(150, 250) == 0:
                artist.penup()
                artist.goto(random.randint(-400, 400), random.randint(-400, 400))
                artist.pendown()

    # Grand finale: All turtles create a firework explosion
    time.sleep(1)
    for artist in artists:
        artist.speed(8)
        for _ in range(36):
            artist.color(random_color())
            artist.goto(random.randint(-400, 400), random.randint(-400, 400))
            artist.dot(random.randint(10, 30))  # Firework dots

    turtle.done()


ultimate_crazy_art()
