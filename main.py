import pygame, os
import libs.handler as Handler
import libs.maps as Maps
import libs.camera as Camera

path = os.path.dirname(__file__)
os.chdir(path)

displayHeight = 800
displayWidth = 1200

pygame.init()
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Python Farming Game")
clock = pygame.time.Clock()

handler = Handler.Handler()
handler.display = display
handler.displayWidth = displayWidth
handler.displayHeight = displayHeight

renderMap = Maps.Map(handler)
camera = Camera.Camera(handler)
handler.camera = camera


def App():
    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False

        display.fill((0, 0, 0))
        renderMap.render()
      
        pygame.display.flip()
        clock.tick(60)

App()
pygame.quit()