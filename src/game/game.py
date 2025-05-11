class Game:
    def __init__(self):
        self.terminate = False
        self.levels = []

    def run(self):
        # initialize the game
        self._init()
        
        # main loop
        while not self.terminate:
            self._draw()
        
        # terminate the game
        self._quit()

    def _init(self):
        pass

    def _draw(self):
        print("hello")
        self.terminate = True
    
    def _quit(self):
        pass
