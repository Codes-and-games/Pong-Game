import time
from paddle import *
from ball import *
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((- 350, 0))
ball1 = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while (game_is_on):
    time.sleep(.05)
    screen.update()
    ball1.move()

    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce()

    if (ball1.distance(r_paddle) < 50 and ball1.xcor() > 320) or (
            ball1.distance(l_paddle) < 50 and ball1.xcor() < -320):
        ball1.bounce_x()

    if ball1.xcor() > 380:
        ball1.man()
        scoreboard.l_point()

    if ball1.xcor() < -380:
        ball1.man()
        scoreboard.r_point()

screen.exitonclick()
