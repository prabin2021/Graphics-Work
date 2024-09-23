import turtle


screen = turtle.Screen()
screen.bgcolor("white")


t = turtle.Turtle()
t.speed(0)  

colors = ["red", "purple", "blue", "green", "yellow", "orange"]


for i in range(360):
    t.pencolor(colors[i % 6])  
    t.width(i // 100 + 1)  
    t.forward(i)
    t.left(59)  

t.hideturtle()
turtle.done()
