from game_controller import GameStatus
from game_rules import GameRestart
import pygame

class SummaryView:
    """
    Summary view class responsible for displaying the game result information.
    It allows the player to retry the game or to go back to the welcome view
    in order to change nickname and/or game difficulty
    """

    __WIDTH = 700
    """
    Width of the window
    """

    __HEIGHT = 800
    """
    Height of the window
    """

    def __init__(self, game_status: GameStatus, nickname: str, game_time: int):
        """
        Initializes the object with required Pygame
        attributes 
        """
        self.__game_status = game_status
        self.__nickname = nickname
        self.__game_time = game_time

        pygame.init()
        self.__screen = pygame.display.set_mode((800, 800), 0, 32)
        pygame.display.set_caption("Game summary")
        self.__HEADER_FONT = pygame.font.SysFont('comicsans', 40)
        self.__BUTTON_FONT = pygame.font.SysFont('comicsans', 30)

    
    def __get_summary_message(self):
        """
        Returns the final player's message depending on the result of the game
        """
        if self.__game_status == GameStatus.VICTORY:
            return (f"Congrats {self.__nickname}!", f"You won in {self.__game_time} s")
        return (f"Sorry {self.__nickname}.", "You lost :(")


    def __get_image_filepath(self):
        """
        Returns the image filepath depending on the result of the game
        """
        if self.__game_status == GameStatus.VICTORY:
            return "images/victory.png"
        return "images/lost.png"


    def __draw(self):
        """
        Displays the content inside the window
        """
        self.__screen.fill((155,155,155))

        player_msg, result_msg = self.__get_summary_message()
        header_text = self.__HEADER_FONT.render(player_msg, 0.5, "black")
        player_msg_header = pygame.Rect(175, 50, 600, 600)
        self.__screen.blit(header_text, player_msg_header)

        header_text = self.__HEADER_FONT.render(result_msg, 0.5, "black")
        result_msg_header = pygame.Rect(175, 110, 600, 600)
        self.__screen.blit(header_text, result_msg_header)

        image_filepath = self.__get_image_filepath()
        image = pygame.image.load(image_filepath).convert() 
        rect = image.get_rect()
        rect.topleft = (200, 200)
        self.__screen.blit(image, rect)

        self.__retry_button = pygame.Rect(175, 700, 200, 50)
        t_retry = pygame.Rect(237, 702, 200, 50)
        textField = self.__BUTTON_FONT.render("Retry", 0.5, "white")
        pygame.draw.rect(self.__screen, "green", self.__retry_button) 
        self.__screen.blit(textField, t_retry)

        self.__change_mode_button = pygame.Rect(425, 700, 200, 50)
        t_change_mode = pygame.Rect(432, 702, 200, 50)
        textField = self.__BUTTON_FONT.render("Change mode", 0.5, "white")
        pygame.draw.rect(self.__screen, "orange", self.__change_mode_button) 
        self.__screen.blit(textField, t_change_mode)

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
                    return None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDownStartPos = event.pos
                    mouse_pressed = pygame.mouse.get_pressed()

                    if mouse_pressed[0]:  
                        if self.__retry_button.collidepoint(mouseDownStartPos):
                            return GameRestart.RETRY
                        if self.__change_mode_button.collidepoint(mouseDownStartPos):
                            return GameRestart.CHANGE_MODE

