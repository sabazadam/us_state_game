import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.values

correct_answer_list = []
correct_answer = 0
while True:
    answer_state = screen.textinput(f" {correct_answer}/50 States Correct"
                                    ,prompt="What's another state's name?").title()
    if answer_state == "Exit": break
    if answer_state in all_states:
        if answer_state in correct_answer_list: continue
        state = data[data.state == answer_state].values[0]
        x = state[1]
        y = state[2]
        turtle.goto(x,y)
        turtle.write(answer_state)
        correct_answer_list.append(state[0])
        correct_answer += 1


for state in all_states:
    if state in correct_answer_list: continue
    my_state = data[data.state == state].values[0]
    x = my_state[1]
    y = my_state[2]
    turtle.goto(x,y)
    turtle.write(my_state[0])

screen.exitonclick()