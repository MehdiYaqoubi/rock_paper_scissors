PLAYER_OPTIONS = {'r': "Rock", 'p': "Paper", 's': "Scissors"}
CONTROL_OPTIONS = {'e': "Exit"}
PLAY_RULE = {
    'r': {'r': 0, 'p': -1, 's': 1},
    's': {'r': -1, 'p': 1, 's': 0},
    'p': {'r': 1, 'p': 0, 's': -1}
}

RESULT_BANNER = {
    1: "You win",
    0: "tie",
    -1: "You lose"
}
