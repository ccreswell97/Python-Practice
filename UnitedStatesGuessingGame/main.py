from turtle import Screen, Turtle
from pandas import read_csv

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
    
    while True:
        answer = screen.textinput("Guess the state", "What is the name of another state?").title()
        if answer in states:
            text_writer.goto(states.get(answer))
            text_writer.write(answer)
    
if __name__ == "__main__":
    main()