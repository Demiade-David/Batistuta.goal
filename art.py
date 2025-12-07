
import turtle

# Setup screen at module scope so it's available when mainloop is called
screen = turtle.Screen()
screen.setup(width=600, height=600)


def draw_branch(t, length, angle):
    if length < 5:
        return # Stop condition

    t.forward(length)
    t.right(angle)

    # Recursive call for the first branch
    draw_branch(t, length * 0.7, angle) 

    t.left(angle * 2)

    # Recursive call for the second branch
    draw_branch(t, length * 0.7, angle)

    t.right(angle)
    t.backward(length)

# Setup and call
t = turtle.Turtle()
t.left(90)
t.speed(0)

draw_branch(t, 100, 20)
t.hideturtle()
screen.mainloop()

# import turtle
# import random

# # Setup the screen
# screen = turtle.Screen()
# screen.setup(width=700, height=700)
# screen.bgcolor("black")
# screen.title("Kaleidoscope Starburst")
# screen.tracer(0)

# # Setup the turtle
# t = turtle.Turtle()
# t.speed(1)
# t.hideturtle()

# # Function to draw a single "petal" of the starburst
# def draw_petal(t, size, color):
#     t.pencolor(color)
#     t.fillcolor(color)
#     t.begin_fill()
#     for _ in range(3): # Draw a triangle
#         t.forward(size)
#         t.left(120)
#     t.end_fill()

# colors = ["#8A2BE2", "#4B0082", "#9400D3", "#BA55D3", "#DA70D6", "#FF00FF", "#EE82EE"] # Violets and Magentas

# num_petals = 36 # Number of shapes to draw around the center
# angle = 360 / num_petals

# for i in range(num_petals):
#     t.penup()
#     t.goto(0,0) # Always start from the center
#     t.pendown()
#     t.setheading(i * angle) # Set orientation
    
#     # Choose a color from the list, cycling through them
#     current_color = colors[i % len(colors)]
    
#     # Draw the petal slightly away from the center
#     t.forward(20) 
#     draw_petal(t, 100, current_color)
    
# screen.update()
# screen.mainloop()


