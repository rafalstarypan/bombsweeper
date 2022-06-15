from enum import Enum, auto

class CellType(Enum):
    """
    Enum class representing cell type
    """
    BOMB  = auto()
    EMPTY = auto()


class Cell:
    """
    Class represents a single cell in the bomb field
    """
    def __init__(self, cell_type: CellType):
        """
        Initializes the Cell object with cell type
        and adjacent bombs count
        """
        self.__cell_type = cell_type
        self.__adjacent_bombs = 0


    def get_cell_type(self):
        """
        Returns the cell type
        """
        return self.__cell_type


    def get_adjacent_bombs(self):
        """
        Returns the adjacent bombs count
        """
        return self.__adjacent_bombs


    def set_cell_type(self, cell_type: CellType):
        """
        Sets the cell type
        """
        self.__cell_type = cell_type


    def is_bomb(self):
        """
        Checks if cell is a bomb
        """
        return self.__cell_type == CellType.BOMB

    
    def is_empty(self):
        """
        Checks if cell is empty
        """
        return self.__cell_type == CellType.EMPTY


    def increment_adjacent_bombs(self):
        """
        Increments by 1 the count of bombs adjacent to the cell 
        """
        self.__adjacent_bombs += 1
        return self.__adjacent_bombs


    def __str__(self):
        if self.__cell_type == CellType.BOMB:
            return "B"
        elif self.__cell_type == CellType.FLAG:
            return "F"
        return "E"

    