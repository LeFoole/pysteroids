from enum import Enum


class GAME_STATE(Enum):
    MENU = 1
    PLAYING = 2
    OVER = 3

class GameStateManager():
    ''
    
    GAME_STATE = GAME_STATE.MENU

    def update_game_state(new_state):
        GameStateManager.GAME_STATE = new_state
