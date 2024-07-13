from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    points_of_winning = (int(difficulty) * 3) + 5
    current_score = open(SCORES_FILE_NAME).readline()

    if current_score == '' or current_score.isdigit() is False:
        current_score = open(SCORES_FILE_NAME, 'w')
        current_score.write(str(points_of_winning))
    else:
        old_score = int(current_score)
        current_score = open(SCORES_FILE_NAME, 'w')
        updated_score = old_score + points_of_winning
        current_score.write(str(updated_score))
