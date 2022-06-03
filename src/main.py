"""
main module used to run the program
"""
from view_manager import ViewManager

def main():
    """ 
    main function of the project
    """
    view_manager = ViewManager()
    view_manager.manage_game_cycle()


if __name__ == "__main__":
    main()
