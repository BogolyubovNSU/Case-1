# Case-study #1
# Developers: Bogolyubov I., Pisarenko D.
#

import turtle

t = turtle.Turtle()
turtle.setup(width=1200, height=1000)


"""
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
"""


def polyhedron(vertices, color):
    """
    Function, drawing polyhedron.
    :param vertices: a list consisting of the coordinates of the polyhedron's vertices;
                     the function will traverse the vertices one by one
    :param color: fill color
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


def title(x, y, text):
    """
    Function, drawing title.
    :param x: the x coordinate of the title center
    :param y: the y coordinate of the title center
    :param text: the text of the title
    :return: None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, align='center', font=('Times New Roman', 20, 'bold'))
    t.penup()


def ratio(k, a, b, vertices):
    """
    Function, adjusts the coordinate values to the specified values.
    :param k: the coefficient that multiplies the x and y coordinates
    :param a: a value that is added to the x coordinate
    :param b: a value that is added to the y coordinate
    :param vertices: a list containing the initial coordinates of the polyhedron's vertices
    :return: a list containing the adjusted coordinates of the polyhedron's vertices
    """
    result = []
    for vertex in vertices:
        result.append((vertex[0] * k + a, vertex[1] * k + b))
    return result


def tengram(stop):
    """
    Function, drawing tengram.
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    :return: None
    """
    polyhedron([(0, 0), (-150, 150), (150, 150)], '#F72A49')
    polyhedron([(0, 0), (150, 150), (150, -150)], '#FEDD14')
    polyhedron([(0, 0), (-75, 75), (-75, -75)], '#4FBAE8')
    polyhedron([(0, 0), (-75, -75), (0, -150), (75, -75)], '#FF7C00')
    polyhedron([(-150, 150), (-150, 0), (-75, -75), (-75, 75)], '#8ECC23')
    polyhedron([(0, -150), (150, -150), (75, -75)], '#FBBF9B')
    polyhedron([(-150, 0), (-150, -75), (-75, -75)], '#EF66E8')
    polyhedron([(-150, -150), (-75, -150), (-75, -75), (-150, -75)], '#3755A4')
    polyhedron([(-75, -75), (-75, -150), (0, -150)], '#A250E2')
    title(0, -200, 'TENGRAM PUZZLE')
    if stop==1:
        turtle.done()


def jet(stop):
    """
    Function, drawing jet.
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    :return: None
    """
    polyhedron(ratio(0.5, -225, 175, [(-375, 325), (-525, 475), (-225, 475)]), '#4FBAE8')
    polyhedron(ratio(0.5, -225, 175, [(-375, 325), (-525, 325), (-450, 400)]), '#FEDD14')
    polyhedron(ratio(0.5, -225, 175, [(-375, 325), (-225, 325), (-225, 175)]), '#FF7C00')
    polyhedron(ratio(0.5, -225, 175, [(-375, 325), (-225, 325), (-150, 400), (-300, 400)]), '#FEDD14')
    polyhedron(ratio(0.5, -225, 175, [(-450, 400), (-525, 475), (-600, 400), (-525, 325)]), '#F72A49')
    polyhedron(ratio(0.5, -225, 175, [(-300, 400), (-88, 400), (-88, 612)]), '#A250E2')
    polyhedron(ratio(0.5, -225, 175, [(-375, 550), (-450, 475), (-300, 475)]), '#FBBF9B')
    title(-412.5, 237.5, 'JET')
    if stop==1:
        turtle.done()


def mountains(stop):
    """
    Function, drawing mountains.
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    :return: None
    """
    polyhedron(ratio(0.6, 175, 175, [(375, 325), (450, 400), (450, 250)]), '#3755A4')
    polyhedron(ratio(0.6, 175, 175, [(375, 325), (450, 250), (375, 250)]), '#4FBAE8')
    polyhedron(ratio(0.6, 175, 175, [(375, 325), (425, 375), (375, 396), (325, 375)]), '#8ECC23')
    polyhedron(ratio(0.6, 175, 175, [(375, 325), (375, 250), (300, 325), (300, 400)]), '#FF7C00')
    polyhedron(ratio(0.6, 175, 175, [(375, 250), (300, 250), (300, 325)]), '#A250E2')
    polyhedron(ratio(0.6, 175, 175, [(300, 250), (300, 400), (150, 250)]), '#F72A49')
    polyhedron(ratio(0.6, 175, 175, [(450, 250), (450, 400), (600, 250)]), '#FEDD14')
    title(400, 237.5, 'MOUNTAINS')
    if stop == 1:
        turtle.done()


def picture3():
    pass


def picture4():
    pass


def main():
    tengram(0)
    jet(0)
    mountains(1)

if __name__ == '__main__':
    main()
