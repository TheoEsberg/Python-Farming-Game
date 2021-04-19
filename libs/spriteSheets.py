class SpriteSheets:
    def __init__(self, handler):
        self.handler = handler

    def getSprites(self, spriteSheet, spriteWidth, spriteHeight, start, stop, scale):
        sprites = []    

        for i in range(start - 1, stop):
            sprite = spriteSheet.subsurface((i * spriteWidth, 0, spriteWidth, spriteHeight))
            sprite = self.handler.pygame.transform.scale(sprite, (spriteWidth * scale, spriteHeight * scale))
            sprites.append(sprite)
        return sprites
