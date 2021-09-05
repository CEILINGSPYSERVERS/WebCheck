import os, sys, pygame
import pygame.gfxdraw
from pygame.locals import *

os.system("cls")


class Ameoba:
    def __init__(self, x, y, radius, red, green, blue):
        # print(f"amoeba ")
        self.x, self.y, self.r = x, y, radius
        self.color = (red, green, blue)

    def funprint(self):
        print(self.x, self.y, self.r)


a1 = Ameoba(100, 100, 120, 255, 0, 0)
a2 = Ameoba(350, 350, 35, 0, 0, 255)


def update(dt):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.

#def spawn(obj):


def draw(screen):
    screen.fill((64, 64, 64))

    pygame.gfxdraw.filled_circle(screen, a1.x, a1.y, a1.r, a1.color)
    pygame.gfxdraw.filled_circle(screen, a2.x, a2.y, a2.r, a2.color)

    pygame.display.flip()


def runPyGame():
    pygame.init()
    pygame.display.set_caption("Amoeba")
    fps = 60.0
    fpsClock = pygame.time.Clock()
    height = 900
    width = int((height / 16) * 9)
    res = height, width
    screen = pygame.display.set_mode(res)
    dt = 1 / fps
    while True:
        update(dt)

        draw(screen)

        dt = fpsClock.tick(fps)


runPyGame()
