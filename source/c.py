#!/usr/bin/env python3
# Written by Telekrex
import pygame
import sys
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
tps = 30
pygame.init()
pygame.display.set_caption('Color Calibrator')
monitor = (pygame.display.Info().current_w, pygame.display.Info().current_h)
clock = pygame.time.Clock()
void = pygame.display.set_mode(monitor, pygame.RESIZABLE)
colors = ['white', 'blue', 'green', 'red', 'yellow', 'purple', 'black']
index = 0


def update_display():
    global void
    global index
    global colors
    void.fill(colors[index])


update_display()
r = True
while r:
    clock.tick(tps)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if index == len(colors)-1:
                    index = 0
                else:
                    index += 1
                update_display()
            if event.key == pygame.K_ESCAPE:
                r = False
                sys.exit()
    pygame.display.flip()
