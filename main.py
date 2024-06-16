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

print(data[data.state == "Connecticut"])
while True:
    answer_state = screen.textinput(title="Guess The State",prompt="What's another state's name?")
    if answer_state in all_states:

        state = data[data.state == answer_state]
        x = state.values[0][1]
        y = state.values[0][2]
        turtle.goto(x,y)
        turtle.write(answer_state)




