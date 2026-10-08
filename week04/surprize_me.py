import turtle
import random

window = turtle.Screen()

game = turtle.Turtle()
game.color("black")
game.shape("square")
game.penup()
game.shapesize(20,32)

p1pos = 0
p2pos = 0
ballDir = True
gameover = False

ballSpeed = 1

ball = turtle.Turtle()
ball.penup()
ball.color('blue')
ball.speed(ballSpeed)
ball.shape('circle')
ball.shapesize(0.5,0.5)

player1 = turtle.Turtle()
player1.color("green")
player1.shape("square")
player1.speed(10)
player1.shapesize(5,1)
player1.penup()
player1.teleport(-300,p1pos)
player1.speed(1)

player2 = turtle.Turtle()
player2.color("red")
player2.shape("square")
player2.speed(10)
player2.shapesize(5,1)
player2.penup()
player2.teleport(300,p2pos)
player2.speed(1)

def p1up():
    global p1pos
    if (p1pos < 140):
        p1pos += 10
        player1.teleport(-300, p1pos)

def p1down():
    global p1pos
    if (p1pos > -140):
        p1pos -= 10
        player1.teleport(-300, p1pos)

def p2up():
    global p2pos
    if (p2pos < 140):
        p2pos += 10
        player2.teleport(300, p2pos)

def p2down():
    global p2pos
    if (p2pos > -140):
        p2pos -= 10
        player2.teleport(300, p2pos)

def ballup():
    ball.setposition(ball.xcor(), ball.ycor()+10)

def balldown():
    ball.setposition(ball.xcor(), ball.ycor()-10)

def speedUp():
    global ballSpeed
    global ball

    if (ballSpeed < 3):
        ballSpeed += 0.1
        ball.speed(ballSpeed)

ballRange = random.randrange(-10,10,1)
if ballRange == 0:
    ballRange = 5
while not gameover:

    if (ballDir):
        ball.forward(10)
    else:
        ball.backward(10)

    # top yukarıya çarparsa
    if (ball.ycor() > 190):
        ballRange *= -1

    #top şağıya çarparsa
    if (ball.ycor() < -190):
        ballRange *= -1

    ball.setposition(ball.xcor(), ball.ycor()+ballRange)

    ballX = int(ball.xcor())
    ballY = int(ball.ycor())

    window.onkey(p1up, "w")
    window.onkey(p1down, "s")
    window.onkey(p2up, "Up")
    window.onkey(p2down, "Down")
    window.onkey(ballup, "y")
    window.onkey(balldown, "h")
    window.listen()


    #top oyuncu1 e çarparsa
    if (ballX == -290 and ballY <= p1pos+50 and ballY >= p1pos-50):
        speedUp()
        ballDir = not ballDir

    #top oyuncu2 ye çarparsa
    if (ballX == 290 and ballY <= p2pos+50 and ballY >= p2pos-50):
        speedUp()
        ballDir = not ballDir

    #top sağdan dışarı çıkarsa
    if (ballX > 300):
        gameover = True
        print("Player 1 wins!!")

    # top soldan dışarı çıkarsa
    if (ballX < -300):
        gameover = True
        print("Player 2 wins!!")          