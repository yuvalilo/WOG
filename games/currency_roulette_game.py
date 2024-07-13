import random
import requests


url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_9W8r7gPztsA3h1EcLoDVFY32Yyc1XQHgK5uceyfF"
resp = requests.get(url)
data = resp.json()


def get_money_interval():
    secret_number = random.randint(1, 100)
    return secret_number


def get_guess_from_user(secret_num):
    guess_num = int(input(f"Guess how much {secret_num} dollars are worth in shekels: "))
    return guess_num


def compare_results(difficulty,  secret_num, guess_num):
    range_num = 10 - difficulty
    if abs(secret_num * data["data"]["ILS"] - guess_num) > range_num:
        return False
    return True


def play(difficulty):
    num1 = get_money_interval()
    num2 = get_guess_from_user(num1)
    print(compare_results(difficulty, num1, num2))
