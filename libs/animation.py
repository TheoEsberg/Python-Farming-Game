import libs.timer as time

class Animation():
    def __init__(self, sprites, speed, handler):
        self.sprites = sprites
        self.speed = speed
        self.handler = handler
        self.timer = time.Timer(speed)
        self.imgIndex = 0
        self.timer.start()
        
    def getCurrentImage(self, isFlipped):
        if (self.speed == 0):
            self.imgIndex = 0
            if (isFlipped):
                return self.handler.pygame.transform.flip(self.sprites[0], True, False)
            return self.sprites[0]

        self.timer.update()
        if (self.timer.isDone()):
            if (self.imgIndex != len(self.sprites) - 1):
                self.imgIndex += 1
            else:
                self.imgIndex = 0
            self.timer.start()

        if (isFlipped):
            return self.handler.pygame.transform.flip(self.sprites[self.imgIndex], True, False)
        else: 
            return self.sprites[self.imgIndex]
    
        