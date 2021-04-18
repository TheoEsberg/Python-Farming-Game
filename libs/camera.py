class Camera:
    def __init__(self, handler):
        self.handler = handler
        self.xOffset = 0
        self.yOffset = 0

    def cameraPos(self, entity):
        #   If the map width is bigger than the display width, this will center the camera on the X-axis
        if ((self.handler.currentMap.width * self.handler.currentMap.tilewidth) > self.handler.displayWidth):
            self.xOffset = max(0, min(self.handler.currentMap.width * self.handler.currentMap.tilewidth - self.handler.displayWidth, entity.x + (entity.width/2) - (self.handler.displayWidth / 2)))
        else:
            #   If the map width is'nt bigger than the display width, this will center the camera on the X-axis
            self.xOffset = (self.handler.currentMap.width * self.handler.currentMap.tilewidth) / 2 - (self.handler.displayHeight / 2)

        #   If the map height is bigger than the display height, this will center the camera on the Y-axis
        if ((self.handler.currentMap.height * self.handler.currentMap.tileheight) > self.handler.displayHeight):
            self.yOffset = max(0, min(self.handler.currentMap.height * self.handler.currentMap.tileheight - self.handler.displayHeight, entity.y + (entity.height/2) - (self.handler.displayHeight / 2)))
        else:
            #   If the map height is'nt bigger than the display height, this will center the camera on the Y-axis
            self.yOffset = (self.handler.currentMap.height * self.handler.currentMap.tileheight) / 2 - (self.handler.displayHeight / 2)

        

        