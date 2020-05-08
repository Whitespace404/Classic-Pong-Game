import turtle
from random import randint
from time import sleep as wait

# for windows:
# import winsound
# and use this command:-

# winsound.Playsound("bounce.wav", winsound.SND_ASYNC)

root = turtle.Screen()
root.title("Rahul's Pong")
root.bgcolor("black")
root.setup(width=800, height=600)
root.tracer(0)
score_a = 0
score_b = 0
player = ''
j = 0

# Creating the functions-
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)


# Listen
root.listen()
root.onkeypress(paddle_a_up, 'w')
root.onkeypress(paddle_a_down, 's')
root.onkeypress(paddle_b_up, 'Up')
root.onkeypress(paddle_b_down, 'Down')

# Paddle on the left
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(360, 0)

# Paddle on the right
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# Ball in the center
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Write score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write(f"""{score_b + score_a}""", align='center',
          font=('Courier', 26, 'normal'))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('white')
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 0)


def losing_msg():
    pen2.write(f'Remember, the lowest score wins!', align='center', font=('Courier', 32, 'normal'))
    wait(1)
    pen2.clear()




pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color('white')
# pen3.penup()
pen3.hideturtle()
pen3.goto(0, 0)
pen3.write('Ready? Starting in 3 seconds.', align='center', font=('Courier', 32, 'normal'))
wait(2)
pen3.clear()
wait(3)
while True:
    root.update()
    # Moving the ball
    xsetting = ball.xcor() + ball.dx
    ball.setx(xsetting)
    ysetting = ball.ycor() + ball.dy
    ball.sety(ysetting)

    # Border checking- Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Border checking- Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # B lost
    # Border checking- Right
    if ball.xcor() > 390:
        player = 'Player B'
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'{score_b + score_a}', align='center',
                  font=('Courier', 26, 'normal'))
        losing_msg()

    # A lost
    # Border checking- Right
    if ball.xcor() < -390:
        player = 'Player A'
        ball.goto(randint(10, 100), randint(10, 100))
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'{score_b + score_a}', align='center',
                  font=('Courier', 26, 'normal'))
        losing_msg()

    # Deflect off right paddle
    if ball.xcor() > 340:
        if ball.ycor() < paddle_b.ycor() + 50:
            if ball.ycor() > paddle_b.ycor() - 40:
                if ball.xcor() < 350:
                    ball.setx(340)
                    ball.dx *= -1
                    j += 1
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass

    # Deflect off left paddle
    if ball.xcor() < -340:
        if ball.ycor() < paddle_a.ycor() + 50:
            if ball.ycor() > paddle_a.ycor() - 40:
                if ball.xcor() > -350:
                    ball.setx(-340)
                    ball.dx *= -1
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
# todo add average feature with 20 paddle hit limit with one local variable for both paddles
