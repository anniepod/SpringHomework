#Question 1
"""
Add some new key bindings to the first sample program:

    -Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
    -Pressing keys + or - should increase or decrease the width of tess’ pen.
        Ensure that the pen size stays between 1 and 20 (inclusive).
    -Handle some other keys to change some attributes of tess, or attributes
    of the window, or to give her new behaviour that can be controlled from the keyboard."""


""" 
import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()    # Create our favorite turtle



# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()

def h5():
    tess.color("red")

def h6():
    tess.color("green")

def h7():
    tess.color("blue")

sz = 1

def h8():
    global sz
    sz +=  1
    if sz > 20:
        sz = 20
    tess.pensize(sz)

def h9():
    global sz
    sz -= 1
    if sz<1:
        sz=1

def h10():
    tess.circle(20)

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(h8, "=")
wn.onkey(h9, "-")
wn.onkey(h10, "c")

wn.listen()
wn.mainloop()
"""



#Question 3


import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
bobgreen = turtle.Turtle()
boborange= turtle.Turtle()
bobred = turtle.Turtle()

def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

def green()
    bobgreen.forward(40)
    bobgreen.left(90)
    bobgreen.forward(50)
    bobgreen.shape("circle")
    bobgreen.shapesize(3)
    bobgreen.fillcolor("green")
    bobgreen.penup()


def orange()
    boborange.forward(40)
    boborange.left(90)
    boborange.forward(120)
    boborange.shape("circle")
    boborange.shapesize(3)
    boborange.fillcolor("orange")

def red()
    bobred.forward(40)
    bobred.left(90)
    bobred.forward(190)
    bobred.shape("circle")
    bobred.shapesize(3)
    bobred.fillcolor("red")


tess.penup()
tess.forward(-150)

draw_housing()

tess.penup()

# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()