from turtle import Turtle,Screen, color
import os
import random
os.system('cls || clear')

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
print(f"Your bet is on: {user_bet}")

colors = ["red","orange","yellow","green","blue","purple"]

y_max = 150;y_min = -150;x_max = 230;x_min = -230

nr_of_turtles = len(colors)
y_step = (y_max-y_min)/nr_of_turtles
list_of_turtles = []

for i,color in enumerate(colors):
    turtle_nr = Turtle(shape="turtle")
    turtle_nr.color(f"{color}")
    turtle_nr.penup()
    turtle_nr.goto(x=x_min,y=y_min+i*y_step)

    list_of_turtles.append(turtle_nr)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_of_turtles:
        random_dist = random.randint(1,10)
        turtle.forward(random_dist)
        if turtle.xcor()>x_max:
            winner = turtle.color()[0]
            print(f"The winner is {winner}")
            is_race_on = False
            break

if winner == user_bet:
    print("You won!")
else: print("You lost.")

screen.exitonclick()