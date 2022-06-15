import pygame
import time
from game_rules import *
from game_controller import *


class MainView:
    """
    Main view class of the game window.
    It is responsible for all the visual functionalities
    in accordance with the game rules
    """

    __WIDTH = 700
    """
    Width of the window
    """

    __HEIGHT = 800
    """
    Height of the window
    """

    __BG_COLOR = "white"
    """
    Background color
    """

    __RECT_COLOR = (200, 200, 200)
    """
    Covered cell color
    """

    __CLICKED_RECT_COLOR = (140, 140, 140)
    """
    Uncovered cell color
    """

    __BOMB_COLOR = "red"
    """
    Revealed bombs color
    """

    __NUM_COLORS = {
        1: "black", 
        2: "green", 
        3: "red", 
        4: "orange",
        5: "yellow",
        6: "purple",
        7: "blue",
        8: "pink",
    }
    """
    Adjacent bombs count information colors
    """

    def __init__(self, game_mode: GameMode, nickname: str):
        """
        Initializes the object with required Pygame
        attributes as well as the GameController instance
        """
        self.__game_controller = GameController(game_mode, nickname)
        self.__CELL_SIZE =  MainView.__WIDTH / self.__game_controller.get_size()
        
        pygame.init()
        self.__win = pygame.display.set_mode((MainView.__WIDTH, MainView.__HEIGHT))
        pygame.display.set_caption("BombSweeper")
        self.__NUM_FONT = pygame.font.SysFont('comicsans', 20)
        self.__FINAL_FONT = pygame.font.SysFont('comicsans', 70)
        self.__TIME_FONT = pygame.font.SysFont('comicsans', 40)
        

    def __draw(self):
        """
        Displays the content inside the window
        """
        self.__win.fill(MainView.__BG_COLOR)

        size = self.__game_controller.get_size()
        current_time    = self.__game_controller.get_game_time()
        remaining_flags = self.__game_controller.get_remaining_flags()

        time_text = self.__TIME_FONT.render(f"Your time: {round(current_time)}", 1, "black")
        flag_text = self.__TIME_FONT.render(f"Remaining flags: {remaining_flags}", 1, "black")

        self.__win.blit(time_text, (10, MainView.__HEIGHT - time_text.get_height()))
        self.__win.blit(flag_text, (300, MainView.__HEIGHT - time_text.get_height()))

        for i in range(size):
            for j in range(size):
                y = self.__CELL_SIZE * i
                x = self.__CELL_SIZE * j

                flag_image = pygame.image.load("../images/flag.png").convert() 

                if self.__game_controller.is_flag(i, j):
                    pygame.draw.rect(self.__win, MainView.__RECT_COLOR, (x, y, self.__CELL_SIZE, self.__CELL_SIZE))
                    rect = flag_image.get_rect()
                    rect.center = (x + self.__CELL_SIZE//2, y + self.__CELL_SIZE//2)
                    self.__win.blit(flag_image, rect)
                    pygame.draw.rect(self.__win, "black", (x, y, self.__CELL_SIZE, self.__CELL_SIZE), 2)
                    continue

                if self.__game_controller.is_covered(i, j):
                    pygame.draw.rect(self.__win, MainView.__RECT_COLOR, (x, y, self.__CELL_SIZE, self.__CELL_SIZE))
                    pygame.draw.rect(self.__win, "black", (x, y, self.__CELL_SIZE, self.__CELL_SIZE), 2)
                    continue
                
                pygame.draw.rect(self.__win, MainView.__CLICKED_RECT_COLOR, (x, y, self.__CELL_SIZE, self.__CELL_SIZE))

                if self.__game_controller.is_bomb(i, j):
                    pygame.draw.circle(self.__win, MainView.__BOMB_COLOR, (x + self.__CELL_SIZE/2, y + self.__CELL_SIZE/2), self.__CELL_SIZE/2 - 4)
                else:
                    pygame.draw.rect(self.__win, "black", (x, y, self.__CELL_SIZE, self.__CELL_SIZE), 2)

                if (bombs := self.__game_controller.get_adjacent_bombs_count(i, j)) > 0:
                    text = self.__NUM_FONT.render(str(bombs), 1, MainView.__NUM_COLORS[bombs])
                    self.__win.blit(text, (x + (self.__CELL_SIZE/2 - text.get_width()/2), y + (self.__CELL_SIZE/2 - text.get_height()/2)))

        pygame.display.update()


    def __convert_mouse_coords_to_grid(self, mouse_pos):
        """
        Returns a cell coordinates converted from Pygame
        mouse event coordinates
        """
        mx, my = mouse_pos
        row = int(my // self.__CELL_SIZE)
        col = int(mx // self.__CELL_SIZE)
        return (row, col)   

    
    def __show_all_bombs(self):
        """
        Shows bombs location to the player after a lost game.
        """
        self.__game_controller.uncover_bombs()
        self.__draw()
        pygame.time.delay(5000)


    def run_game(self):
        """
        Handles player's events and refreshes the displayed content
        """
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.__convert_mouse_coords_to_grid(pygame.mouse.get_pos()) 
                    mouse_pressed = pygame.mouse.get_pressed()

                    if mouse_pressed[0]:     
                        self.__game_controller.uncover_cell(row, col)

                    elif mouse_pressed[2]:
                        self.__game_controller.handle_flag_event(row, col)

                status = self.__game_controller.get_game_status()
                if status != GameStatus.IN_PROGRESS:
                    run = False
                    if status == GameStatus.LOST:
                        self.__show_all_bombs()
                    
            self.__draw()
        pygame.quit()
        return self.__game_controller.get_game_summary()