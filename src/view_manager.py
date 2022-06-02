from welcome_view import *
from main_window import *

class ViewManager:
    def __init__(self):
        self.__welcome_view = WelcomeView()
        nickname, selected_game_mode = self.__welcome_view.display()
        if not selected_game_mode:
            return

        self.__main_view = MainView(game_mode=selected_game_mode, nickname=nickname)
        self.__main_view.run_game()


