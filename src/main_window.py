import pygame
import time
from game_rules import *
from bomb_field import *

class GameStatus(Enum):
    IN_PROGRESS = auto()
    LOST        = auto()
    VICTORY     = auto()


class MainWindow:
    __WIDTH = 700
    __HEIGHT = 800
    __BG_COLOR = "white"
    __FLAG_COLOR = "green"
    __RECT_COLOR = (200, 200, 200)
    __CLICKED_RECT_COLOR = (140, 140, 140)
    __BOMB_COLOR = "red"
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

    def __init__(self, game_mode: GameMode):
        self.bomb_field = BombFieldGrid(game_mode=game_mode)
        self.start_time = time.time()
        self.CELL_SIZE =  MainWindow.__WIDTH / self.bomb_field.get_size()
        self.game_status = GameStatus.IN_PROGRESS

        pygame.init()
        self.win = pygame.display.set_mode((MainWindow.__WIDTH, MainWindow.__HEIGHT))
        pygame.display.set_caption("BombSweeper")
        self.__NUM_FONT = pygame.font.SysFont('comicsans', 20)
        self.__FINAL_FONT = pygame.font.SysFont('comicsans', 70)
        self.__TIME_FONT = pygame.font.SysFont('comicsans', 40)
        

    def draw(self):
        current_time = time.time() - self.start_time
        self.win.fill(MainWindow.__BG_COLOR)
        time_text = self.__TIME_FONT.render(f"Your time: {round(current_time)}", 1, "black")
        flag_text = self.__TIME_FONT.render(f"Remaining flags: {self.bomb_field.get_remaining_flags()}", 1, "black")
        self.win.blit(time_text, (10, MainWindow.__HEIGHT - time_text.get_height()))
        self.win.blit(flag_text, (300, MainWindow.__HEIGHT - time_text.get_height()))

        for i in range(self.bomb_field.get_size()):
            for j in range(self.bomb_field.get_size()):
                y = self.CELL_SIZE * i
                x = self.CELL_SIZE * j

                if self.bomb_field.is_flag(i, j):
                    pygame.draw.rect(self.win, MainWindow.__FLAG_COLOR, (x, y, self.CELL_SIZE, self.CELL_SIZE))
                    pygame.draw.rect(self.win, "black", (x, y, self.CELL_SIZE, self.CELL_SIZE), 2)
                    continue

                if self.bomb_field.is_cell_covered(i, j):
                    pygame.draw.rect(self.win, MainWindow.__RECT_COLOR, (x, y, self.CELL_SIZE, self.CELL_SIZE))
                    pygame.draw.rect(self.win, "black", (x, y, self.CELL_SIZE, self.CELL_SIZE), 2)
                    continue
                
                pygame.draw.rect(self.win, MainWindow.__CLICKED_RECT_COLOR, (x, y, self.CELL_SIZE, self.CELL_SIZE))

                if self.bomb_field.is_bomb(i, j):
                    pygame.draw.circle(self.win, MainWindow.__BOMB_COLOR, (x + self.CELL_SIZE/2, y + self.CELL_SIZE/2), self.CELL_SIZE/2 - 4)
                else:
                    pygame.draw.rect(self.win, "black", (x, y, self.CELL_SIZE, self.CELL_SIZE), 2)

                if (bombs := self.bomb_field.get_adjacent_bombs_count(i, j)) > 0:
                    text = self.__NUM_FONT.render(str(bombs), 1, MainWindow.__NUM_COLORS[bombs])
                    self.win.blit(text, (x + (self.CELL_SIZE/2 - text.get_width()/2), y + (self.CELL_SIZE/2 - text.get_height()/2)))

        pygame.display.update()


    def draw_final_message(self, text):
        text = self.__FINAL_FONT.render(text, 1, "black")
        self.win.blit(text, (MainWindow.__WIDTH/2 - text.get_width()/2,
                    MainWindow.__HEIGHT/2 - text.get_height()/2))
        pygame.display.update()


    def __get_grid_pos(self, mouse_pos):
        mx, my = mouse_pos
        row = int(my // self.CELL_SIZE)
        col = int(mx // self.CELL_SIZE)
        return (row, col)   


    def complete_lost_game(self):
        self.bomb_field.uncover_bombs()
        self.draw()
        self.bomb_field.reset()
        self.draw_final_message("You lost! Try again...")
        pygame.time.delay(5000)
        self.game_status = GameStatus.IN_PROGRESS
        self.start_time = time.time()


    def complete_victory_game(self):
        self.draw()
        self.bomb_field.reset()
        game_time = time.time() - self.start_time
        self.draw_final_message(f"You won in {int(game_time)} s")
        pygame.time.delay(5000)
        self.game_status = GameStatus.IN_PROGRESS
        self.start_time = time.time()


    def run_game(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.__get_grid_pos(pygame.mouse.get_pos()) 
                    mouse_pressed = pygame.mouse.get_pressed()

                    if mouse_pressed[0]:     
                        self.bomb_field.uncover_cell(row, col)

                        if self.bomb_field.is_bomb(row, col): 
                            self.game_status = GameStatus.LOST

                        if self.bomb_field.is_victory():
                            self.game_status = GameStatus.VICTORY

                    elif mouse_pressed[2]:
                        self.bomb_field.flag_cell(row, col)
            
                if self.game_status == GameStatus.LOST:
                    self.complete_lost_game()
                elif self.game_status == GameStatus.VICTORY:
                    self.complete_victory_game()

                self.draw()
        pygame.quit()