# To use this, first save the file. Remember the directory that you saved
# it in. Then, open python interactive mode, where you see the '>>>'. If
# you are running windows, that means running 'python idle', and on mac it
# means opening the terminal and typing 'python3'. Then import the file.
# If the file is in a folder named 'my_project', and *that* folder is on
# the desktop, then it will look like this:
# 
# >>> import Desktop.my_project.our_turtle
# 
# **Make sure you are using the correct directory names, not just mine**
# 
# Now you can run the function by referencing the directory, then the file, 
# then the function in the file. In my example, the directories are
# 'Desktop' and 'my_project', the file is 'our_turtle', and the function
# is 'move_and_turn()'
# 
# >>> Desktop.my_project.our_turtle.move_and_turn(100, 45)
# >>> Desktop.my_project.our_turtle.move_and_turn(100, 45)

import turtle

my_turtle = turtle.Turtle()

def move_and_turn(move, turn):
    my_turtle.forward(move)
    my_turtle.right(turn)
