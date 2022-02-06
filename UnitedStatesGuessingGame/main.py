# Play this United States guessing game and test your knowledge of US geography!

from turtle import Screen, Turtle
from pandas import read_csv

# used this method to get more accurate spots for the state name to sit 
def get_mouse_click_coord(x,y):
    print(x,y)

def main():
    screen = Screen()
    screen.title("US States Guessing Game")
    image = "blank_states_img.gif"
    screen.addshape(image)

    us_map = Turtle()
    us_map.shape(image)
    
    text_writer = Turtle()
    text_writer.hideturtle()
    text_writer.up()

    df = read_csv("50_states.csv")
    state_coords = list(zip(df.x, df.y))
    states = dict(zip(df.state, state_coords))
    # screen.onscreenclick(get_mouse_click_coord)
    # screen.mainloop()
    guesses = []
    while True:
        input_title = f"{len(guesses)}/50 States Correct"
        answer = screen.textinput(input_title, "What is the name of another state?").title()
        if answer in states:
            text_writer.goto(states.get(answer))
            text_writer.write(answer, align="Center")
            guesses.append(answer)
        
        if len(guesses) == 50:
            screen.exitonclick()
            return
        
    
if __name__ == "__main__":
    main()