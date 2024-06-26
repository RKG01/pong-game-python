import turtle
import winsound

bouncing = "jump.wav" 

wn = turtle.Screen()
wn.title("Pong by @RKgaming")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


score_a = 0
score_b = 0


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)






paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2


ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("blue")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.15
ball2.dy = -0.15


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0 ", align="center", font=("courier", 14, "normal"))


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



wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center",
                  font=("courier", 14, "normal"))
        winsound.PlaySound("bouncing", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 14, "normal"))
        winsound.PlaySound("bouncing", winsound.SND_ASYNC)




    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1
        winsound.PlaySound("bouncing", winsound.SND_ASYNC)

    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1
        winsound.PlaySound("bouncing", winsound.SND_ASYNC)

    if ball2.xcor() > 390:
        ball2.goto(0, 0)
        ball2.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center",
                  font=("courier", 14, "normal"))
        winsound.PlaySound(bouncing, winsound.SND_ASYNC)

    if ball2.xcor() < -390:
        ball2.goto(0, 0)
        ball2.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 14, "normal"))
        winsound.PlaySound(bouncing, winsound.SND_ASYNC)





    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(bouncing, winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(bouncing, winsound.SND_ASYNC)

    if (340 < ball2.xcor() < 350) and (paddle_b.ycor() - 50 < ball2.ycor() < paddle_b.ycor() + 50):
        ball2.setx(340)
        ball2.dx *= -1
        winsound.PlaySound(bouncing, winsound.SND_ASYNC)

    if (-350 < ball2.xcor() < -340) and (paddle_a.ycor() - 50 < ball2.ycor() < paddle_a.ycor() + 50):
        ball2.setx(-340)
        ball2.dx *= -1
        winsound.PlaySound(bouncing, winsound.SND_ASYNC)





    if ball.xcor() >ball2.xcor():

        if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
          paddle_b_up()

        elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
          paddle_b_down()
    
    else:
        if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
          paddle_b_up()

        elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
          paddle_b_down()
