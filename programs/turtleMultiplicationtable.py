import turtle
# Create a turtle object
pen = turtle.Turtle()
# pen.speed(0)  # Set the drawing speed to fastest

# Function to write text at a given position
def write_text(x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(text)

# Function to draw the multiplication table
def draw_table(rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            # Calculate position
            x = -200 + j * 40
            y = 200 - i * 20
            pen.color("red")
            write_text(x + 10, y - 10, str(i * j))
draw_table(10, 10)

turtle.mainloop()
