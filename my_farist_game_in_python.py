import turtle

wind=turtle.Screen()#intialize screen
wind.title("my game")#title for my screen
wind.bgcolor("black")#color for my screen
wind.setup(width=800, height=600)#set the width and height for the window
wind.tracer(0)#stops the window from updating automatically

#shot 1
    
shot1 = turtle.Turtle()
shot1.speed(0)
shot1.shape("square")
shot1.color("blue")
shot1.shapesize(stretch_wid=5,stretch_len=1)
shot1.penup()
shot1.goto(-350,0)

#shot2

shot2 = turtle.Turtle()#intializes turtle object(shape)
shot2.speed(0)#set the speed
shot2.shape("square")#set the shape of object
shot2.color("red")
shot2.shapesize(stretch_wid=5,stretch_len=1)#set the shape size
shot2.penup()#stops the opject from the drawing lins
shot2.goto(350,0)#set the position

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5


#score
score1=0
score2=0
score=turtle.Turtle()
score.speed()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)


#functions
#
def shot1_up():
    y=shot1.ycor()#get the y coodinate of the shot1
    y+=20
    shot1.sety(y)#set the y of shot1 to the new y coordinate
#    
def shot1_down():
    y=shot1.ycor()
    y-=20
    y=shot1.sety(y)

def shot2_up():
    y=shot2.ycor()
    y+=20
    shot2.sety(y)
#    
def shot2_down():
    y=shot2.ycor()
    y-=20
    y=shot2.sety(y)
            

#keyboard bindings
    
wind.listen()#tall the window to expect keybord input

wind.onkeypress(shot1_up,"w") 

wind.onkeypress(shot1_down,"s")

wind.onkeypress(shot2_up,"Up") 

wind.onkeypress(shot2_down,"Down")


#main game loop .
while True:
    wind.update()#updates the screen everytime loop run.
    #move the ball
    ball.setx(ball.xcor()+ball.dx)#ball start in 0 and everytime loop run go 2px in x
    ball.sety(ball.ycor()+ball.dy)#ball start in 0 and everytime loop run go 2px in y
    #border check ,top border +300px , bottm border -300px . ball is 20px
    if ball.ycor() >290: #if ball is at top border
        ball.sety(290)#set y coordinate +290
        ball.dy *=-1#reverse direction , making +.5--->-0.5
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1,score2), align="center" , font=("Courier",24,"normal"))
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1,score2), align="center" , font=("Courier",24,"normal"))
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < shot2.ycor()+40 and ball.ycor()>shot2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < shot1.ycor()+40 and ball.ycor()>shot1.ycor()-40):
        ball.setx(340)
        ball.dx *=-1
       





