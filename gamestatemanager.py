from enum import Enum

from objectgroups import ObjectGroups


class GAME_STATE(Enum):
    PRE_MENU = 1
    MENU = 2
    PLAYING = 3
    OVER = 4

class GameManager():
    ''
    
    GAME_STATE = GAME_STATE.MENU
    GAME_SCORE: int = 0

    def update_game_state(new_state):
        GameManager.GAME_STATE = new_state
