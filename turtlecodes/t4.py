from turtle import *

speed('fastest')
pensize(2)
bgcolor('black')
pencolor('white')
colors = ['red', 'pink', 'blue', 'green', 'orange', 'purple']
side = 6
for i in range(side):
    fd(200)
    for i in range(side):
        fd(100)
        begin_fill()
        fillcolor(colors[i%6])
        lt(360/side)
        for i in range(side):
            fd(50)
            for i in range(side):
                fd(25)
                lt(360/side)
            lt(360/side)
        end_fill()
        dot(10, 'white')
    lt(360/side)

hideturtle()
mainloop()