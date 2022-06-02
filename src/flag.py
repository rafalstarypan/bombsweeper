from cell import *
from game_rules import *

class FlagManager:
    def __init__(self, game_mode: GameMode):
        self.reset(game_mode)

    
    def reset(self, game_mode: GameMode):
        self.__flags_count = GameRules.get_flags_count(game_mode)
        self.__flag_coords = set()

    
    def add_flag(self, row, col):
        if len(self.__flag_coords) == self.__flags_count:
            return
        if (row, col) in self.__flag_coords:
            return

        self.__flag_coords.add((row, col))
    

    def remove_flag(self, row, col):
        if (row, col) in self.__flag_coords:
            self.__flag_coords.remove((row, col))

    
    def is_flag(self, row, col):
        return (row, col) in self.__flag_coords


    def get_remaining_flags(self):
        return self.__flags_count - len(self.__flag_coords)
        
