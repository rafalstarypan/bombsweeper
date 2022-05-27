"""
main module used to run program
"""

# from game_status import GameStatus
from game_rules import *
from bomb_field import *

def main():
    """ 
    main function of project
    """
    # gs = GameStatus()
    grid = BombFieldGrid(game_mode=GameMode.HARD)
    for i in range(grid.SIZE):
        for j in range(grid.SIZE):
            print(grid.field[i][j], end='')
        print()


if __name__ == "__main__":
    main()
