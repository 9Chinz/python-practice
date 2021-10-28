import pygame
from pygame import display

# initialize
pygame.init()

# create display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(display)

# set caption
pygame.display.set_caption("Test")

# game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

# end of the game
pygame.quit()