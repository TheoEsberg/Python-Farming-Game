import pygame

class ShadowsAndLights:
    def __init__(self, handler):
        self.handler = handler
        self.shadow = self.handler.pygame.Surface((self.handler.displayWidth, self.handler.displayHeight), self.handler.pygame.SRCALPHA)
        self.shadow.fill((0, 0, 0, 128))

        self.handler.player.x

        self.light = pygame.image.load('res/gfx/gui/light.png')
        self.light = pygame.transform.scale(self.light, (self.light.get_width() * 12, self.light.get_height() * 12))

    def tick(self):
        # self.renderShadows()
        self.renderLight()

    def renderShadows(self):
        self.handler.display.blit(self.shadow, (0, 0))

    def renderLight(self):
        filter = pygame.surface.Surface((self.handler.displayWidth, self.handler.displayHeight))
        filter.fill((128, 128, 128))
        filter.blit(self.light, (pygame.mouse.get_pos()))
        self.handler.display.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)