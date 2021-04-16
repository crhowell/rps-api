import random

from . import models

# Decision Matrix
DMATRIX = [
    [0, 2, 1],
    [1, 0, 2],
    [2, 1, 0],
]
# CMAP -> Choice Mapping:
# - Rock 0 (index) in DMATRIX
# - Paper 1 (index)  in DMATRIX
# - Scissors 2 (index) in DMATRIX 
CMAP = {'R': 0, 'P': 1, 'S': 2}
# Result Mapping - None (tie), True (win), False (loss)
RMAP = {0: None, 1: True, 2: False}

def check_player_won(p_choice, b_choice):
    """Uses a matrix for decision making.
    Choices are converted to an index using CMAP.
    
    Using the player index as the row and bot index column,
    we can figure out from the matrix if its a tie,win,loss.
    """
    p_idx, b_idx = CMAP[p_choice], CMAP[b_choice]
    matrix_index = DMATRIX[p_idx][b_idx]
    return RMAP[matrix_index]


def attach_game_data(request):
    bot = models.Bot.objects.order_by('?').first()
    bot_choice = random.choice(['R', 'P', 'S'])
    player_choice = request.data.get('player_choice')
    request.data.update({
        'creator': request.user.id,
        'bot': bot.id,
        'bot_choice': bot_choice
    })
    if player_choice:
        player_won = check_player_won(player_choice, bot_choice)
        request.data.update({'player_has_won': player_won})
    return request