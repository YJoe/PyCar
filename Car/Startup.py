import pygame
import math
pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("", 20)

pygame.init()
width = 1000
height = 600
main_s = pygame.display.set_mode((width, height))


def deg_to_rad(degrees):
    return degrees / 180.0 * math.pi