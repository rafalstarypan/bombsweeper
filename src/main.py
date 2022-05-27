"""
main module used to run program
"""

from game_rules import *
from bomb_field import *
from main_window import MainWindow

def main():
    """ 
    main function of project
    """
    main_window = MainWindow(game_mode=GameMode.EASY)
    main_window.run_game()


if __name__ == "__main__":
    main()
