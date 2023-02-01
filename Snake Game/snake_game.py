"""
    GIT: @drafonsopena
    + The objective is to create a Snake Game using Python.
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install libraries (eg: pip3 install tk)
    | Basic Python skills
    | Use a virtual environment
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Create display window
    | Create snake and food, functions and buttons
    +---------------- 3 ----------------
    | All necessary libraries for the Snake Game:
    | import turtle
    | import random
    | import time
    +------------------------------------
"""

# importing the necessary libraries
import turtle
import random
import time

# creation of game screen
screen = turtle.Screen()
screen.title("Jogo da Cobrinha")
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor("turquoise")

# setting directions and moving speed
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0
delay = 0.1

# creation of snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# creation of food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(30, 30)

# previous food
old_fruit = []

# setting the scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

# Keyboard binding
# move the snake UP
def go_up():
    if snake.direction != "down":
        snake.direction = "up"
# move the snake DOWN
def go_down():
    if snake.direction != "up":
        snake.direction = "down"
# move the snake LEFT
def go_left():
    if snake.direction != "right":
        snake.direction = "left"
# move the snake RIGHT
def go_right():
    if snake.direction != "left":
        snake.direction = "right"
# move UP
def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
# move DOWN
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
# move LEFT
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
# move RIGHT
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# identify which key is being pressed
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# snake and food collision
# main loop
while True:
    screen.update() # to update when the objects change
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001
    # setting the value for the new food
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index-1].xcor()
        b = old_fruit[index-1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()
# if the snake touches the borders of the window
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("GAME OVER \n YOUR SCORE: {}\n Thank you.".format(score), align="center", font=("Courier", 30, "bold"))
# if the snake touches itself
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("GAME OVER \n YOUR SCORE IS: {}".format(score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()