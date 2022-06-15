import time

class TimeManager:
    """
    Class measures the time of the game and passes it 
    to the controller when needed
    """
    def __init__(self):
        """
        Initializes the object
        """
        self.reset()

    
    def reset(self):
        """
        Resets the object state setting the current time
        as the object field 
        """
        self.__start_time = time.time()

    
    def get_game_time(self):
        """
        Returns the duration of the game in seconds
        """
        return int(round(time.time() - self.__start_time))