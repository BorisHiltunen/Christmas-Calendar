"""
data.py:
Initializes and preserves the needed attributes for future use.
"""

import pygame
from app import file_management

pygame.init()

image_names = []
images = {}

file_management.download_pictures()

image_list = [
    (images["lid1.png"], images["lid1_hover_over.png"]),
    (images["lid1.png"], images["lid1_hover_over.png"]),
    (images["lid2.png"], images["lid2_hover_over.png"]),
    (images["lid3.png"], images["lid3_hover_over.png"]),
    (images["lid4.png"], images["lid4_hover_over.png"]),
    (images["lid5.png"], images["lid5_hover_over.png"]),
    (images["lid6.png"], images["lid6_hover_over.png"]),
    (images["lid7.png"], images["lid7_hover_over.png"]),
    (images["lid8.png"], images["lid8_hover_over.png"]),
    (images["lid9.png"], images["lid9_hover_over.png"]),
    (images["lid10.png"], images["lid10_hover_over.png"]),
    (images["lid11.png"], images["lid11_hover_over.png"]),
    (images["lid12.png"], images["lid12_hover_over.png"]),
    (images["lid13.png"], images["lid13_hover_over.png"]),
    (images["lid14.png"], images["lid14_hover_over.png"]),
    (images["lid15.png"], images["lid15_hover_over.png"]),
    (images["lid16.png"], images["lid16_hover_over.png"]),
    (images["lid17.png"], images["lid17_hover_over.png"]),
    (images["lid18.png"], images["lid18_hover_over.png"]),
    (images["lid19.png"], images["lid19_hover_over.png"]),
    (images["lid20.png"], images["lid20_hover_over.png"]),
    (images["lid21.png"], images["lid21_hover_over.png"]),
    (images["lid22.png"], images["lid22_hover_over.png"]),
    (images["lid23.png"], images["lid23_hover_over.png"]),
    (images["lid24.png"], images["lid24_hover_over.png"])
]

# lids list contains every lid's images, coordinates, date,
# string that tells whether lid is open or closed
# and string that tells whether the sound is available or not.
lids = [
    (image_list[0], (-10, -10), "25.12.2021", "closed", "available"),
    (image_list[1], (0, 0), "17.12.2021", "closed", "available"),
    (image_list[2], (105, 0), "20.12.2021", "closed", "available"),
    (image_list[3], (209, 0), "24.12.2021", "closed", "available"),
    (image_list[4], (313, 0), "9.12.2021", "closed", "available"),
    (image_list[5], (0, 86), "12.12.2021", "closed", "available"),
    (image_list[6], (105, 86), "6.12.2021", "closed", "available"),
    (image_list[7], (209, 86), "14.12.2021", "closed", "available"),
    (image_list[8], (313, 86), "3.12.2021", "closed", "available"),
    (image_list[9], (0, 171), "4.12.2021", "closed", "available"),
    (image_list[10], (105, 171), "19.12.2021", "closed", "available"),
    (image_list[11], (209, 171), "22.12.2021", "closed", "available"),
    (image_list[12], (313, 171), "16.12.2021", "closed", "available"),
    (image_list[13], (0, 256), "21.12.2021", "closed", "available"),
    (image_list[14], (105, 256), "15.12.2021", "closed", "available"),
    (image_list[15], (209, 256), "1.12.2021", "closed", "available"),
    (image_list[16], (313, 256), "7.12.2021", "closed", "available"),
    (image_list[17], (0, 341), "10.12.2021", "closed", "available"),
    (image_list[18], (105, 341), "23.12.2021", "closed", "available"),
    (image_list[19], (209, 341), "18.12.2021", "closed", "available"),
    (image_list[20], (313, 341), "11.12.2021", "closed", "available"),
    (image_list[21], (0, 426), "2.12.2021", "closed", "available"),
    (image_list[22], (105, 426), "8.12.2021", "closed", "available"),
    (image_list[23], (209, 426), "13.12.2021", "closed", "available"),
    (image_list[24], (313, 426), "5.12.2021", "closed", "available")
    ]

height = 600
width = 416

locked = False

sounds_on = True
music_on = True

# Making the mouse invisible by making it appear outside of the window
x = 1000
y = 1000

mouse_button_down = False
sound_button_x = False
sound_button_y = False
music_button_x = False
music_button_y = False
sound_button = ""
music_button = ""
lid_x = False
lid_y = False

lid = ""
is_it_time = ""

display = pygame.display.set_mode((width, height))

pygame.display.set_caption("ChristmasCalendar")

file_management.sound_manager()
