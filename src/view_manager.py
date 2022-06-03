from summary_view import SummaryView
from welcome_view import *
from main_window import *
from game_rules import GameRestart

class ViewManager:
    def __init__(self):
        pass


    def manage_game_cycle(self):
        game_restart = GameRestart.CHANGE_MODE
        nickname, selected_game_mode = None, None

        while True:
            if not game_restart:
                return

            if game_restart == GameRestart.CHANGE_MODE:
                welcome_view = WelcomeView()
                nickname, selected_game_mode = welcome_view.display()

            if not selected_game_mode:
                return

            main_view = MainView(game_mode=selected_game_mode, nickname=nickname)
            nickname, game_status, game_time = main_view.run_game()

            summary_view = SummaryView(game_status=game_status, nickname=nickname, game_time=game_time)
            game_restart = summary_view.display()
            
