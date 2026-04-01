import turtle
turtle.speed(5)
turtle.pensize(3)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()

turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.pendown()

turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()

turtle.left(90)
turtle.forward(113)
turtle.right(90)
turtle.pendown()

turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.done()
