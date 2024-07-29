from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import pygame
pygame.init()
sound1 = pygame.mixer.Sound("eatfood.wav")
sound2 = pygame.mixer.Sound("gameover.wav")

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.bgpic("backggg.png")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 15:
        sound1.play()
        food.refresh()
        snake.extend()
        score.increase_score()



    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        score.reset_score()
        snake.reset_snake()
        game_on = False
        sound2.play()
        score.game_over()



    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
            game_on = False
            sound2.play()
            score.game_over()





screen.exitonclick()