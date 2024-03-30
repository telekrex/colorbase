#!/usr/bin/env python3

#######################################
# Colorbase ~ A display checker tool :)
#######################################

import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '1'
tps = 60 # ticks per second
pygame.init()
pygame.display.set_caption('Colorbase R2')
monitor = (pygame.display.Info().current_w, pygame.display.Info().current_h)
fullscreen = False
clock = pygame.time.Clock() # start pygame clock
void = pygame.display.set_mode((200, 200), pygame.RESIZABLE)
colors = ['white', 'blue', 'green', 'red', 'yellow', 'cyan', 'magenta', 'gray', 'black']
index = 0 # set index of color selection


def update_display():
    # updates display
    # to color at index
    global void
    global index
    global colors
    void.fill(colors[index])


update_display()
r = True
while r:
    clock.tick(tps)
    for event in pygame.event.get():
        # checking for input events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # on SPACE, toggle fullscreen/
                # resizable windows size
                if fullscreen == False:
                    fullscreen = True
                    void = pygame.display.set_mode(monitor, pygame.FULLSCREEN)
                else:
                    fullscreen = False
                    void = pygame.display.set_mode((200, 200), pygame.RESIZABLE)
                update_display()
            if event.key == pygame.K_RETURN:
                # on ENTER (aka RETURN),
                # change index, thus color
                if index == len(colors)-1:
                    index = 0
                else:
                    index += 1
                update_display()
            if event.key == pygame.K_ESCAPE:
                # on ESCAPE, exit application
                r = False
                sys.exit()
    pygame.display.flip()