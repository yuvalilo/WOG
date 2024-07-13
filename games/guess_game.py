import random


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    input_num = int(input(f"Please enter a number within the range of 0 to {difficulty}: "))
    return input_num


def compare_results(num1, num2):
    if num1 == num2:
        return True
    return False


def play(difficulty):
    num1 = generate_number(difficulty)
    num2 = get_guess_from_user(difficulty)
    print(compare_results(num1, num2))
