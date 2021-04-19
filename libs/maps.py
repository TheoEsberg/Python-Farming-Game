from pytmx import load_pygame, TiledTileLayer
import pytmx, libs.timer, libs.tileAnimation

class Map:
    def __init__(self, handler):
        self.handler = handler
        self.displayWidth = handler.displayWidth
        self.displayHeight = handler.displayHeight
        self.display = handler.display

        self.timer = libs.timer.Timer(500)
        self.timer.start()
        self.timer2 = libs.timer.Timer(500)
        self.animIndex = 0

        self.animations = {}
        for gid, props in self.handler.currentMap.tile_properties.items():
            imgs = []
            for animation_frame in props['frames']:
                imgs.append(self.handler.currentMap.get_tile_image_by_gid(animation_frame.gid))
            print(imgs)
            imgs.pop(len(imgs) -1)
            anim = libs.tileAnimation.tileAnimation(imgs, props["frames"][0].duration, self.handler, gid)
            self.animations[gid] = anim
        
    def renderingDoneRight(self):
        xStart = max(0, self.handler.camera.xOffset / self.handler.currentMap.tilewidth)
        xEnd = min(self.handler.currentMap.width, (self.handler.camera.xOffset + self.handler.displayWidth) / self.handler.currentMap.tilewidth + 1)
        yStart = max(0, self.handler.camera.yOffset / self.handler.currentMap.tileheight)
        yEnd = min(self.handler.currentMap.height, (self.handler.camera.yOffset + self.handler.displayHeight) / self.handler.currentMap.tileheight + 1)

        for i in range(len(self.handler.currentMap.layers) - 1):
            for x in range(int(xStart), int(xEnd)):
                for y in range(int(yStart), int(yEnd)):
                    tile = self.handler.currentMap.get_tile_image(x, y, i)
                    if (tile):
                        gid = self.handler.currentMap.get_tile_gid(x, y, i)
                        if (gid in self.animations):
                            self.animations[gid].tick(x, y)
                            continue

                        self.display.blit(tile, (x * self.handler.currentMap.tilewidth - self.handler.camera.xOffset,
                                                 y * self.handler.currentMap.tileheight - self.handler.camera.yOffset))

                        

