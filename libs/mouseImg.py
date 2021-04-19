
class Mouse():
    def __init__(self, handler):
        self.handler = handler
        self.mouseImg = self.handler.pygame.image.load("res/gfx/gui/crosshair.png")
        self.mouseImg = self.handler.pygame.transform.scale(self.mouseImg, (24 * 3, 24 * 3))
        self.handler.pygame.mouse.set_visible(False)

    def tick(self):
        self.x, self.y = self.handler.pygame.mouse.get_pos()
        self.handler.display.blit(self.mouseImg, (self.x - self.mouseImg.get_width()/2, self.y - self.mouseImg.get_height()/2))