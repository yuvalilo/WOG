import random
from Utils import screen_cleaner


def generate_sequence(difficulty):
    a = []
    for i in range(0, difficulty):
        rand_num = random.randint(1, 101)
        a.append(rand_num)
    return screen_cleaner(a)


def get_list_from_user(a):
    print("Please enter the list of numbers you just saw: ")
    b = []
    for i in range(0, len(a)):
        b.append(int(input()))
    return b


def is_list_equal(a, b):
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True


def play(difficulty):
    a = generate_sequence(difficulty)
    b = get_list_from_user(a)
    print(is_list_equal(a, b))
