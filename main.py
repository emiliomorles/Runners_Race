from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which runner wil win the race? Enter a color: \n\n"
                                                          "(red, orange, yellow, green, blue or black)")
colors = ["red", "orange", "yellow", "green", "blue", "black"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_runners = []

goal = Turtle(shape="square")
goal.shapesize(stretch_wid=20, stretch_len=0.2, outline=0.2)
goal.penup()
goal.color("gray")
goal.goto(x=210, y=0)

for character_index in range(0, 6):
    new_runner = Turtle(shape="triangle")
    new_runner.penup()
    new_runner.color(colors[character_index])
    new_runner.goto(x=-210, y=y_positions[character_index])
    all_runners.append(new_runner)

if user_bet:
    is_race_on = True

while is_race_on:
    for runner in all_runners:
        if runner.xcor() > 210:
            is_race_on = False
            winning_runner = runner.pencolor()
            if winning_runner == user_bet:
                print(f"You've won!. The {winning_runner} runner is the winner!")
            else:
                print(f"You've lost!. The {winning_runner} runner is the winner!")

        random_distance = random.randint(0, 10)
        runner.forward(random_distance)

screen.exitonclick()
