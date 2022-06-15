from cell import *
from bomb_field_grid import *
from flag import *
from game_rules import *
from time_manager import * 
from queue import Queue

class GameStatus(Enum):
    """
    Enum class representing the status of the game
    """
    IN_PROGRESS = auto()
    LOST        = auto()
    VICTORY     = auto()


class GameController:
    """
    The controller class is responsible for the communication
    between view and model classes 
    """

    def __init__(self, game_mode: GameMode, nickname: str):
        """
        Initializes the controller object with the difficulty mode 
        and player's nickname
        """
        self.__game_mode = game_mode
        self.__nickname = nickname
        self.reset()

    
    def reset(self):
        """
        Resets the object state
        """
        self.__game_status  = GameStatus.IN_PROGRESS
        self.__bomb_field   = BombFieldGrid(self.__game_mode)   
        self.__flag_manager = FlagManager(self.__game_mode) 
        self.__time_manager = TimeManager()


    def is_bomb(self, row, col):
        """
        Checks if the cell with given coordinates is a bomb
        """
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__bomb_field.is_bomb(row, col)


    def is_flag(self, row, col):
        """
        Checks if the cell with given coordinates is a flag
        """
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__flag_manager.is_flag(row, col)


    def is_empty(self, row, col):
        """
        Checks if the cell with given coordinates is empty
        """
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__bomb_field.is_empty()

    
    def is_covered(self, row, col):
        """
        Checks if the cell with given coordinates is covered
        """
        if not self.__bomb_field.inside(row, col): 
            return False
        return self.__bomb_field.is_covered(row, col)


    def uncover_cell(self, row, col):
        """
        Uncovers cells starting from the cell with given coordinates
        """
        if self.is_flag(row, col) or not self.is_covered(row, col):
            return 

        if self.is_bomb(row, col):
            self.__game_status = GameStatus.LOST
            return
        
        self.__bomb_field.uncover(row, col)
        if self.__is_victory():
            self.__game_status = GameStatus.VICTORY


    def __is_victory(self):
        """
        Checks if the game has ended with the victory
        """
        size = GameRules.get_bomb_field_size(self.__game_mode)
        bombs_count = GameRules.get_bombs_count(self.__game_mode)
        return self.__bomb_field.get_uncovered_cells() == (size**2 - bombs_count)


    def uncover_bombs(self):
        """
        Reveals the bombs location after 
        losing the game
        """
        size = self.__bomb_field.get_size()
        for i in range(size):
            for j in range(size):
                if self.is_bomb(i, j):
                    self.__bomb_field.uncover(i, j)


    def handle_flag_event(self, row, col):
        """
        Handles the mouse right button click.
        Adds or removes a flag depending on the cell
        type and the number of remaining flags
        """
        if not self.is_covered(row, col):
            return
        if self.is_flag(row, col):
            self.__flag_manager.remove_flag(row, col)
        else:
            self.__flag_manager.add_flag(row, col)


    def get_adjacent_bombs_count(self, row, col):
        """
        Returns the count of the adjacent bombs 
        of the cell with given coordinates
        """
        return self.__bomb_field.get_adjacent_bombs_count(row, col)


    def get_game_time(self):
        """
        Returns the duration of the game in seconds
        """
        return self.__time_manager.get_game_time()

    
    def get_game_status(self):
        "Returns the game status"
        return self.__game_status


    def get_size(self):
        """
        Returns the bomb field size
        """
        return GameRules.get_bomb_field_size(self.__game_mode)

    
    def get_remaining_flags(self):
        """
        Returns the number of remaining flags
        """
        return self.__flag_manager.get_remaining_flags()

    
    def get_game_summary(self):
        """
        Returns a tuple containing information
        needed by the game summary view:
        player's nickname, final game status, game duration time
        in seconds
        """
        return (self.__nickname, self.__game_status, self.get_game_time())

