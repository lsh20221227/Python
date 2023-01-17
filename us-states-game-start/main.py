import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer = []

while len(answer) < 50:
    answer_state = screen.textinput(title=f"{len(answer)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in answer:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        answer.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


# states to learn.csv
# nam = list(set(all_states) - set(answer))

screen.exitonclick()

