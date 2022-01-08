"""event_analyser.py: Contains function that analyses the calendar's events."""

import pygame
from app import data


def analyse_events():
    """
    Funktion that is responsible
    for making the calendar's mouse work as intended.
    """

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            data.x = event.pos[0]-data.images["mouse.png"].get_width()/2
            data.y = event.pos[1]-data.images["mouse.png"].get_height()/2
        if event.type == pygame.MOUSEBUTTONDOWN:
            data.mouse_button_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            data.mouse_button_down = False
        if event.type == pygame.QUIT:
            exit()
