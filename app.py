from games import memory_game, guess_game, currency_roulette_game
from score import add_score


def welcome():
    username = input("Please enter your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def is_valid(string, maximum):
    if not string.isnumeric():
        print("Input cannot be a string or negative number")
        return -1
    elif not 1 <= int(string) <= maximum:
        print("Invalid number")
        return -1
    else:
        print("Selected successfully!\n")


def start_play():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
       guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    game_number = input("Choose a game by number: ")
    while is_valid(game_number, 3) == -1:
        game_number = input("Please try again: ")

    difficulty_level = input("Choose a difficulty level between 1-5: ")
    while is_valid(difficulty_level, 5) == -1:
        difficulty_level = input("Choose a difficulty level between 1-5: ")

    add_score(difficulty_level)

    if int(game_number) == 1:
        print((20 * "-") + " Memory Game! " + (20 * "-"))
        memory_game.play(int(difficulty_level))

    elif int(game_number) == 2:
        print((20 * "-") + " Guess Game! " + (20 * "-"))
        guess_game.play(int(difficulty_level))

    elif int(game_number) == 3:
        print((20 * "-") + " Currency Roulette Game! " + (20 * "-"))
        currency_roulette_game.play(int(difficulty_level))
