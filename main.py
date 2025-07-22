import turtle
import pandas

screen=turtle.Screen()
screen.title("Indian States and UTs Game")
image="India.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("India States-UTs.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<28:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/28 states correct ",
                                  prompt="What is another state's name ?").title()

    #If answer_state is one of the states in all states of 50_states.csv
    #If they got it right :
    #Create a turtle to write the name of state in state's x and y coordinates

    if answer_state=="Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
