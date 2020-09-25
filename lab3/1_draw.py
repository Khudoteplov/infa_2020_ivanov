import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255,255,0), (200,200), 100)
line(screen, (0, 0, 0), (100, 120), (180, 170), 10)
line(screen, (0,0,0), (220, 170), (300, 150), 10)

circle(screen, (255, 0, 0), (160, 180), 15)
circle(screen, (0, 0, 0), (160, 180), 9)

circle(screen, (255, 0, 0), (240, 182), 12)
circle(screen, (0, 0, 0), (240, 182), 6)

line(screen, (0,0, 0),(150, 250), (250, 250), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
