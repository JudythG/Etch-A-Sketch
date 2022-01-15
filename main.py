from turtle import Turtle, Screen

TURN_ANGLE = 10
MOVE_LEN = 10


def move_forward():
    turtle.forward(MOVE_LEN)


def move_backward():
    turtle.backward(MOVE_LEN)


def move_counterclockwise():
    turtle.left(TURN_ANGLE)


def move_clockwise():
    turtle.right(TURN_ANGLE)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle = Turtle()
turtle.pensize(3)
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()