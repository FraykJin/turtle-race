from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle_list =[]
y = 90
for i in range(len(colors)):
    turtle_list.append(Turtle(shape='turtle'))
    turtle_list[i].penup()
    turtle_list[i].goto(-230, y)
    turtle_list[i].color(colors[i])
    y -= 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('win')
            else:
                print('lose')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()