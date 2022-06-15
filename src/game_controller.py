from cell import *
from bomb_field_grid import *
from flag import *
from game_rules import *
from time_manager import * 
from queue import Queue

class GameStatus(Enum):
    IN_PROGRESS = auto()
    LOST        = auto()
    VICTORY     = auto()


class GameController:
    def __init__(self, game_mode: GameMode, nickname: str):
        self.__game_mode = game_mode
        self.__nickname = nickname
        self.reset()

    
    def reset(self):
        self.__game_status  = GameStatus.IN_PROGRESS
        self.__bomb_field   = BombFieldGrid(self.__game_mode)   
        self.__flag_manager = FlagManager(self.__game_mode) 
        self.__time_manager = TimeManager()


    def is_bomb(self, row, col):
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__bomb_field.is_bomb(row, col)


    def is_flag(self, row, col):
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__flag_manager.is_flag(row, col)


    def is_empty(self, row, col):
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__bomb_field.is_empty()

    
    def is_covered(self, row, col):
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__bomb_field.is_covered(row, col)


    def uncover_cell(self, row, col):
        if self.is_flag(row, col) or not self.is_covered(row, col):
            return 

        if self.is_bomb(row, col):
            self.__game_status = GameStatus.LOST
            return
        
        self.__bomb_field.uncover(row, col)
        if self.__is_victory():
            self.__game_status = GameStatus.VICTORY


    def __is_victory(self):
        size = GameRules.get_bomb_field_size(self.__game_mode)
        bombs_count = GameRules.get_bombs_count(self.__game_mode)
        return self.__bomb_field.get_uncovered_cells() == (size**2 - bombs_count)


    def uncover_bombs(self):
        size = self.__bomb_field.get_size()
        for i in range(size):
            for j in range(size):
                if self.is_bomb(i, j):
                    self.__bomb_field.uncover(i, j)


    def handle_flag_event(self, row, col):
        if not self.is_covered(row, col):
            return
        if self.is_flag(row, col):
            self.__flag_manager.remove_flag(row, col)
        else:
            self.__flag_manager.add_flag(row, col)


    def get_adjacent_bombs_count(self, row, col):
        return self.__bomb_field.get_adjacent_bombs_count(row, col)


    def get_game_time(self):
        return self.__time_manager.get_game_time()

    
    def get_game_status(self):
        return self.__game_status


    def get_size(self):
        return GameRules.get_bomb_field_size(self.__game_mode)

    
    def get_remaining_flags(self):
        return self.__flag_manager.get_remaining_flags()

    
    def get_game_summary(self):
        return (self.__nickname, self.__game_status, self.get_game_time())

