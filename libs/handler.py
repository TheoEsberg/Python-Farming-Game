from pytmx import load_pygame
import pytmx, os

path = os.path.dirname(__file__)
os.chdir(path)

class Handler:
    def __init__(self):
        self.pygame = None
        self.display = None
        self.displayHeight = 800
        self.displayWidth = 1200
        self.camera = None
        self.pygame = None
        self.player = None

        #   Maps 
        self.map = pytmx.load_pygame("res/maps/supermap.tmx", pixelalpha=True)

        self.currentMap = self.map
