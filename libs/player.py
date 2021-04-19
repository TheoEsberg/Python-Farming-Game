import libs.entity as entity
import libs.spriteSheets
import libs.animation as anim
import libs.inputs as inputs
import libs.collision as col


class Player(entity.Entity):
    def __init__(self, x, y, width, height, layer, handler):
        super().__init__(x, y, width, height, layer, handler)

        self.spriteSheet = libs.spriteSheets.SpriteSheets(self.handler)
        self.playerSprites = self.handler.pygame.image.load("res/gfx/player/Player-sprite-sheet.png")
        self.playerIdle = self.spriteSheet.getSprites(self.playerSprites, 24, 24, 1, 1, 4)
        self.playerRight = self.spriteSheet.getSprites(self.playerSprites, 24, 24, 2, 19, 4)
        self.playerRunAnimation = anim.Animation(self.playerRight, 35, self.handler)
        self.playerIdleAnimation = anim.Animation(self.playerIdle, 0, self.handler)
        self.inputs = inputs.Inputs(self.handler)
        self.movementSpeed = 4
        self.isFlipped = False
        self.col = col.Collision(self, self.handler)

    def tick(self):
        self.running()
        self.handler.camera.cameraPos(self)
        self.flipPlayer()
        self.renderPlayer()
        self.inputs.checkForInputs()
        self.movement()
        
    def running(self):
        if (self.inputs.shift()):
            self.movementSpeed = 8
        else: self.movementSpeed = 4

    def flipPlayer(self):
        self.mouseX, self.mouseY = self.handler.pygame.mouse.get_pos()
        if (self.mouseX < (self.x - self.handler.camera.xOffset + 48)):
            self.isFlipped = True
        else: self.isFlipped = False

    def renderPlayer(self):
        if (self.inputs.movementInputs()):
            self.display.blit(self.playerRunAnimation.getCurrentImage(self.isFlipped), (self.x - self.handler.camera.xOffset, self.y - self.handler.camera.yOffset))
        else: self.display.blit(self.playerIdleAnimation.getCurrentImage(self.isFlipped), (self.x - self.handler.camera.xOffset, self.y - self.handler.camera.yOffset))

    def movement(self):
        if (self.inputs.up()):
            if (self.inputs.right() or self.inputs.left()):
                if (self.col.CheckCollision(0, -self.movementSpeed / 1.5) == False):
                    self.y -= self.movementSpeed / 1.5
            elif (self.col.CheckCollision(0, -self.movementSpeed) == False):
                self.y -= self.movementSpeed
        
        if (self.inputs.down()):
            if (self.inputs.right() or self.inputs.left()):
                if (self.col.CheckCollision(0, self.movementSpeed / 1.5) == False):
                    self.y += self.movementSpeed / 1.5
            elif (self.col.CheckCollision(0, self.movementSpeed) == False):
                self.y += self.movementSpeed
        
        if (self.inputs.right()):
            if (self.inputs.up() or self.inputs.down()):
                if (self.col.CheckCollision(self.movementSpeed / 1.5, 0) == False):
                    self.x += self.movementSpeed / 1.5
            elif (self.col.CheckCollision(self.movementSpeed, 0) == False): 
                self.x += self.movementSpeed
        
        if (self.inputs.left()):
            if (self.inputs.up() or self.inputs.down()):
                if (self.col.CheckCollision(-self.movementSpeed / 1.5, 0) == False):
                    self.x -= self.movementSpeed / 1.5
            elif (self.col.CheckCollision(-self.movementSpeed, 0) == False): 
                self.x -= self.movementSpeed


        
        
