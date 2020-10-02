import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

cloud=(168, 186, 186, 70)

rect(screen, (255, 255, 255), (0, 0, 500, 450))

rect(screen, (183, 196, 200), (0, 0, 500, 445))
rect(screen, (83, 108, 103, 0), (0, 450, 500, 250))



ellipse(screen, cloud, (-100, 50, 400, 100))

rect(screen, (147, 167, 172), (10, 20, 100, 450))

rect( screen, (219, 227, 226), (400, 10, 95, 460))
ellipse_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
ellipse_surface.fill((255, 100, 100, 100))
ellipse( screen, cloud, (150, -20, 400, 123))


rect(screen, (111, 145, 138), (350, 100, 100, 500))

rect(screen, (147, 172, 167), (150, 90, 80, 450))

ellipse(screen, cloud, (-100, 350, 350, 90))

rect(screen, (183, 200, 196), (50, 100, 130, 490))

ellipse( screen, cloud, (90, 200, 500, 130))

ellipse (screen, (183, 200, 196), (-20, 600, 600, 180))

rect(screen, (100, 200, 200), (200, 600, 200, 50))
rect(screen, (100, 200, 200), (240, 570, 110, 30))
rect(screen, (200, 200, 255), (250, 575, 40, 25))
rect(screen, (200, 200, 255), (300, 575, 40, 25))

ellipse(screen, (0, 0, 0), (350, 630,40, 40))

ellipse(screen, (0, 0, 0), (220, 630, 40, 40))
rect(screen, (0, 0, 0), (185, 635, 15, 7))

ellipse(screen, (130, 150, 150), (40, 610, 130, 40))
ellipse(screen, (130, 150, 150), (10, 560, 130, 40))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
