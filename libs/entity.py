from abc import ABC, abstractmethod

entities = []
class Entity:
    def __init__(self, x, y, width, height, layer, handler):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height
        self.layer = layer 
        
        self.handler = handler
        self.pygame = handler.pygame
        self.display = handler.display
        self.allowTick = True

        entities.append(self)

    @abstractmethod
    def tick(self):
        pass
