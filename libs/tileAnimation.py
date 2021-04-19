import libs.animation

class tileAnimation:
    def __init__(self, tiles, duration, handler, id):
        self.tiles = tiles 
        self.duration = duration
        self.handler = handler

        self.anim = libs.animation.Animation(self.tiles, self.duration)

    def tick(self, tileX, tileY):
        img = self.anim.getCurrentImage(False)
        self.handler.display.blit(img, (tileX * self.handler.currentMap.tilewidth - self.handler.camera.xOffset,
                                        tileY * self.handler.currentMap.tileheight - self.handler.camera.yOffset))


                                

