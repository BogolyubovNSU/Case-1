import turtle


t = turtle.Turtle()
turtle.setup(width=1200, height=1000)


def triangle(vertices,color,v):
    t.speed(10)
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    t.goto(vertices[1])
    t.goto(vertices[2])
    t.goto(vertices[0])
    t.end_fill()
    t.setheading(90)
    if v==1:
        turtle.done()


def square(x,y,a,color,v):
    t.speed(10)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.end_fill()
    t.setheading(90)
    if v==1:
        turtle.done()


def rhombus(x,y,a,angle0,angle1,angle2,color,v):
    t.speed(10)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(angle0)
    t.forward(a)
    t.right(angle1)
    t.forward(a)
    t.right(angle2)
    t.forward(a)
    t.right(angle1)
    t.forward(a)
    t.end_fill()
    t.setheading(90)
    if v==1:
        turtle.done()


def parallelogram(x,y,a1,a2,angle,color,v):
    t.speed(10)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(a1)
    t.left(180-angle)
    t.forward(a2)
    t.left(angle)
    t.forward(a1)
    t.left(180-angle)
    t.forward(a2)
    t.end_fill()
    t.setheading(90)
    if v==1:
        turtle.done()


def general_tengram():
    triangle([(0, 0), (50 * (2 ** 0.5), 0), (25 * (2 ** 0.5), 25 * (2 ** 0.5))], 'pink',0)
    rhombus(25*(2**0.5),25*(2**0.5),50,45,90,90,'blue',0)
    triangle([(50 * (2 ** 0.5), 0),(100*2**0.5,0),(100*2**0.5,50*2**0.5)],'yellow',0)
    triangle([(0,0),(50*2**0.5,50*2**0.5),(0,100*2**0.5)],'darkorchid1',0)
    triangle([(0,100*2**0.5),(100*2**0.5,100*2**0.5),(50*2**0.5,50*2**0.5)],'lightblue',0)
    triangle([(50*2**0.5,50*2**0.5),(75*2**0.5,75*2**0.5),(75*2**0.5,25*2**0.5)],'darkolivegreen1',0)
    parallelogramm((100*2**0.5),(50*2**0.5),(50*2**0.5),50,45,'lightyellow',1)


def picture1():
    pass


def picture2():
    pass


def picture3():
    pass


def picture4():
    pass


def picture5():
    pass


def picture6():
    pass


def picture7():
    pass


def picture8():
    pass

def main():
    pass

main()
