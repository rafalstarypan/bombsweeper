from game_controller import GameStatus
from game_rules import GameMode
import pygame

class WelcomeView:
    """
    View class responsible for the welcome window where
    the player has to give their nickname and select
    the difficulty mode
    """

    __WIDTH = 700
    """
    Width of the window
    """
    __HEIGHT = 800
    """
    Height of the window
    """

    def __init__(self):
        """
        Initializes the object with required Pygame
        attributes 
        """
        self.__selected_game_mode = None
        self.__player = ""
        self.__active_input = False
        self.__ready = False

        pygame.init()
        self.__screen = pygame.display.set_mode((700, 700), 0, 32)
        pygame.display.set_caption("Start the game")
        self.__HEADER_FONT = pygame.font.SysFont('comicsans', 40)
        self.__BUTTON_FONT = pygame.font.SysFont('comicsans', 30)

    
    def __draw(self):
        """
        Displays the content inside the window
        """
        self.__screen.fill((155,155,155))

        header_text = self.__HEADER_FONT.render("Enter your nick", 0.5, "black")
        game_mode_header = pygame.Rect(100, 50, 500, 500)
        self.__screen.blit(header_text, game_mode_header)

        self.__player_input = pygame.Rect(100, 130, 400, 50)
        input_color = "grey" if self.__active_input else "white" 
        pygame.draw.rect(self.__screen, input_color, self.__player_input) 

        player_text = self.__BUTTON_FONT.render(self.__player, 0.5, "black")
        player_text_wrapper = pygame.Rect(110, 135, 400, 50)
        self.__screen.blit(player_text, player_text_wrapper)
        
        header_text = self.__HEADER_FONT.render("Choose the difficulty mode", 0.5, "black")
        game_mode_header = pygame.Rect(100, 200, 500, 500)
        self.__screen.blit(header_text, game_mode_header)

        self.__easy_mode_button = pygame.Rect(265, 286, 190, 50)
        self.__medium_mode_button  = pygame.Rect(265, 330, 190, 50)
        self.__hard_mode_button = pygame.Rect(265, 380, 190, 50)
        self.__play_button = pygame.Rect(100, 480, 500, 50)

        easy_button_color = "green"
        medium_button_color = "orange"
        hard_button_color = "red"
        if self.__selected_game_mode == GameMode.EASY:
            easy_button_color = "darkgreen"
            medium_button_color = "lightgrey"
            hard_button_color = "lightgrey"
        if self.__selected_game_mode == GameMode.MEDIUM:
            easy_button_color = "lightgrey"
            medium_button_color = "darkorange"
            hard_button_color = "lightgrey"
        if self.__selected_game_mode == GameMode.HARD:
            easy_button_color = "lightgrey"
            medium_button_color = "lightgrey"
            hard_button_color = "darkred"
        play_button_color = "blue" if self.__ready else "lightgrey"

        t_easy = pygame.Rect(295, 286, 190, 50)
        t_medium = pygame.Rect(295, 334, 190, 50)
        t_hard = pygame.Rect(295, 384, 190, 50)
        t_play = pygame.Rect(310, 483, 100, 50)

        for txt, color, btn, trect in \
            [["EASY",    easy_button_color,  self.__easy_mode_button,   t_easy], 
             ["MEDIUM",  medium_button_color,     self.__medium_mode_button, t_medium],
             ["HARD",    hard_button_color,        self.__hard_mode_button,   t_hard],
             ["PLAY",    play_button_color,  self.__play_button,               t_play]]:

            textField = self.__BUTTON_FONT.render(txt, 0.5, "white")
            pygame.draw.rect(self.__screen, color, btn) 
            self.__screen.blit(textField, trect)

        pygame.display.update()

    
    def display(self):
        """
        Handles player's events and refreshes the displayed content
        """
        while True:
            self.__draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return (None, None)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDownStartPos = event.pos
                    mouse_pressed = pygame.mouse.get_pressed()

                    if mouse_pressed[0]:  
                        if self.__easy_mode_button.collidepoint(mouseDownStartPos):
                            self.__selected_game_mode = GameMode.EASY
                        elif self.__medium_mode_button.collidepoint(mouseDownStartPos):
                            self.__selected_game_mode = GameMode.MEDIUM
                        elif self.__hard_mode_button.collidepoint(mouseDownStartPos):
                            self.__selected_game_mode = GameMode.HARD
                        elif self.__player_input.collidepoint(mouseDownStartPos):
                            self.__active_input = not self.__active_input
                        elif self.__play_button.collidepoint(mouseDownStartPos):
                            if self.__ready:
                                pygame.quit()
                                return (self.__player, self.__selected_game_mode)
                        else:
                            self.__active_input = False

                if event.type == pygame.KEYDOWN:
                    if self.__active_input:
                        if event.key == pygame.K_BACKSPACE:
                            if self.__player != "": 
                                self.__player = self.__player[:-1]
                        else:
                            self.__player += event.unicode
                
                self.__ready = (self.__player and self.__selected_game_mode)
           
