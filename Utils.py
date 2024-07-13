import time


SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 400


def screen_cleaner(a):
    print(f'\r{a}', end='')
    time.sleep(0.7)
    print('\r', end='')
    return a
