from cell import *
from game_rules import *
import random

class BombFieldGrid:
    def __init__(self, game_mode: GameMode):
        self.SIZE = GameRules.get_bomb_field_size(game_mode=game_mode)
        self.BOMBS_COUNT = GameRules.get_bombs_count(game_mode=game_mode)
        self.is_covered = [[False] * self.SIZE for _ in range(self.SIZE)]
        self.field = [[Cell(CellType.EMPTY) for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        
        self.__create_bomb_field()
        
    def __create_bomb_field(self):
        bombs_coords = set()

        while len(bombs_coords) < self.BOMBS_COUNT:
            row = random.randrange(0, self.SIZE)
            col = random.randrange(0, self.SIZE)
            pos = row, col

            if pos in bombs_coords:
                continue

            bombs_coords.add(pos)
            self.field[row][col].set_cell_type(CellType.BOMB)

        for bomb in bombs_coords:
            neighbors = self.get_neighbors(*bomb)
            for r, c in neighbors:
                if self.field[r][c].get_cell_type() != CellType.BOMB:
                    self.field[r][c].increment_adjacent_bombs()

    def inside(self, r, c):
        return r >= 0 and c >= 0 and r < self.SIZE and c < self.SIZE


    def get_neighbors(self, row, col):
        neighbors = []
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc
            if self.inside(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors

