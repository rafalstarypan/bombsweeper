from cell import *
from game_rules import *
import random
from queue import Queue

class BombFieldGrid:
    """
    The class represents the bomb field. It performs the main part
    of the game's logic
    """

    def __init__(self, game_mode: GameMode):
        """
        Initializes the object with the game difficulty mode
        """
        self.__game_mode = game_mode
        self.reset()
    

    def reset(self):
        """
        Resets the object state
        """
        self.__SIZE = GameRules.get_bomb_field_size(game_mode=self.__game_mode)
        self.__BOMBS_COUNT = GameRules.get_bombs_count(game_mode=self.__game_mode)

        self.__is_covered = [[True] * self.__SIZE for _ in range(self.__SIZE)]
        self.__field = [[Cell(CellType.EMPTY) for _ in range(self.__SIZE)] for _ in range(self.__SIZE)]
        self.__uncovered_cells = 0
        
        self.__create_bomb_field()


    def __create_bomb_field(self):
        """
        Creates the bomb field choosing random locations of the bombs
        """
        bombs_coords = set()

        while len(bombs_coords) < self.__BOMBS_COUNT:
            row = random.randrange(0, self.__SIZE)
            col = random.randrange(0, self.__SIZE)
            pos = row, col

            if pos in bombs_coords:
                continue

            bombs_coords.add(pos)
            self.__field[row][col].set_cell_type(CellType.BOMB)

        for bomb in bombs_coords:
            neighbors = self.__get_neighbors(*bomb)
            for r, c in neighbors:
                if self.__field[r][c].get_cell_type() != CellType.BOMB:
                    self.__field[r][c].increment_adjacent_bombs()
    

    def __get_neighbors(self, row, col):
        """
        Returns a list of cells neighbouring to the one 
        with given coordinates
        """
        neighbors = []
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc
            if self.inside(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors

    
    def get_size(self):
        """
        Returns the bomb field size
        """
        return self.__SIZE


    def inside(self, r, c):
        """
        Checks if the cell with given coordinates
        is situated inside the field
        """
        return r >= 0 and c >= 0 and r < self.__SIZE and c < self.__SIZE


    def get_cell_type(self, row, col):
        """
        Returns the type of the cell with given coordinates
        """
        return self.__field[row][col].get_cell_type()

    
    def get_adjacent_bombs_count(self, row, col):
        """
        Returns the count of the adjacent bombs 
        of the cell with given coordinates
        """
        return self.__field[row][col].get_adjacent_bombs()


    def get_uncovered_cells(self):
        "Returns the number of uncovered cells"
        return self.__uncovered_cells

    
    def set_cell_type(self, row, col, cell_type: CellType):
        """
        Sets the type of the cell with given coordinates
        """
        self.__field[row][col].set_cell_type(cell_type=cell_type)

    
    def is_bomb(self, row, col):
        """
        Checks if the cell with given coordinates is a bomb
        """
        return self.__field[row][col].is_bomb()


    def is_empty(self, row, col):
        """
        Checks if the cell with given coordinates is empty
        """
        return self.__field[row][col].is_empty()


    def is_covered(self, row, col):
        """
        Checks if the cell with given coordinates is covered
        """
        return self.__is_covered[row][col]

    
    def uncover(self, row, col):
        """
        Uncovers cells starting from the cell with given coordinates
        """
        self.__is_covered[row][col] = False

        if self.is_empty(row, col):
            self.__uncover_from_pos(row, col)

    
    def __uncover_from_pos(self, row, col):
        """
        Uncovers cells starting from the cell with given coordinates
        """
        q = Queue()
        q.put((row, col))
        self.__is_covered[row][col] = False
        self.__uncovered_cells += 1
        visited = set()

        while not q.empty():
            current = q.get()

            neighbors = self.__get_neighbors(*current)
            for r, c in neighbors:
                if (r, c) in visited:
                    continue
                
                cell: Cell = self.__field[r][c]
                if cell.is_empty() and cell.get_adjacent_bombs() == 0 and self.__is_covered[r][c]:
                    q.put((r, c))
                if cell.is_empty() and self.__is_covered[r][c]:
                    self.__is_covered[r][c] = False
                    self.__uncovered_cells += 1
                
                visited.add((r, c))