from pytmx import load_pygame, TiledTileLayer
import pytmx, libs.timer

class Map:
    def __init__(self, handler):
        self.handler = handler
        self.displayWidth = handler.displayWidth
        self.displayHeight = handler.displayHeight
        self.display = handler.display

        self.timer = libs.timer.Timer(500)
        self.timer.start()
        self.animIndex = 0

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

    def rendering(self):
        for gid, props in self.handler.currentMap.tile_properties.items():
            for animation_frame in props["frames"]:
                print(animation_frame)
                print(animation_frame.gid)
                image = self.handler.currentMap.get_tile_image_by_gid(animation_frame.gid)
                self.display.blit(image, (200, 200))

    def tickAnimIndex(self):
        self.timer.update()
        # if (self.timer.isDone()):
        #     if(self.animIndex == 0):
        #         self.animIndex = 1
        #     elif (self.animIndex == 1): 
        #         self.animIndex = 0
        #     self.timer.start()
        # print(self.animIndex)

    def renderingDoneRight(self):
        self.timer.update()
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

                    gid = self.handler.currentMap.get_tile_gid(x, y, i)
                    for gid, props in self.handler.currentMap.tile_properties.items():

                        if(self.timer.isDone()):
                            tile = self.handler.currentMap.get_tile_image_by_gid(props["frames"][0].gid)
                            self.display.blit(tile, (x * self.handler.currentMap.tilewidth - self.handler.camera.xOffset,
                                                        y * self.handler.currentMap.tileheight - self.handler.camera.yOffset))
                            self.timer.start()
                            if (self.timer.isDone()):
                                print("This should change it")
                                tile = self.handler.currentMap.get_tile_image_by_gid(props["frames"][0].gid)
                                self.display.blit(tile, (x * self.handler.currentMap.tilewidth - self.handler.camera.xOffset,
                                                        y * self.handler.currentMap.tileheight - self.handler.camera.yOffset))


                        
                            # print(props["id"])

                            # for animation_frame in props["frames"]:
                            #     if (self.timer.isDone()):
                            #         tile = self.handler.currentMap.get_tile_image_by_gid(animation_frame.gid)
                            #         self.display.blit(tile, (x * self.handler.currentMap.tilewidth - self.handler.camera.xOffset,
                            #                                  y * self.handler.currentMap.tileheight - self.handler.camera.yOffset))
                            #         self.timer.start()
                                   

        # for gid, props in self.handler.currentMap.tile_properties.items():
            

        # for gid, props in self.handler.currentMap.tile_properties.items():
        #     print(self.handler.currentMap.tile_properties)
        #     for i in range(len(props["frames"])):
                
        #         pass 

        #     for animation_frame in props["frames"]:
        #         pass

        
                


                                                

                    
          
