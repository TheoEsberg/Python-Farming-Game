from pytmx import load_pygame, TiledTileLayer
import pytmx, os

path = os.path.dirname(__file__)
os.chdir(path)

class Map:
    def __init__(self, handler):
        self.handler = handler
        self.displayWidth = handler.displayWidth
        self.displayHeight = handler.displayHeight
        self.display = handler.display

    def render(self):
        self.ti = self.handler.currentMap.get_tile_image_by_gid
        xStart = max(0, self.handler.camera.xOffset / self.handler.currentMap.tilewidth)
        xEnd = min(self.handler.currentMap.width, (self.handler.camera.xOffset + self.handler.displayWidth) / self.handler.currentMap.tilewidth + 1)
        yStart = max(0, self.handler.camera.yOffset / self.handler.currentMap.tileheight)
        yEnd = min(self.handler.currentMap.height, (self.handler.camera.yOffset + self.handler.displayHeight) / self.handler.currentMap.tileheight + 1)

        for i in range(len(self.handler.currentMap.layers) - 1):
            for x in range(int(xStart), int(xEnd)):
                for y in range(int(yStart), int(yEnd)):
                    tile = self.handler.currentMap.get_tile_image(x, y, i)
                    if (tile):
                        self.display.blit(tile, (x * self.handler.currentMap.tilewidth - self.handler.camera.xOffset,
                                                 y * self.handler.currentMap.tileheight - self.handler.camera.yOffset))
          
