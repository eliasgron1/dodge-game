import pygame

#Game Variables
FPS = 60
MORE_SPEED = pygame.USEREVENT + 1
FRAMES_PER_SEC = pygame.time.Clock()
SPEED = 3
SCORE = 0
HIGH_SCORE = 0

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('ball game')


