#pong
import turtle

#screen
win = turtle.Screen()
win.title('Pong ')
win.bgcolor('green')
win.setup(width=800, height=600)
win.tracer(0)



#paddle1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape('square')
pad1.color('red')
pad1.penup()
pad1.shapesize(stretch_wid=5 ,stretch_len=1)
pad1.goto(-350,0)

pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape('square')
pad2.color('yellow')
pad2.penup()
pad2.shapesize(stretch_wid=5 ,stretch_len=1)
pad2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')  
ball.penup()
ball.shapesize(stretch_wid=2 ,stretch_len=2)
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color('green')
pen.hideturtle()
pen.goto(0, 260)

#function for pad1
def pad1up():
    y = pad1.ycor()
    y += 20
    pad1.sety(y)
    
def pad1down():
    y = pad1.ycor()
    y -= 20
    pad1.sety(y)
    
#func for pad2
def pad2up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)
    
def pad2down():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)
    

    
#bind for pad 1
win.listen()
win.onkeypress(pad1up, 'w')

win.listen()
win.onkeypress(pad1down, 's')

#bind for pad 2
win.listen()
win.onkeypress(pad2up, 'Up')

win.listen()
win.onkeypress(pad2down, 'Down')

while True:
    win.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # 290 because the height is 600 so 300 and -300 and ball is 20 by 20
    if ball.ycor() > 290:
        ball.sety(290)
        #reverse direction
        ball.dy*= -1
        
    if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy*= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() <- 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    #hitting
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() < -350 and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        
        
    #Leader board

        
        
    



