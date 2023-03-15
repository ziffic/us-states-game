import turtle
import pandas
from map import Map

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

game = Map()
correct_guesses = []
current_score = 0
title_text = "Guess the State"

while current_score < 51:
    guessed_answer = screen.textinput(title=title_text, prompt="What's another state's name?").title()
    if guessed_answer == "Exit":
        break

    if guessed_answer in all_states:
        if correct_guesses.count(guessed_answer) == 0:
            correct_guesses.append(guessed_answer)
            state_data = data[data.state == guessed_answer]
            game.state = guessed_answer
            game.x = int(state_data.x)
            game.y = int(state_data.y)
            game.update_map()
            game.add_point()
            title_text = f"{game.score}/50 States Correct"
