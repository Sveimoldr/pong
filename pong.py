import turtle
from time import sleep

window = turtle.Screen()
window.title('Pong by Leo Carvalho')
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Placar

scoreA = 0
scoreB = 0

#Barra P1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Barra P2

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 
ball.dy = 2
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)
def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)
def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

#Keybindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")



#Loop principal
while True:
    sleep(0.01)
    window.update()
    
  #movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Checagemde borda
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      
    elif ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      
    if ball.xcor() > 350:
      scoreA += 1
      pen.clear()
      pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
      ball.goto (0, 0)
      ball.dx *= -1
    elif ball.xcor() < -350:
      scoreB += 1
      pen.clear()
      pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
      ball.goto (0,0)
      ball.dx*= -1
#Colisões
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
       
    