from turtle import Screen
from snake import Snake
from myDay24.my182.food import Food
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Global objects
snake = None
food = None
scoreboard = None
game_is_on = True

def setup_game():
    global snake, food, scoreboard
    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(restart_game, "r")

def game_loop():
    global game_is_on
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
           snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

def restart_game():
    setup_game()
    game_loop()

# Start the game
setup_game()
game_loop()
screen.exitonclick()
