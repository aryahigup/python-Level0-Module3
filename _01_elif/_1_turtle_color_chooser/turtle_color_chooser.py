import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    t = turtle.Turtle()
    loop = 1
    while loop == 1:
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
        for i in range(4):
            t.forward(100)
            t.right(90)
        #      3) Set the pen width to 10
        t.pensize(10)
        #      4) Ask the user what color pen they would like to draw with
        color = simpledialog.askstring(title='Color Chooser', prompt='What color would you like')
        #      5) Use an if/else statement to set the pen color that the user
        #         requested
        if color == 'blue':
            t.pencolor('blue')
        elif color == 'red':
            t.pencolor('red')
        elif color == 'yellow':
            t.pencolor('yellow')
        elif color == 'purple':
            t.pencolor('purple')
        else:
            t.pencolor('black')
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
