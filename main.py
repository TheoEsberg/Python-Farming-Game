import pygame, os
import libs.handler as Handler
import libs.maps as Maps
import libs.camera as Camera
import libs.player
import libs.entity
import libs.mouseImg
import libs.FPSCounter

path = os.path.dirname(__file__)
os.chdir(path)

displayHeight = 1080
displayWidth = 1920

pygame.init()
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Python Farming Game")
clock = pygame.time.Clock()

handler = Handler.Handler()
handler.pygame = pygame
handler.display = display
handler.displayWidth = displayWidth
handler.displayHeight = displayHeight

renderMap = Maps.Map(handler)
camera = Camera.Camera(handler)
handler.camera = camera

player = libs.player.Player(500, 500, 24, 24, 1, handler)
mouseSetting = libs.mouseImg.Mouse(handler)
FPS = libs.FPSCounter.FPS(handler, clock)


def App():
    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False

        display.fill((0, 0, 0))
        renderMap.renderingDoneRight()

        for entity in libs.entity.entities:
            if (entity.allowTick == True):
                entity.tick()

        mouseSetting.tick()
        FPS.tick()

        pygame.display.flip()
        clock.tick(60)

App()
pygame.quit()