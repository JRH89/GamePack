import turtle
import random
import time

wn = turtle.Screen()
wn.setup(700,500)
wn.colormode(255)
wn.bgcolor(0, 180, 90)
wn.tracer(0)
wn.title("Hoop Master")

basket = turtle.Turtle()
basket.showturtle()
basket.penup()
basket.goto(0, 150)
wn.register_shape("hoop1.gif")
basket.shape("hoop1.gif")

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("orange")
ball.shapesize(2.5)
ball.goto(0, -180)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-330, -230)
pen.write("Score:0", font=("Verdana", 30, "bold"))

pen2 = turtle.Turtle()
pen2.penup()
pen2.hideturtle()
pen2.goto(100, -230)
pen2.write("Shots:0", font=("Verdana", 30, "bold"))

pen3 = turtle.Turtle()
pen3.penup()
pen3.hideturtle()
pen3.goto(-330, 200)
pen3.write("Accuracy:0", font=("Verdana", 30, "bold"))

def shoot():
    global shots1, score1
    shots1 += 1
    pen2.clear()
    pen2.write("Shots:{}".format(shots1), font=("Verdana", 30, "bold"))

    for ball in range(30):
        y = ball.ycor()
        y += 15
        x_diff = basket.xcor() - ball.xcor()
        x_diff /= 10  # divide by a factor to slow down horizontal movement
        x = ball.xcor() + x_diff
        ball.goto(x, y)
        time.sleep(0.02)
        wn.update()
        
        if (ball.xcor() < basket.xcor() + 30) and (ball.xcor() > basket.xcor() - 30) and (ball.ycor() == basket.ycor()):
            score1 += 1
            ball.sety(120)
            wn.update()
            time.sleep(0.02)
            ball.sety(80)
            wn.update()
            pen.clear()
            pen.write("Score:{}".format(score1), font=("Verdana", 30, "bold"))
            break
            
    if score1 > 0:
        accuracy = score1/shots1*100
        pen3.clear()
        pen3.write("Accuracy:{:.2f}".format(accuracy), font=("Verdana", 30, "bold"))
    
    # reset ball position after a short delay
    time.sleep(1)
    ball.goto(0, -180)

          
def yay1():
    shoot()
    
wn.listen()
wn.onkeypress(yay1, "s")

score1 = 0
shots1 = 0

while True:
    wn.update()
    
    x = random.randint(1, 150)
    basket.setx(basket.xcor() + x)
    time.sleep(0.1)
    x = random.randint(1, 150)
    time.sleep(0.1)
    basket.setx(basket.xcor() - x)
    
    if basket.xcor() > 250:
        basket.setx(220)
    if basket.xcor() < -250:
        basket.setx(-220)