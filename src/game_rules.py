from abc import ABC
from enum import Enum, auto

class GameMode(Enum):
    """
    Enum class representing the game difficulty mode
    """
    EASY   = auto()
    MEDIUM = auto()
    HARD   = auto()


class GameRules(ABC):
    """
    Abstract class keeping the game parameters that depend on
    the game difficulty mode
    """
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
        """
        Returns the bomb field size
        """
        return GameRules.__BOMB_FIELD_SIZE[game_mode]

    @staticmethod
    def get_bombs_count(game_mode: GameMode):
        """
        Returns the bombs count
        """
        return GameRules.__BOMBS_COUNT[game_mode]

    @staticmethod
    def get_flags_count(game_mode: GameMode):
        """
        Returns the flags count
        """
        return GameRules.__BOMBS_COUNT[game_mode]


class GameRestart(Enum):
    """
    Enum class representing player's decision about the game restart 
    """
    RETRY       = auto()
    CHANGE_MODE = auto()
