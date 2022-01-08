"""
lid_management.py:
File that contains function that is responsible
for making the calendar's lids work as intended.
"""

from app import data
from app import time_management


def lid_manager():
    """
    Funktion that is responsible
    for making the calendar's lids work as intended.
    """

    count = 1

    while count < 25:
        first_condition_for_lid_x = (data.lids[count][1][0]-10) >= \
            data.x-data.images["lid1.png"].get_width()
        second_condition_for_lid_x = (data.lids[count][1][0]+96) <= \
            data.x+data.images["lid1.png"].get_width()
        data.lid_x = first_condition_for_lid_x and \
            second_condition_for_lid_x

        first_condition_for_lid_y = (data.lids[count][1][1]-10) >= \
            data.y-data.images["lid1.png"].get_height()
        second_condition_for_lid_y = (data.lids[count][1][1]+77) <= \
            data.y+data.images["lid1.png"].get_height()
        data.lid_y = first_condition_for_lid_y and \
            second_condition_for_lid_y
        if data.lids[count][3] == "opened":
            if data.lid_x and data.lid_y:
                data.lid = None
            else:
                data.lid = None
        else:
            if data.lid_x and data.lid_y:
                data.lid = data.display.blit(
                    data.lids[count][0][1],
                    (
                        data.lids[count][1][0],
                        data.lids[count][1][1]
                        )
                    )
                if data.mouse_button_down:
                    if time_management.time_teller() == data.lids[count][2]:
                        if data.lids[count][3] == "closed":
                            if data.sounds_on:
                                data.opening_sound.play()
                            data.lids[count] = (
                                data.lids[count][0],
                                data.lids[count][1],
                                data.lids[count][2],
                                "opened",
                                data.lids[count][4]
                                )
                            data.lid = None
                    else:
                        if data.lids[count][4] == "available":
                            if data.sounds_on:
                                data.locked_sound.play()
                            data.lids[count] = (
                                data.lids[count][0],
                                data.lids[count][1],
                                data.lids[count][2],
                                data.lids[count][3],
                                "unavailable"
                                )
                        data.lid = data.display.blit(
                            data.lids[count][0][0],
                            (
                                data.lids[count][1][0],
                                data.lids[count][1][1]
                                )
                            )
                        data.is_it_time = data.display.blit(
                            data.images["not_time_yet.png"],
                            (
                                data.lids[count][1][0],
                                data.lids[count][1][1]
                                )
                            )
                else:
                    data.lids[count] = (
                        data.lids[count][0],
                        data.lids[count][1],
                        data.lids[count][2],
                        data.lids[count][3],
                        "available"
                        )
            else:
                data.lid = data.display.blit(
                    data.lids[count][0][0],
                    (
                        data.lids[count][1][0],
                        data.lids[count][1][1]
                        )
                    )
                data.is_it_time = None
        count += 1
