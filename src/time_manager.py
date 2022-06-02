import time

class TimeManager:
    def __init__(self):
        self.reset()

    
    def reset(self):
        self.__start_time = time.time()

    
    def get_game_time(self):
        return int(round(time.time() - self.__start_time))