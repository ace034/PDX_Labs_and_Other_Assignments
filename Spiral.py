import turtle
my_spiral = turtle.Turtle()
def spiral(distance, angle, boot):
    g = distance
    while g >= 0:
        my_spiral.forward(g)
        my_spiral.right (angle)
        g = g - boot

def loop_shape(sides, angle, distance):
    for i in range(0, 360):
        for j in range(0, sides):
            my_spiral.right(angle):
            my_spiral.forward(distance)
        my_spiral.right(1)
        my_spiral.forward(1)
