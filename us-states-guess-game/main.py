import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-guess-game\states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("us-states-guess-game\states.csv")

all_states = states.state.to_list()
guessed_states = []


while len(guessed_states) < 50:

    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 Correct states ", prompt="What's another state's name").title()
    
    if user_answer == "Exit":
        
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(states)

        break

    if user_answer in all_states:
        guessed_states.append(user_answer)
        #Initialize a turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #gives the row of the state guessed by the user
        state_row = states[states.state == user_answer]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(user_answer)
        



#gets the coordinates of the states yo show them on the screen
# def get_mouse_click_coor(x, y):
#     print(x,  y)

# turtle.onscreenclick(get_mouse_click_coor)


#Keeps the screen on till the cancle button is clicked
# screen.exitonclick()
# turtle.mainloop()


