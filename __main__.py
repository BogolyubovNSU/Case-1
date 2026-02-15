# Case-study #1
# Developers: Bogolyubov I., Pisarenko D.
#

import turtle

t = turtle.Turtle()
turtle.setup(width=1200, height=1000)


def polyhedron(vertices,color,stop):
    """
    Function, drawing polyhedron.
    :param vertices: a list consisting of the coordinates of the polyhedron's vertices;
                     the function will traverse the vertices one by one
    :param color: fill color
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    :return: None
    """
    t.speed(10)
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    for vertex in vertices[1:] + [vertices[0]]:
        t.goto(vertex)
    t.end_fill()
    t.penup()
    if stop==1:
        turtle.done()


def tengram():
    """
    Function, drawing tengram.
    Summary of colors:
    RED - #F72A49
    YELLOW - #FEDD14
    PINK - #EF66E8
    ORANGE - #FF7C00
    LIGHT ORANGE - #FBBF9B
    GREEN - #8ECC23
    VIOLET - #A250E2
    BLUE - #4FBAE8
    DARK BLUE - #3755A4
    :return: None
    """
    polyhedron([(0, 0), (-150, 150), (150, 150)], '#F72A49', 0)
    polyhedron([(0, 0), (150, 150), (150, -150)], '#FEDD14', 0)
    polyhedron([(0, 0), (-75, 75), (-75, -75)], '#4FBAE8', 0)
    polyhedron([(0, 0), (-75, -75), (0, -150), (75, -75)], '#FF7C00', 0)
    polyhedron([(-150, 150), (-150, 0), (-75, -75), (-75, 75)], '#8ECC23', 0)
    polyhedron([(0, -150), (150, -150), (75, -75)], '#FBBF9B', 0)
    polyhedron([(-150, 0), (-150, -75), (-75, -75)], '#EF66E8', 0)
    polyhedron([(-150, -150), (-75, -150), (-75, -75), (-150, -75)], '#3755A4', 0)
    polyhedron([(-75, -75), (-75, -150), (0, -150)], '#A250E2', 1)


def picture1():
    pass


def picture2():
    pass


def picture3():
    pass


def picture4():
    pass


def main():
    pass

if __name__ == '__main__':
    main()
