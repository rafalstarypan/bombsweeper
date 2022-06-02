from game_controller import GameStatus
from game_rules import GameMode
import pygame

class WelcomeView:
    __WIDTH = 700
    __HEIGHT = 800

    def __init__(self):
        self.__selected_game_mode = None
        pygame.init()
        self.__screen = pygame.display.set_mode((600, 600), 0, 32)
        pygame.display.set_caption("Start the game")
        self.__HEADER_FONT = pygame.font.SysFont('comicsans', 40)
        self.__BUTTON_FONT = pygame.font.SysFont('comicsans', 30)

    
    def __draw(self):
        self.__screen.fill((155,155,155))
        self.__easy_mode_button = pygame.Rect(210, 156, 190, 50)
        self.__medium_mode_button  = pygame.Rect(210, 200, 190, 50)
        self.__hard_mode_button = pygame.Rect(210, 250, 190, 50)

        t_easy = pygame.Rect(240, 156, 190, 50)
        t_medium = pygame.Rect(240, 204, 190, 50)
        t_hard = pygame.Rect(240, 254, 190, 50)

        header_text = self.__HEADER_FONT.render("Choose the difficulty mode", 0.5, "black")
        game_mode_header = pygame.Rect(50, 50, 500, 500)
        self.__screen.blit(header_text, game_mode_header)

        for txt, color, btn, trect in \
            [["EASY",    "green",  self.__easy_mode_button,   t_easy], 
             ["MEDIUM",  "orange", self.__medium_mode_button, t_medium],
             ["HARD",    "red",    self.__hard_mode_button,   t_hard]]:

            textField = self.__BUTTON_FONT.render(txt, 0.5, "white")
            pygame.draw.rect(self.__screen, color, btn) 
            self.__screen.blit(textField, trect)

        pygame.display.update()

    
    def display(self):
        while not self.__selected_game_mode:
            self.__draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return self.__selected_game_mode

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
           
        pygame.quit()
        return self.__selected_game_mode
