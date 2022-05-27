from enum import Enum, auto

class CellType(Enum):
    BOMB  = auto()
    EMPTY = auto()


class Cell:
    def __init__(self, cell_type: CellType):
        self.__cell_type = cell_type
        self.__adjacent_bombs = 0

    def get_cell_type(self):
        return self.__cell_type

    def get_adjacent_bombs(self):
        return self.__adjacent_bombs

    def set_cell_type(self, cell_type: CellType):
        self.__cell_type = cell_type

    def increment_adjacent_bombs(self):
        self.__adjacent_bombs += 1
        return self.__adjacent_bombs

    def __str__(self):
        if self.__cell_type == CellType.BOMB:
            return "B"
        elif self.__cell_type == CellType.FLAG:
            return "F"
        return "E"

    