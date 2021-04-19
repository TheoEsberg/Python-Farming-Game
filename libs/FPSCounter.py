import math

class FPS():
    def __init__(self, handler, clock):
        self.handler = handler
        self.clock = clock
        self.font = self.handler.pygame.font.Font("res/fonts/PIXELADE.TTF", 32)

    def tick(self):
        self.fps = self.font.render("FPS: " + str(math.floor(self.clock.get_fps())), True, (255, 255, 255))
        self.handler.display.blit(self.fps, (16, 16))