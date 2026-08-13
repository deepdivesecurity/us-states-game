import pandas
import turtle

BACKGROUND_FILE_PATH = "assets/blank_states_img.gif"
DATA_FILE_PATH = "assets/50_states.csv"
MISSED_STATES_FILE_PATH = "assets/missed_states.csv"

def read_data(file_path: str): 
    return pandas.read_csv(file_path)

def check_guess(df, guess): 
    if guess in df["state"].values: 
        return True
    else: 
        return False

def write_guess_to_map(guess, x, y): 
    text = turtle.Turtle()
    text.hideturtle()
    text.speed(0)
    text.penup()
    text.goto(x, y)
    text.write(guess)

def main(): 
    df = read_data(DATA_FILE_PATH)
    print()

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(BACKGROUND_FILE_PATH)
    turtle.shape(BACKGROUND_FILE_PATH)

    score = 0

    game_on = True
    while game_on: 
        guess = screen.textinput(f"{score}/50 States Correct", "What's another state's name?")
        guess = guess.title()
        if check_guess(df, guess): 
            write_guess_to_map(guess, int(df[df["state"] == guess]["x"].item()), int(df[df["state"] == guess]["y"].item()))
            df.drop(df[df["state"] == guess].index, inplace=True)
            score += 1
        if score == 50 or guess.lower() == "exit": 
            game_on = False
            df.to_csv(MISSED_STATES_FILE_PATH, columns=["state"], index=False)

if __name__ == "__main__":
    main()