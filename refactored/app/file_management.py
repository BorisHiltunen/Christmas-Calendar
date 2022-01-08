"""
file_management.py:
File that contains two functions that initialize files.
"""

import os
from app import data
import pygame


def download_pictures():
    """
    Function that downloads pictures
    that will be used in the calendar.
    """

    data.image_names = [
        "full_background.png", "mouse.png", "not_time_yet.png",
        "sound_button_on.png", "sound_button_off.png",
        "music_button_on.png", "music_button_off.png",
        "sound_button_on_hover_over.png",
        "sound_button_off_hover_over.png",
        "music_button_on_hover_over.png",
        "music_button_off_hover_over.png",
        "lid1.png", "lid2.png", "lid3.png", "lid4.png", "lid5.png",
        "lid6.png", "lid7.png", "lid8.png", "lid9.png", "lid10.png",
        "lid11.png", "lid12.png", "lid13.png", "lid14.png", "lid15.png",
        "lid16.png", "lid17.png", "lid18.png", "lid19.png", "lid20.png",
        "lid21.png", "lid22.png", "lid23.png", "lid24.png",
        "lid1_hover_over.png", "lid2_hover_over.png",
        "lid3_hover_over.png", "lid4_hover_over.png",
        "lid5_hover_over.png", "lid6_hover_over.png",
        "lid7_hover_over.png", "lid8_hover_over.png",
        "lid9_hover_over.png", "lid10_hover_over.png",
        "lid11_hover_over.png", "lid12_hover_over.png",
        "lid13_hover_over.png", "lid14_hover_over.png",
        "lid15_hover_over.png", "lid16_hover_over.png",
        "lid17_hover_over.png", "lid18_hover_over.png",
        "lid19_hover_over.png", "lid20_hover_over.png",
        "lid21_hover_over.png", "lid22_hover_over.png",
        "lid23_hover_over.png", "lid24_hover_over.png"
        ]
    data.images = {}

    for image in data.image_names:
        data.images[image] = pygame.image.load(
            os.path.join("images", image)
            )


def sound_manager():
    """Function that initializes calendar's music and sounds."""

    data.opening_sound = pygame.mixer.Sound(
        os.path.join("sounds", "opening_sound.wav")
        )
    data.locked_sound = pygame.mixer.Sound(
        os.path.join("sounds", "locked_sound.wav")
        )

    data.music = pygame.mixer.music.load(
        os.path.join("music", "music.wav")
        )
    pygame.mixer.music.play(loops=-1)
