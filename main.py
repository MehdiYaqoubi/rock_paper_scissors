from random import choice

from constants import PLAYER_OPTIONS, RESULT_BANNER, CONTROL_OPTIONS
from core import check_one_hand, modify_scores, check_total

scores = {'user': 0, 'system': 0, 'total_user': 0, 'total_system': 0}
play = True
while play:
    user_input = input('Enter your choice (options s, r, p)(e for Exit): ')
    system_choice = choice(list(PLAYER_OPTIONS.keys()))

    if user_input in PLAYER_OPTIONS.keys():
        result = check_one_hand(user_input, system_choice)
        modify_scores(result, scores)
        print(
            f"Your choice: {PLAYER_OPTIONS[user_input]},"
            f" system choice: {PLAYER_OPTIONS[system_choice]},"
            f" result: {RESULT_BANNER[result]},"
            f" scores: {scores['user']} - {scores['system']}"
        )
        check_total(scores)
    elif user_input in CONTROL_OPTIONS:
        play = False
        print('Thank you, Bye!')
    else:
        print('Invalid input, choose between the options please (s, r, p) ')
