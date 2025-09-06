import turtle
import time
import colorsys

# --- Setup the screen ---
screen = turtle.Screen()
screen.title("Digital Pookalam")
screen.bgcolor("white")
screen.setup(width=800, height=800)

# --- Create a turtle object ---
t = turtle.Turtle()
t.speed(0) # Set the fastest drawing speed

# --- Function to draw a spirograph-like petal pattern ---
def draw_spiro_petals(t, size, repeat, start_angle):
    for i in range(repeat):
        t.circle(size)
        t.right(360 / repeat)

# --- Function to draw a filled flower petal ---
def draw_petal(t, size, color):
    t.color(color)
    t.begin_fill()
    t.circle(size, 30)
    t.left(120)
    t.circle(size, 30)
    t.end_fill()




r = 285
t.pensize(10)
t.pencolor("maroon")
t.penup()
t.home()

t.sety(-r)
t.pendown()
t.circle(r)
t.penup()
t.pensize(1)

# --- Draw the main layers of the Pookalam ---

# Layer 1: Outermost circle with spiral pattern
t.penup()
t.goto(0, -280)
t.pendown()
t.color("orange")
t.width(5)
t.begin_fill()
t.circle(280)
t.end_fill()





# Layer 2: Repeating circular petals
num_petals = 39
for i in range(num_petals):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_petals))
    t.forward(220)
    t.pendown()
    draw_petal(t, 120, "red")



# Layer 4: Smaller repeating petals
num_petals_small = 39
for i in range(num_petals_small):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_petals_small) + 11.25) # Offset to fill gaps
    t.forward(180)
    t.pendown()
    draw_petal(t, 80, "purple")




r = 230
t.pensize(18)
t.pencolor("white")
t.penup()
t.home()
t.sety(-r)
t.pendown()
t.circle(r)
t.penup()
t.pensize(1)





r = 180
t.pensize(15)
t.pencolor("green")
t.penup()
t.home()
t.sety(-r)
t.pendown()
t.circle(r)
t.penup()
t.pensize(1)





    


# Layer 5: Colorful mandala-like inner spiral
t.penup()
t.goto(0, 0)
t.pendown()
t.width(2)
num_colors = 12
for i in range(360):
    t.pencolor(colorsys.hsv_to_rgb(i / 360, 0.9, 0.9))
    t.circle(120 - i * 0.3, 90)
    t.left(90)
    t.circle(120 - i * 0.3, 90)
    t.left(10)



# --- Hide the turtle and display the result ---
t.hideturtle()
time.sleep(10) # Keeps the window open longer
turtle.done()
