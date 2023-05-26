import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

states = data["state"]
states_list = states.to_list()
correct_states = []

while len(correct_states) < 50:

    answer = screen.textinput(title=f"{len(correct_states)}/{len(states_list)} States Correct", prompt="What's another states name?").title()

    if answer == "Exit":
        to_learn = [state for state in states_list if state not in correct_states]
        df = pandas.DataFrame(to_learn)
        df.to_csv("states_to_learn.csv")
        break

    if answer in states_list:
        correct_states.append(answer)
        x_cor = int(data[data["state"] == answer].x.iloc[0])
        y_cor = int(data[data["state"] == answer].y.iloc[0])
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x_cor, y_cor)
        turtle.write(arg=answer, align="center", font=("Ariel", 9, "bold"))


