from cell import *
from game_rules import *

class FlagManager:
    """
    The class manages the flags during the game
    """

    def __init__(self, game_mode: GameMode):
        """
        Initializes the object with the game difficulty mode
        """
        self.reset(game_mode)

    
    def reset(self, game_mode: GameMode):
        """
        Resets the object
        """
        self.__flags_count = GameRules.get_flags_count(game_mode)
        self.__flag_coords = set()

    
    def add_flag(self, row, col):
        """
        Adds a new flag to the structure
        """
        if len(self.__flag_coords) == self.__flags_count:
            return
        if (row, col) in self.__flag_coords:
            return

        self.__flag_coords.add((row, col))
    

    def remove_flag(self, row, col):
        """
        Removes a flag with given coordinates from the structure 
        """
        if (row, col) in self.__flag_coords:
            self.__flag_coords.remove((row, col))

    
    def is_flag(self, row, col):
        """
        Checks if the flag with given coordinates exists
        """
        return (row, col) in self.__flag_coords


    def get_remaining_flags(self):
        """
        Returns the number of remaining flags
        """
        return self.__flags_count - len(self.__flag_coords)
        
