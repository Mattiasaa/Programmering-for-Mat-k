import turtle
bob = turtle.Turtle()
print(bob)

def draw_square(turtle, size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)
        
def draw_polygon(turtle, size, edges):
    angle = 360 / edges
    for i in range(edges):
        turtle.fd(size)
        turtle.lt(angle)

# draw_square(bob, 100)
draw_polygon(bob, 1, 360)

turtle.mainloop()