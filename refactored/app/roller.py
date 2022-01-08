"""
roller.py:
File that contains function for looping over and over
thus making the game flow.
"""

import pygame
from app import game_visualizer
from app import event_analyzer


def loop():
    """
    Funktion that loops over and over.
    Thus making the use of the calendar feel comfortable.
    """

    clock = pygame.time.Clock()

    while True:
        game_visualizer.draw_the_calendar()
        event_analyzer.analyse_events()
        clock.tick(60)
