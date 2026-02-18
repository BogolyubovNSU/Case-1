# Case-study #1
# Developers: Bogolyubov I., Pisarenko D.
#

import turtle

type Point = tuple[float, float]

t = turtle.Turtle()
turtle.setup(width=1200, height=1000)
turtle.tracer(0)


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


def polyhedron(vertices: list[Point], color: str, stop: int = 0) -> None:
    """
    Function, drawing polyhedron.

    :param vertices: a list consisting of the coordinates of the polyhedron's
    vertices. The function will traverse the vertices one by one
    :param color: fill color
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(vertices[0])
    t.pendown()

    for vertex in vertices[1:] + [vertices[0]]:
        t.goto(vertex)

    t.end_fill()
    t.penup()

    if stop:
        turtle.done()


def title(x: float, y: float, text: str, stop: int = 0) -> None:
    """
    Function, drawing title.

    :param x: the x coordinate of the title center
    :param y: the y coordinate of the title center
    :param text: the text of the title
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, align='center', font=('Times New Roman', 20, 'bold'))
    t.penup()

    if stop:
        turtle.done()


def ratio(coefficients: list[float], vertices: list[Point]) -> list[Point]:
    """
    Function, adjusts the coordinate values to the specified values.

    :param coefficients: a list consisting of three elements:
    1) the coefficient that multiplies the x and y coordinates
    2) a value that is added to the x coordinate
    3) a value that is added to the y coordinate
    :param vertices: a list containing the initial coordinates
    of the polyhedron's vertices

    :return: a list containing the adjusted coordinates
    of the polyhedron's vertices
    """
    result = []

    for vertex in vertices:
        result.append((vertex[0] * coefficients[0] + coefficients[1],
                       vertex[1] * coefficients[0] + coefficients[2]))

    return result


def tengram(stop: int = 0) -> None:
    """
    Function, drawing tengram.

    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

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

    if stop:
        turtle.done()


def jet(stop: int = 0) -> None:
    """
    Function, drawing jet.

    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    cfc = [0.5, -225, 175]

    polyhedron(ratio(cfc, [(-375, 325), (-525, 475), (-225, 475)]), '#4FBAE8')
    polyhedron(ratio(cfc, [(-375, 325), (-525, 325), (-450, 400)]), '#8ECC23')
    polyhedron(ratio(cfc, [(-375, 325), (-225, 325), (-225, 175)]), '#FF7C00')
    polyhedron(ratio(cfc, [(-300, 400), (-88, 400), (-88, 612)]), '#A250E2')
    polyhedron(ratio(cfc, [(-375, 550), (-450, 475), (-300, 475)]), '#FBBF9B')

    polyhedron(
        ratio(cfc, [(-375, 325), (-225, 325), (-150, 400), (-300, 400)]),
        '#FEDD14')
    polyhedron(
        ratio(cfc, [(-450, 400), (-525, 475), (-600, 400), (-525, 325)]),
        '#F72A49')

    title(-412.5, 237.5, 'JET')

    if stop:
        turtle.done()


def mountains(stop: int = 0) -> None:
    """
    Function, drawing mountains.

    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    cfc = [0.6, 175, 175]

    polyhedron(ratio(cfc, [(375, 325), (450, 400), (450, 250)]), '#3755A4')
    polyhedron(ratio(cfc, [(375, 325), (450, 250), (375, 250)]), '#4FBAE8')
    polyhedron(ratio(cfc, [(375, 250), (300, 250), (300, 325)]), '#A250E2')
    polyhedron(ratio(cfc, [(300, 250), (300, 400), (150, 250)]), '#F72A49')
    polyhedron(ratio(cfc, [(450, 250), (450, 400), (600, 250)]), '#FEDD14')

    polyhedron(ratio(cfc, [(375, 325), (425, 375), (375, 425), (325, 375)]),
               '#8ECC23')
    polyhedron(ratio(cfc, [(375, 325), (375, 250), (300, 325), (300, 400)]),
               '#FF7C00')

    title(400, 237.5, 'MOUNTAINS')

    if stop:
        turtle.done()


def table(stop: int = 0) -> None:
    """
    Function, drawing table.

    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    cfc = [1 ,50 , 100]

    polyhedron(ratio(cfc, [(-425, -425), (-425,-475), (-375, -425)]), '#4FBAE8')
    polyhedron(ratio(cfc, [(-425, -475), (-425, -375), (-525, -375)]), '#8ECC23')
    polyhedron(ratio(cfc, [(-575, -375), (-575, -425), (-525,-425)]), '#3755A4')
    polyhedron(ratio(cfc, [(-575, -425), (-475, -425), (-525, -475)]), '#FBBF9B')
    polyhedron(ratio(cfc, [(-475, -425), (-550, -500), (-400,-500)]), '#F72A49')

    polyhedron(
        ratio(cfc, [(-525, -375), (-575, -375), (-525, -425), (-475, -425)]),
        '#FEDD14')
    polyhedron(
        ratio(cfc, [(-375, -375), (-375, -425), (-425, -425,), (-425, -375)]),
        '#EF66E8')

    title(-425, -437.5, 'TABLE')

    if stop:
        turtle.done()


def airplane(stop: int = 0) -> None:
    """
    Function, drawing airplane.

    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    cfc = [1.1 ,50 , 100]

    polyhedron(ratio(cfc, [(200, -375), (250, -375), (250, -425)]), '#4FBAE8')
    polyhedron(ratio(cfc, [(250, -415), (300, -415), (300, -385)]), '#3755A4')
    polyhedron(ratio(cfc, [(250, -415), (250, -385), (300, -385)]), '#F72A49')
    polyhedron(ratio(cfc, [(330, -400), (330, -350), (380, -400)]), '#FEDD14')
    polyhedron(ratio(cfc, [(330, -400), (330, -450), (380, -400)]), '#8ECC23')

    polyhedron(
        ratio(cfc, [(380, -400), (355, -375), (400, -375), (425, -400)]),
        '#FF7C00')
    polyhedron(
        ratio(cfc, [(300, -385), (330, -385), (330, -415), (300, -415)]),
        '#A250E2')

    title(387.5, -437.5, 'AIRPLANE')

    if stop:
        turtle.done()


def main(stop: int = 0) -> None:
    """
    Main function.

    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    tengram()
    jet()
    mountains()
    table()
    airplane()
    turtle.update()

    if stop:
        turtle.done()


if __name__ == '__main__':
    main(1)
