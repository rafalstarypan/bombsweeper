from abc import ABC
from enum import Enum, auto

class GameMode(Enum):
    EASY   = auto()
    MEDIUM = auto()
    HARD   = auto()


class GameRules(ABC):
    __BOMB_FIELD_SIZE = {
        GameMode.EASY: 8,
        GameMode.MEDIUM: 10,
        GameMode.HARD: 10
    }

    __BOMBS_COUNT = {
        GameMode.EASY: 10,
        GameMode.MEDIUM: 15,
        GameMode.HARD: 20
    }

    @staticmethod
    def get_bomb_field_size(game_mode: GameMode):
        return GameRules.__BOMB_FIELD_SIZE[game_mode]

    @staticmethod
    def get_bombs_count(game_mode: GameMode):
        return GameRules.__BOMBS_COUNT[game_mode]

    @staticmethod
    def get_flags_count(game_mode: GameMode):
        return GameRules.__BOMBS_COUNT[game_mode]
