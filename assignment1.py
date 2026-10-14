import turtle
import easygui


def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def draw_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


def draw_concentric_circles(t, radius, color):
    for r in range(radius, 0, -20):
        t.penup()
        t.goto(0, -r)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()


def draw_star(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def main():
    shape = easygui.buttonbox(
        "Choose a shape to draw:",
        "Geometric Pattern Studio",
        ["Square", "Equilateral Triangle",
         "Concentric Circles", "Custom Star"]
    )

    if not shape:
        return

    dimension = easygui.integerbox(
        "Enter dimension/radius (50-250):",
        "Shape Dimension",
        lowerbound=50,
        upperbound=250
    )

    if dimension is None:
        return

    color = easygui.enterbox(
        "Enter fill color:",
        "Fill Color",
        "blue"
    )

    if not color:
        return

    screen = turtle.Screen()
    screen.title("Geometric Pattern Studio")

    t = turtle.Turtle()
    t.speed(5)

    if shape == "Square":
        t.penup()
        t.goto(-dimension / 2, dimension / 2)
        t.pendown()
        draw_square(t, dimension, color)

    elif shape == "Equilateral Triangle":
        t.penup()
        t.goto(-dimension / 2, -dimension / 3)
        t.pendown()
        draw_triangle(t, dimension, color)

    elif shape == "Concentric Circles":
        draw_concentric_circles(t, dimension, color)

    elif shape == "Custom Star":
        t.penup()
        t.goto(0, dimension / 2)
        t.setheading(0)
        t.pendown()
        draw_star(t, dimension, color)

    t.hideturtle()
    easygui.msgbox("Drawing completed successfully!", "Completed")
    turtle.bye()


if __name__ == "__main__":
    main()
