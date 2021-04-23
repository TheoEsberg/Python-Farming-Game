import pygame, os
import libs.handler as Handler
import libs.maps as Maps
import libs.camera as Camera
import libs.player
import libs.entity
import libs.mouseImg
import libs.FPSCounter
import libs.shadowsAndLight

path = os.path.dirname(__file__)
os.chdir(path)

displayHeight = 600
displayWidth = 800

pygame.init()
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Python Farming Game")
clock = pygame.time.Clock()

pygame.mixer.init()
soundtrack = pygame.mixer.Sound("res/sfx/soundtrack-1.wav")
pygame.mixer.Sound.set_volume(soundtrack, 0.1)
pygame.mixer.Sound.play(soundtrack)


handler = Handler.Handler()
handler.pygame = pygame
handler.display = display
handler.displayWidth = displayWidth
handler.displayHeight = displayHeight

renderMap = Maps.Map(handler)
camera = Camera.Camera(handler)
handler.camera = camera

player = libs.player.Player(500, 500, 24, 24, 1, handler)
handler.player = player
mouseSetting = libs.mouseImg.Mouse(handler)
FPS = libs.FPSCounter.FPS(handler, clock)
SaL = libs.shadowsAndLight.ShadowsAndLights(handler)

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

        # Testing light and shadows
        # shadows = pygame.Surface((displayWidth, displayHeight), pygame.SRCALPHA)
        # print(shadows.get_flags())
        # shadows.fill((0, 0, 0, 64))
        # display.blit(shadows, (0, 0))

        SaL.tick()
        mouseSetting.tick()
        FPS.tick()

        pygame.display.flip()
        clock.tick(60)

App()
pygame.mixer.quit()
pygame.quit()