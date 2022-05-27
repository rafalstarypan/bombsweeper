"""
MainWindow module
"""

import pygame
# from GameSquareGrid import GameSquareGrid
# from MessageWindow import MessageWindow
from pathlib import Path
import os

class MainWindow():
    """
    MainWindow class.

    Class created for convienient game GUI managing of GameStatus. Processes event handling,
    shows information about side to move and processes to final window when game ends.
    """

    __side_icon_size = 100

    __background_color = (200, 200, 200)

    def __init__(self, game_status):
        """
        Create MainWindow representing game_status.
        """

        self.__gs = game_status
        """
        Pointer to GameStatus object.
        """

        self.__screen = pygame.display.set_mode((1200, 700), 0, 32)
        """
        pygame.surface object, on which all GUI elements will be displayed.
        """
        self.__screen.fill(MainWindow.__background_color)


        self.__final_message = None
        """
        MessageWindow object used when game will end.
        """

        self.__gsg = GameSquareGrid(self.__screen, 20, 150, self.__gs.playerBoard, self.__gs.opponentBoard)
        """
        GameSquareGrid object pointer with positioned (x, y) coords and 2 boards.
        """

        self.__game_in_progress = False
        """
        Boolean value storing whether game still in progress.
        """

        pygame.init()
        pygame.display.set_caption("BombSweeper")
        pygame.display.set_icon(self.__program_icon)
                       

    def start_game(self):
        """
        Start and process game.
        Process event handling.
        When game is ended show final MessageWindow and return.
        """
        self.__game_in_progress = True
        self.__gsg.reset_gridUI()

        while self.__game_in_progress:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_in_progress = False

                if self.__gs.get_player_to_move() == 1:
                    is_move_done, is_move_accurate = self.__gsg.handle_event(event)
                    
                    if is_move_done:
                        if not is_move_accurate:
                            self.__gs.change_player_to_move()

                    if self.__gs.has_game_ended():
                        self.__game_in_progress = False

            if self.__gs.get_player_to_move() == 0:
                self.__show_cpu_icon()
                self.__gs.make_AI_move()
                self.__gsg.reset_gridUI()

                if self.__gs.has_game_ended():
                    self.__game_in_progress = False
    
            else:
                self.__show_player_icon()
        
        pygame.quit()
        if not self.__gs.opponentBoard.is_defeated():
            self.__final_message = MessageWindow("You lost the game", "game-lost.png")
        else:
            self.__final_message = MessageWindow("You won the game", "game-won.png")