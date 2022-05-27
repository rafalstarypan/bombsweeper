from cell import *
from game_rules import *
import random
from queue import Queue 

class BombFieldGrid:
    def __init__(self, game_mode: GameMode):
        self.game_mode = game_mode
        self.reset()
    

    def reset(self):
        self.SIZE = GameRules.get_bomb_field_size(game_mode=self.game_mode)
        self.BOMBS_COUNT = GameRules.get_bombs_count(game_mode=self.game_mode)
        self.REMAINING_FLAGS = GameRules.get_flags_count(game_mode=self.game_mode)

        self.is_covered = [[True] * self.SIZE for _ in range(self.SIZE)]
        self.field = [[Cell(CellType.EMPTY) for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.flag_coords = set()
        self.uncovered_cells = 0
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


    def is_bomb(self, row, col):
        if not self.inside(row, col): return False
        return self.field[row][col].get_cell_type() == CellType.BOMB


    def is_flag(self, row, col):
        return (row, col) in self.flag_coords


    def is_empty(self, row, col):
        if not self.inside(row, col): return False
        return self.field[row][col].get_cell_type() == CellType.EMPTY and not self.is_flag(row, col)


    def uncover_cell(self, row, col):
        if not self.inside(row, col):
            return
        if self.is_bomb(row, col) or self.is_flag(row, col):
            return
        if not self.is_covered[row][col]:
            return
        
        self.__uncover_from_pos(row, col)


    def uncover_bombs(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.is_bomb(i, j):
                    self.is_covered[i][j] = False


    def flag_cell(self, row, col):
        if not self.is_cell_covered(row, col):
            return
        if (row, col) in self.flag_coords:
            self.flag_coords.remove((row, col))
            self.REMAINING_FLAGS += 1
            return
        if self.REMAINING_FLAGS == 0:
            return
        self.flag_coords.add((row, col))
        self.REMAINING_FLAGS -= 1


    def __uncover_from_pos(self, row, col):
        q = Queue()
        q.put((row, col))
        self.is_covered[row][col] = False
        self.uncovered_cells += 1
        visited = set()

        while not q.empty():
            current = q.get()

            neighbors = self.get_neighbors(*current)
            for r, c in neighbors:
                if (r, c) in visited:
                    continue
                
                cell = self.field[r][c]
                if self.is_empty(r, c) and cell.get_adjacent_bombs() == 0 and self.is_covered[r][c]:
                    q.put((r, c))
                if self.is_empty(r, c) and self.is_covered[r][c]:
                    self.is_covered[r][c] = False
                    self.uncovered_cells += 1
                
                visited.add((r, c))


    def inside(self, r, c):
        return r >= 0 and c >= 0 and r < self.SIZE and c < self.SIZE


    def get_size(self):
        return self.SIZE


    def get_remaining_flags(self):
        return self.REMAINING_FLAGS


    def get_neighbors(self, row, col):
        neighbors = []
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc
            if self.inside(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors


    def get_adjacent_bombs_count(self, row, col):
        return self.field[row][col].get_adjacent_bombs()


    def is_cell_covered(self, row, col):
        return self.is_covered[row][col]


    def is_bomb_hit(self, row, col):
        return self.field[row][col].get_cell_type() == CellType.BOMB


    def is_victory(self):
        return self.uncovered_cells == self.SIZE*self.SIZE - self.BOMBS_COUNT


    def get_cell_type(self, row, col):
        return self.field[row][col].get_cell_type()

