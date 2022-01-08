"""
game_visualizer:
File that contains function that basically draws the calendar.
"""

from app import data
from app import sound_and_music_management
from app import lid_management
import pygame


def draw_the_calendar():
    """Funktion that basically draws the calendar."""

    data.display.fill((0, 100, 100))
    data.display.blit(data.images["full_background.png"], (0, 0))

    sound_and_music_management.sound_and_music_manager()
    lid_management.lid_manager()

    data.display.blit(data.images["mouse.png"], (data.x, data.y))

    pygame.display.flip()
