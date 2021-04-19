
class Inputs():
    def __init__(self, handler):
        self.handler = handler
        self.keys = self.handler.pygame.key.get_pressed()
        
    def checkForInputs(self):
        self.keys = self.handler.pygame.key.get_pressed()

    def movementInputs(self):
        if (self.up() or self.down() or self.left() or self.right()):
            return True

    def shift(self):
        if (self.keys[self.handler.pygame.K_LSHIFT] or self.keys[self.handler.pygame.K_RSHIFT]):
            return True

    def up(self):
        if (self.keys[self.handler.pygame.K_UP] or self.keys[self.handler.pygame.K_w]):
            return True
    
    def down(self):
        if (self.keys[self.handler.pygame.K_DOWN] or self.keys[self.handler.pygame.K_s]):
            return True
    
    def left(self):
        if (self.keys[self.handler.pygame.K_LEFT] or self.keys[self.handler.pygame.K_a]):
            return True
    
    def right(self):
        if (self.keys[self.handler.pygame.K_RIGHT] or self.keys[self.handler.pygame.K_d]):
            return True
    
