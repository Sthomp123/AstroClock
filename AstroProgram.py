#!/usr/bin/env python 3
# AstroClock
# Ethan Dall & Steven Thompson
# 3-21-18

import os
import pygame
import math
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# time
walk = 0
type_x = 0
type_y = 0
move_sec = 0
move_min = 0
move_hr = 0
HYP = 180
timeCount = 0
timeSec = 1000
timeMin = 6000
timeHr = 3600000
rotate = 360
offset = 15
tm_sec = 0
tm_min = 0
tm_hr = 0

# dictionary to hold numeral for printing
numeral_dict = {}


def setxAngleAttribute(x_angle):
    x = (HYP * math.cos(math.radians(x_angle)))
    return x


def setyAngleAttribute(y_angle):
    y = (HYP * math.sin(math.radians(y_angle)))
    return y

# Starts Pygame

pygame.init()

# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)

# Fonts
name_font = pygame.font.SysFont('Times New Roman.ttf', 25)

pygame.display.set_caption("Astronomical Clock")

# Numbers to be drawn
for i in range(1, 25):
    val = i
    numeral = ''
    numeral += 'X' * (i // 10)
    if i % 10 == 9:
        numeral += 'IX'
        val -= 9
    else:
        cost = i % 10 // 5
        numeral += 'V' * cost
        val -= cost * 5

    if val % 5 == 4 and val != 9:
        numeral += 'IV'
    else:
        numeral += 'I' * (val % 5)

    numeral_dict[str(i)] = name_font.render(numeral, 1, (0, 0, 0))


class Clock(object):

    def __init__(self):
        self.hour24_face()
        self.hour_hands()

    @staticmethod
    def hour24_face():
        # +200 because 200 is center and numbers to need to rotate around it
        for i in range(1, 25):
            coords = (270 + (offset * i)) % 360
            screen.blit(numeral_dict[str(i)], (setxAngleAttribute(coords) + 190, setyAngleAttribute(coords) + 190))

    @staticmethod
    def hour_hands():
        """Runs and Draws the Seconds-Hand"""
        secX = (HYP * math.cos(math.radians(move_sec))) + 200
        secY = (HYP * math.sin(math.radians(move_sec))) + 200
        pygame.draw.line(screen, RED, (200, 200), (secX, secY), 2)

        """Runs and Draws the Minutes-Hand"""
        minX = (HYP * math.cos(math.radians(move_min))) + 200
        minY = (HYP * math.sin(math.radians(move_min))) + 200
        pygame.draw.line(screen, BLACK, (200, 200), (minX, minY), 3)

        """Runs and Draws the Hours-Hand"""
        hrX = (HYP * math.cos(math.radians(move_hr))/1.5) + 200
        hrY = (HYP * math.sin(math.radians(move_hr))/1.5) + 200
        pygame.draw.line(screen, BLACK, (200, 200), (hrX, hrY), 3)


frame = Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.circle(screen, BLACK, (200, 200), 200, 1)
    frame.hour_hands()
    frame.hour24_face()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Updates Seconds
    tm_sec = time.localtime()[5]
    move_sec = (tm_sec * 6 - 90) % 360

    # Updates Minutes
    tm_min = time.localtime()[4]
    if (tm_hr % 2) != 0:
        move_min = (tm_min * 3 + 90)
    else:
        move_min = (tm_min * 3 - 90) % 360

    # Updates Hours
    tm_hr = time.localtime()[3]
    if tm_min < 180:
        move_hr = (15 * tm_hr) - 90
    elif tm_min >= 180:
        move_hr = ((15 * tm_hr) - 90) * 2

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()