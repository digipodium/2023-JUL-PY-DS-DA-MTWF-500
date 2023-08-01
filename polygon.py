from turtle import *

# define a function
def hexagon():
    for i in range(6):
        fd(100)
        lt(360/6)

# call the function
hexagon()
penup()
goto(100,100)
pendown()
hexagon()
penup()
goto(-100,100)
pendown()
hexagon()
penup()
goto(-100,-100)
pendown()
hexagon()
penup()
goto(100,-100)
pendown()
hexagon()
hideturtle()
mainloop()