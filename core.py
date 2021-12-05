from constants import PLAY_RULE


def check_one_hand(user_choice, system_choice):
    return PLAY_RULE[user_choice][system_choice]


def modify_scores(current_result, current_scores):
    if current_result == 1:
        current_scores['user'] += 1
    elif current_result == -1:
        current_scores['system'] += 1


def check_total(current_scores):
    if current_scores['user'] == 3:
        current_scores['total_user'] += 1
        current_scores['user'] = 0
        current_scores['system'] = 0
        print('#' * 30, '\t You win the hand \t', '#' * 30)
        print(
            f"Total score: {current_scores['total_user']} - {current_scores['total_system']}")
        print('#' * 83)
    elif current_scores['system'] == 3:
        current_scores['total_system'] += 1
        current_scores['user'] = 0
        current_scores['system'] = 0
        print('#' * 30, '\t You lose the hand \t', '#' * 30)
        print(
            f"Total score: {current_scores['total_user']} - {current_scores['total_system']}")
        print('#' * 83)
