import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
state_list = data.state.to_list()

guessed_answer = answer_state.capitalize()
state_found = False
for state in state_list:
    if guessed_answer == state:
        state_found = True
        break

if state_found:
    correct_guesses.append(guessed_answer)
    print(data[data.state == answer_state.capitalize()].x)
    print(data[data.state == answer_state.capitalize()].y)

# if state_list.index(answer_state.capitalize()):
#     print("Hit")
# else:
#     print("Nope")

# TODO: 3. Write correct guesses onto the map
# TODO: 4. Use a loop to allow the user to keep guessing
# TODO: 5. Record the correct guess in a list
# TODO: 6. Keep track of the score

screen.exitonclick()
