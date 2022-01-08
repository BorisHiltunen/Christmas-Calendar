"""main.py: Contains ChristmasCalendar class."""

import datetime
import pygame


class ChristmasCalendar:
    """
    Class that contains necessary functions
    to make ChristmasCalendar app work as intended.
    """

    def __init__(self):
        pygame.init()

        self.download_pictures()

        image_list = [
            (self.images["lid1.png"], self.images["lid1_hover_over.png"]),
            (self.images["lid1.png"], self.images["lid1_hover_over.png"]),
            (self.images["lid2.png"], self.images["lid2_hover_over.png"]),
            (self.images["lid3.png"], self.images["lid3_hover_over.png"]),
            (self.images["lid4.png"], self.images["lid4_hover_over.png"]),
            (self.images["lid5.png"], self.images["lid5_hover_over.png"]),
            (self.images["lid6.png"], self.images["lid6_hover_over.png"]),
            (self.images["lid7.png"], self.images["lid7_hover_over.png"]),
            (self.images["lid8.png"], self.images["lid8_hover_over.png"]),
            (self.images["lid9.png"], self.images["lid9_hover_over.png"]),
            (self.images["lid10.png"], self.images["lid10_hover_over.png"]),
            (self.images["lid11.png"], self.images["lid11_hover_over.png"]),
            (self.images["lid12.png"], self.images["lid12_hover_over.png"]),
            (self.images["lid13.png"], self.images["lid13_hover_over.png"]),
            (self.images["lid14.png"], self.images["lid14_hover_over.png"]),
            (self.images["lid15.png"], self.images["lid15_hover_over.png"]),
            (self.images["lid16.png"], self.images["lid16_hover_over.png"]),
            (self.images["lid17.png"], self.images["lid17_hover_over.png"]),
            (self.images["lid18.png"], self.images["lid18_hover_over.png"]),
            (self.images["lid19.png"], self.images["lid19_hover_over.png"]),
            (self.images["lid20.png"], self.images["lid20_hover_over.png"]),
            (self.images["lid21.png"], self.images["lid21_hover_over.png"]),
            (self.images["lid22.png"], self.images["lid22_hover_over.png"]),
            (self.images["lid23.png"], self.images["lid23_hover_over.png"]),
            (self.images["lid24.png"], self.images["lid24_hover_over.png"])
        ]

        # lids list contains every lid's index, coordinates, date,
        # string that tells whether lid is open or closed
        # and string that tells whether the sound is available or not.

        self.lids = [
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

        self.height = 600
        self.width = 416

        self.locked = False

        self.sounds_on = True
        self.music_on = True

        # Making the mouse invisible by making it appear outside of the window
        self.x = 1000
        self.y = 1000

        self.mouse_button_down = False
        self.sound_button_x = False
        self.sound_button_y = False
        self.music_button_x = False
        self.music_button_y = False
        self.sound_button = ""
        self.music_button = ""
        self.lid_x = False
        self.lid_y = False

        self.lid = ""
        self.is_it_time = ""

        self.display = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("ChristmasCalendar")

        self.sound_manager()
        self.loop()

    def download_pictures(self):
        """
        Function that downloads pictures
        that will be used in the calendar.
        """

        self.image_names = [
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
        self.images = {}

        for image in self.image_names:
            self.images[image] = pygame.image.load(image)

    def sound_manager(self):
        """Function that initializes calendar's music and sounds."""

        self.opening_sound = pygame.mixer.Sound('opening_sound.wav')
        self.locked_sound = pygame.mixer.Sound('locked_sound.wav')

        self.music = pygame.mixer.music.load('music.wav')
        pygame.mixer.music.play(loops=-1)

    def time_teller(self):
        """Funktion that returns the date in the correct form."""

        time = datetime.datetime.now()
        day = time.day
        month = time.month
        year = time.year
        return f"{day}.{month}.{year}"

    def sound_and_button_manager(self):
        """
        Funktion that is responsible
        for making the sound and music buttons work as intended.
        """

        first_condition_for_sound_button_x = 224 >= \
            self.x-self.images["sound_button_on.png"].get_width()
        second_condition_for_sound_button_x = 309 <= \
            self.x+self.images["sound_button_on.png"].get_width()
        self.sound_button_x = first_condition_for_sound_button_x and \
            second_condition_for_sound_button_x

        first_condition_for_sound_button_y = 510 >= \
            self.y-self.images["sound_button_on.png"].get_height()
        second_condition_for_sound_button_y = 595 <= \
            self.y+self.images["sound_button_on.png"].get_height()
        self.sound_button_y = first_condition_for_sound_button_y and \
            second_condition_for_sound_button_y

        if self.sound_button_x and self.sound_button_y:
            if self.sounds_on:
                self.sound_button = self.display.blit(
                    self.images["sound_button_on_hover_over.png"],
                    (224, 510)
                    )
            else:
                self.sound_button = self.display.blit(
                    self.images["sound_button_off_hover_over.png"],
                    (224, 510)
                    )
            if self.mouse_button_down:
                if self.locked is False:
                    self.locked = True
                    if self.sounds_on:
                        self.sounds_on = False
                    else:
                        self.sounds_on = True
            else:
                self.locked = False
        else:
            if self.sounds_on:
                self.sound_button = self.display.blit(
                    self.images["sound_button_on.png"],
                    (224, 510)
                    )
            else:
                self.sound_button = self.display.blit(
                    self.images["sound_button_off.png"],
                    (224, 510)
                    )

        first_condition_for_music_button_x = 324 >= \
            self.x-self.images["music_button_on.png"].get_width()
        second_condition_for_music_button_x = 409 <= \
            self.x+self.images["music_button_on.png"].get_width()
        self.music_button_x = first_condition_for_music_button_x and \
            second_condition_for_music_button_x

        first_condition_for_music_button_y = 510 >= \
            self.y-self.images["music_button_on.png"].get_height()
        second_condition_for_music_button_y = 595 <= \
            self.y+self.images["music_button_on.png"].get_height()
        self.music_button_y = first_condition_for_music_button_y and \
            second_condition_for_music_button_y

        if self.music_button_x and self.music_button_y:

            if self.music_on:
                self.music_button = self.display.blit(
                    self.images["music_button_on_hover_over.png"],
                    (324, 510)
                    )
            else:
                self.music_button = self.display.blit(
                    self.images["music_button_off_hover_over.png"],
                    (324, 510)
                    )

            if self.mouse_button_down:
                if self.locked is False:
                    self.locked = True
                    if self.music_on:
                        pygame.mixer.music.pause()
                        self.music_on = False
                    else:
                        pygame.mixer.music.unpause()
                        self.music_on = True
            else:
                self.locked = False
        else:
            if self.music_on:
                self.music_button = self.display.blit(
                    self.images["music_button_on.png"],
                    (324, 510)
                    )
            else:
                self.music_button = self.display.blit(
                    self.images["music_button_off.png"],
                    (324, 510)
                    )

    def lid_management(self):
        """
        Funktion that is responsible
        for making the calendar's lids work as intended.
        """

        count = 1

        while count < 25:
            first_condition_for_lid_x = (self.lids[count][1][0]-10) >= \
                self.x-self.images["lid1.png"].get_width()
            second_condition_for_lid_x = (self.lids[count][1][0]+96) <= \
                self.x+self.images["lid1.png"].get_width()
            self.lid_x = first_condition_for_lid_x and \
                second_condition_for_lid_x

            first_condition_for_lid_y = (self.lids[count][1][1]-10) >= \
                self.y-self.images["lid1.png"].get_height()
            second_condition_for_lid_y = (self.lids[count][1][1]+77) <= \
                self.y+self.images["lid1.png"].get_height()
            self.lid_y = first_condition_for_lid_y and \
                second_condition_for_lid_y
            if self.lids[count][3] == "opened":
                if self.lid_x and self.lid_y:
                    self.lid = None
                else:
                    self.lid = None
            else:
                if self.lid_x and self.lid_y:
                    self.lid = self.display.blit(
                        self.lids[count][0][1],
                        (
                            self.lids[count][1][0],
                            self.lids[count][1][1]
                            )
                        )
                    if self.mouse_button_down:
                        if self.time_teller() == self.lids[count][2]:
                            if self.lids[count][3] == "closed":
                                if self.sounds_on:
                                    self.opening_sound.play()
                                self.lids[count] = (
                                    self.lids[count][0],
                                    self.lids[count][1],
                                    self.lids[count][2],
                                    "opened",
                                    self.lids[count][4]
                                    )
                                self.lid = None
                        else:
                            if self.lids[count][4] == "available":
                                if self.sounds_on:
                                    self.locked_sound.play()
                                self.lids[count] = (
                                    self.lids[count][0],
                                    self.lids[count][1],
                                    self.lids[count][2],
                                    self.lids[count][3],
                                    "unavailable"
                                    )
                            self.lid = self.display.blit(
                                self.lids[count][0][0],
                                (
                                    self.lids[count][1][0],
                                    self.lids[count][1][1]
                                    )
                                )
                            self.is_it_time = self.display.blit(
                                self.images["not_time_yet.png"],
                                (
                                    self.lids[count][1][0],
                                    self.lids[count][1][1]
                                    )
                                )
                    else:
                        self.lids[count] = (
                            self.lids[count][0],
                            self.lids[count][1],
                            self.lids[count][2],
                            self.lids[count][3],
                            "available"
                            )
                else:
                    self.lid = self.display.blit(
                        self.lids[count][0][0],
                        (
                            self.lids[count][1][0],
                            self.lids[count][1][1]
                            )
                        )
                    self.is_it_time = None
            count += 1

    def loop(self):
        """
        Funktion that loops over and over.
        Thus making the use of the calendar feel comfortable.
        """

        clock = pygame.time.Clock()

        while True:
            self.draw_the_calendar()
            self.analyse_events()
            clock.tick(60)

    def analyse_events(self):
        """
        Funktion that is responsible
        for making the game's mouse work as intended.
        """

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.x = event.pos[0]-self.images["mouse.png"].get_width()/2
                self.y = event.pos[1]-self.images["mouse.png"].get_height()/2
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_down = False
            if event.type == pygame.QUIT:
                exit()

    def draw_the_calendar(self):
        """Funktion that basically draws the calendar."""

        self.display.fill((0, 100, 100))
        self.display.blit(self.images["full_background.png"], (0, 0))

        self.sound_and_button_manager()
        self.lid_management()

        self.display.blit(self.images["mouse.png"], (self.x, self.y))

        pygame.display.flip()


if __name__ == "__main__":
    ChristmasCalendar()
