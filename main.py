import turtle
import pandas
from map import Map

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game = Map()
data = pandas.read_csv("50_states.csv")
correct_guesses = []
current_score = 0
title_text = "Guess the State"

while current_score < 51:
    answer_state = screen.textinput(title=title_text, prompt="What's another state's name?")
    state_list = data.state.to_list()
    print(f"answer_state: {answer_state}")
    guessed_answer = answer_state.title()
    print(f"guessed_answer: {guessed_answer}")
    state_found = False
    for state in state_list:
        if guessed_answer == state:
            state_found = True
            break

    if state_found:
        if correct_guesses.count(guessed_answer) == 0:
            correct_guesses.append(guessed_answer)
            state_info = data[data.state == guessed_answer]
            game.state = guessed_answer
            game.x = int(state_info.x.to_string(index=False))
            game.y = int(state_info.y.to_string(index=False))
            game.update_map()
            game.add_point()
            title_text = f"{game.score}/50 States Correct"

screen.exitonclick()
