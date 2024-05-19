# Use the “turtle” module to draw concentric circles with different colours.
import turtle
import introJitendra
introJitendra.printIntro("Use the “turtle” module to draw concentric circles with different colours.")

colors = ['red', 'green', 'blue', 'orange', 'purple']
turtle.pensize(4)

for i in range(5):
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(0, -i * 20)
    turtle.pendown()
    turtle.circle(20 + i * 20)

turtle.done()
