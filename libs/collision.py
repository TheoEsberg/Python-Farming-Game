import pytmx
from pytmx import load_pygame, TiledTileLayer

class Collision:
    def __init__(self, entity, handler):
        self.entity = entity
        self.handler = handler

    def CheckCollision(self, x, y):
        entityCol = self.handler.pygame.Rect(self.entity.x - 24 + x - self.handler.camera.xOffset, 
                                             self.entity.y - 24 + y - self.handler.camera.yOffset, 48, 48)
        
        for tile_object in self.handler.currentMap.objects:
            if (self.handler.pygame.Rect(tile_object.x - (self.handler.currentMap.tilewidth / 2) - self.handler.camera.xOffset,
                                         tile_object.y - (self.handler.currentMap.tileheight / 2) - self.handler.camera.yOffset,
                                         tile_object.width, tile_object.height).colliderect(entityCol) == True):
                
                if (tile_object.name == "wall"):
                    print("HIT A WALL")
                    return "wall"
        return False
    
