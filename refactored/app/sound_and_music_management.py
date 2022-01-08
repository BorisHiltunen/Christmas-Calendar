"""
sound_and_music_management.py:
File that contains function that is responsible
for making the sound and music buttons work as intended.
"""

from app import data
import pygame


def sound_and_music_manager():
    """
    Funktion that is responsible
    for making the sound and music buttons work as intended.
    """

    first_condition_for_sound_button_x = 224 >= \
        data.x-data.images["sound_button_on.png"].get_width()
    second_condition_for_sound_button_x = 309 <= \
        data.x+data.images["sound_button_on.png"].get_width()
    data.sound_button_x = first_condition_for_sound_button_x and \
        second_condition_for_sound_button_x

    first_condition_for_sound_button_y = 510 >= \
        data.y-data.images["sound_button_on.png"].get_height()
    second_condition_for_sound_button_y = 595 <= \
        data.y+data.images["sound_button_on.png"].get_height()
    data.sound_button_y = first_condition_for_sound_button_y and \
        second_condition_for_sound_button_y

    if data.sound_button_x and data.sound_button_y:
        if data.sounds_on:
            data.sound_button = data.display.blit(
                data.images["sound_button_on_hover_over.png"],
                (224, 510)
                )
        else:
            data.sound_button = data.display.blit(
                data.images["sound_button_off_hover_over.png"],
                (224, 510)
                )
        if data.mouse_button_down:
            if data.locked is False:
                data.locked = True
                if data.sounds_on:
                    data.sounds_on = False
                else:
                    data.sounds_on = True
        else:
            data.locked = False
    else:
        if data.sounds_on:
            data.sound_button = data.display.blit(
                data.images["sound_button_on.png"],
                (224, 510)
                )
        else:
            data.sound_button = data.display.blit(
                data.images["sound_button_off.png"],
                (224, 510)
                )

    first_condition_for_music_button_x = 324 >= \
        data.x-data.images["music_button_on.png"].get_width()
    second_condition_for_music_button_x = 409 <= \
        data.x+data.images["music_button_on.png"].get_width()
    data.music_button_x = first_condition_for_music_button_x and \
        second_condition_for_music_button_x

    first_condition_for_music_button_y = 510 >= \
        data.y-data.images["music_button_on.png"].get_height()
    second_condition_for_music_button_y = 595 <= \
        data.y+data.images["music_button_on.png"].get_height()
    data.music_button_y = first_condition_for_music_button_y and \
        second_condition_for_music_button_y

    if data.music_button_x and data.music_button_y:

        if data.music_on:
            data.music_button = data.display.blit(
                data.images["music_button_on_hover_over.png"],
                (324, 510)
                )
        else:
            data.music_button = data.display.blit(
                data.images["music_button_off_hover_over.png"],
                (324, 510)
                )

        if data.mouse_button_down:
            if data.locked is False:
                data.locked = True
                if data.music_on:
                    pygame.mixer.music.pause()
                    data.music_on = False
                else:
                    pygame.mixer.music.unpause()
                    data.music_on = True
        else:
            data.locked = False
    else:
        if data.music_on:
            data.music_button = data.display.blit(
                data.images["music_button_on.png"],
                (324, 510)
                )
        else:
            data.music_button = data.display.blit(
                data.images["music_button_off.png"],
                (324, 510)
                )
