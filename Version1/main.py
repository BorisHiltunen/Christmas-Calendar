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

        self.opening_sound = pygame.mixer.Sound('opening_sound.wav')
        self.locked_sound = pygame.mixer.Sound('locked_sound.wav')

        self.music = pygame.mixer.music.load('music.wav')
        pygame.mixer.music.play(loops=-1)

        self.height = 600
        self.width = 416

        self.locked = False

        self.sound_lock1 = False
        self.sound_lock2 = False
        self.sound_lock3 = False
        self.sound_lock4 = False
        self.sound_lock5 = False
        self.sound_lock6 = False
        self.sound_lock7 = False
        self.sound_lock8 = False
        self.sound_lock9 = False
        self.sound_lock10 = False
        self.sound_lock11 = False
        self.sound_lock12 = False
        self.sound_lock13 = False
        self.sound_lock14 = False
        self.sound_lock15 = False
        self.sound_lock16 = False
        self.sound_lock17 = False
        self.sound_lock18 = False
        self.sound_lock19 = False
        self.sound_lock20 = False
        self.sound_lock21 = False
        self.sound_lock22 = False
        self.sound_lock23 = False
        self.sound_lock24 = False

        self.sounds_on = True
        self.music_on = True

        #Tells whether a lid is open or not
        self.opened1 = False
        self.opened2 = False
        self.opened3 = False
        self.opened4 = False
        self.opened5 = False
        self.opened6 = False
        self.opened7 = False
        self.opened8 = False
        self.opened9 = False
        self.opened10 = False
        self.opened11 = False
        self.opened12 = False
        self.opened13 = False
        self.opened14 = False
        self.opened15 = False
        self.opened16 = False
        self.opened17 = False
        self.opened18 = False
        self.opened19 = False
        self.opened20 = False
        self.opened21 = False
        self.opened22 = False
        self.opened23 = False
        self.opened24 = False

        #Making the mouse invisible by making it appear outside of the window
        self.x = 1000
        self.y = 1000

        self.mouse_button_down = False
        self.sound_button_x = False
        self.sound_button_y = False
        self.music_button_x = False
        self.music_button_y = False
        self.sound_button = ""
        self.music_button = ""
        self.lid1_x = False
        self.lid1_y = False
        self.lid2_x = False
        self.lid2_y = False
        self.lid3_x = False
        self.lid3_y = False
        self.lid4_x = False
        self.lid4_y = False
        self.lid5_x = False
        self.lid5_y = False
        self.lid6_x = False
        self.lid6_y = False
        self.lid7_x = False
        self.lid7_y = False
        self.lid8_x = False
        self.lid8_y = False
        self.lid9_x = False
        self.lid9_y = False
        self.lid10_x = False
        self.lid10_y = False
        self.lid11_x = False
        self.lid11_y = False
        self.lid12_x = False
        self.lid12_y = False
        self.lid13_x = False
        self.lid13_y = False
        self.lid14_x = False
        self.lid14_y = False
        self.lid15_x = False
        self.lid15_y = False
        self.lid16_x = False
        self.lid16_y = False
        self.lid17_x = False
        self.lid17_y = False
        self.lid18_x = False
        self.lid18_y = False
        self.lid19_x = False
        self.lid19_y = False
        self.lid20_x = False
        self.lid20_y = False
        self.lid21_x = False
        self.lid21_y = False
        self.lid22_x = False
        self.lid22_y = False
        self.lid23_x = False
        self.lid23_y = False
        self.lid24_x = False
        self.lid24_y = False
        self.lid_1 = ""
        self.lid_2 = ""
        self.lid_3 = ""
        self.lid_4 = ""
        self.lid_5 = ""
        self.lid_6 = ""
        self.lid_7 = ""
        self.lid_8 = ""
        self.lid_9 = ""
        self.lid_10 = ""
        self.lid_11 = ""
        self.lid_12 = ""
        self.lid_13 = ""
        self.lid_14 = ""
        self.lid_15 = ""
        self.lid_16 = ""
        self.lid_17 = ""
        self.lid_18 = ""
        self.lid_19 = ""
        self.lid_20 = ""
        self.lid_21 = ""
        self.lid_22 = ""
        self.lid_23 = ""
        self.lid_24 = ""
        self.is_it_time = ""

        self.display = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("ChristmasCalendar")

        self.loop()

    def download_pictures(self):
        """
        Function that downloads pictures
        that will be used in the calendar.
        """

        self.background = pygame.image.load("background2.png")
        self.mouse = pygame.image.load("mouse.png")
        self.not_time_yet = pygame.image.load("not_time_yet.png")

        self.sound_button_on = pygame.image.load("sound_button_on.png")
        self.sound_button_off = pygame.image.load("sound_button_off.png")
        self.music_button_on = pygame.image.load("music_button_on.png")
        self.music_button_off = pygame.image.load("music_button_off.png")
        self.sound_button_on_hover_over = pygame.image.load("sound_button_on_hover_over.png")
        self.sound_button_off_hover_over = pygame.image.load("sound_button_off_hover_over.png")
        self.music_button_on_hover_over = pygame.image.load("music_button_on_hover_over.png")
        self.music_button_off_hover_over = pygame.image.load("music_button_off_hover_over.png")

        self.lid1 = pygame.image.load("lid1.png")
        self.lid2 = pygame.image.load("lid2.png")
        self.lid3 = pygame.image.load("lid3.png")
        self.lid4 = pygame.image.load("lid4.png")
        self.lid5 = pygame.image.load("lid5.png")
        self.lid6 = pygame.image.load("lid6.png")
        self.lid7 = pygame.image.load("lid7.png")
        self.lid8 = pygame.image.load("lid8.png")
        self.lid9 = pygame.image.load("lid9.png")
        self.lid10 = pygame.image.load("lid10.png")
        self.lid11 = pygame.image.load("lid11.png")
        self.lid12 = pygame.image.load("lid12.png")
        self.lid13 = pygame.image.load("lid13.png")
        self.lid14 = pygame.image.load("lid14.png")
        self.lid15 = pygame.image.load("lid15.png")
        self.lid16 = pygame.image.load("lid16.png")
        self.lid17 = pygame.image.load("lid17.png")
        self.lid18 = pygame.image.load("lid18.png")
        self.lid19 = pygame.image.load("lid19.png")
        self.lid20 = pygame.image.load("lid20.png")
        self.lid21 = pygame.image.load("lid21.png")
        self.lid22 = pygame.image.load("lid22.png")
        self.lid23 = pygame.image.load("lid23.png")
        self.lid24 = pygame.image.load("lid24.png")

        self.lid1_hover_over = pygame.image.load("lid1_hover_over.png")
        self.lid2_hover_over = pygame.image.load("lid2_hover_over.png")
        self.lid3_hover_over = pygame.image.load("lid3_hover_over.png")
        self.lid4_hover_over = pygame.image.load("lid4_hover_over.png")
        self.lid5_hover_over = pygame.image.load("lid5_hover_over.png")
        self.lid6_hover_over = pygame.image.load("lid6_hover_over.png")
        self.lid7_hover_over = pygame.image.load("lid7_hover_over.png")
        self.lid8_hover_over = pygame.image.load("lid8_hover_over.png")
        self.lid9_hover_over = pygame.image.load("lid9_hover_over.png")
        self.lid10_hover_over = pygame.image.load("lid10_hover_over.png")
        self.lid11_hover_over = pygame.image.load("lid11_hover_over.png")
        self.lid12_hover_over = pygame.image.load("lid12_hover_over.png")
        self.lid13_hover_over = pygame.image.load("lid13_hover_over.png")
        self.lid14_hover_over = pygame.image.load("lid14_hover_over.png")
        self.lid15_hover_over = pygame.image.load("lid15_hover_over.png")
        self.lid16_hover_over = pygame.image.load("lid16_hover_over.png")
        self.lid17_hover_over = pygame.image.load("lid17_hover_over.png")
        self.lid18_hover_over = pygame.image.load("lid18_hover_over.png")
        self.lid19_hover_over = pygame.image.load("lid19_hover_over.png")
        self.lid20_hover_over = pygame.image.load("lid20_hover_over.png")
        self.lid21_hover_over = pygame.image.load("lid21_hover_over.png")
        self.lid22_hover_over = pygame.image.load("lid22_hover_over.png")
        self.lid23_hover_over = pygame.image.load("lid23_hover_over.png")
        self.lid24_hover_over = pygame.image.load("lid24_hover_over.png")

    def what_time_is_it(self):
        """Funktion that returns the date in the correct form."""
        time = datetime.datetime.now()
        day = time.day
        month = time.month
        year = time.year
        return f"{day}.{month}.{year}"

    def sound_management(self):
        """
        Funktion that is responsible
        for making the sound and music buttons work as intended.
        """

        self.sound_button_x = 224 >= self.x-self.sound_button_on.get_width() and 309 <= self.x+self.sound_button_on.get_width()
        self.sound_button_y = 510 >= self.y-self.sound_button_on.get_height() and 595 <= self.y+self.sound_button_on.get_height()
        if self.sound_button_x and self.sound_button_y:

            if self.sounds_on:
                self.sound_button = self.display.blit(self.sound_button_on_hover_over, (224, 510))
            else:
                self.sound_button = self.display.blit(self.sound_button_off_hover_over, (224, 510))

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
                self.sound_button = self.display.blit(self.sound_button_on, (224, 510))
            else:
                self.sound_button = self.display.blit(self.sound_button_off, (224, 510))

        self.music_button_x = 324 >= self.x-self.music_button_on.get_width() and 409 <= self.x+self.music_button_on.get_width()
        self.music_button_y = 510 >= self.y-self.music_button_on.get_height() and 595 <= self.y+self.music_button_on.get_height()
        if self.music_button_x and self.music_button_y:

            if self.music_on:
                self.music_button = self.display.blit(self.music_button_on_hover_over, (324, 510))
            else:
                self.music_button = self.display.blit(self.music_button_off_hover_over, (324, 510))

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
                self.music_button = self.display.blit(self.music_button_on, (324, 510))
            else:
                self.music_button = self.display.blit(self.music_button_off, (324, 510))

    def lids(self):
        """Funktion that is responsible for making the calendar's lids work as intended."""

        #Lids Y
        #85, 170, 255, 340, 425, 510
        #Lids X
        #105, 209, 313, 416

        #First lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid1_x = -10 >= self.x-self.lid1.get_width() and 96 <= self.x+self.lid1.get_width()
        self.lid1_y = -10 >= self.y-self.lid1.get_height() and 77 <= self.y+self.lid1.get_height()
        if self.opened1:
            if self.lid1_x and self.lid1_y:
                self.lid_1 = None
            else:
                self.lid_1 = None
        else:
            if self.lid1_x and self.lid1_y:
                self.lid_1 = self.display.blit(self.lid1_hover_over, (0, 0))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "17.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened1 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened1 = True
                            self.lid_1 = None
                            self.opened1 = True
                    else:
                        if self.sound_lock1 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock1 = True
                        self.lid_1 = self.display.blit(self.lid1, (0, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 0))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_1 = self.display.blit(self.lid1, (0, 0))
                self.is_it_time = None

        #Second lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid2_x = 95 >= self.x-self.lid2.get_width() and 201 <= self.x+self.lid2.get_width()
        self.lid2_y = -10 >= self.y-self.lid2.get_height() and 77 <= self.y+self.lid2.get_height()
        if self.opened2:
            if self.lid2_x and self.lid2_y:
                self.lid_2 = None
            else:
                self.lid_2 = None
        else:
            if self.lid2_x and self.lid2_y:
                self.lid_2 = self.display.blit(self.lid2_hover_over, (105, 0))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "20.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened2 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened2 = True
                            self.lid_2 = None
                            self.opened2 = True
                    else:
                        if self.sound_lock2 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock2 = True
                        self.lid_2 = self.display.blit(self.lid2, (105, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (105, 0))
                else:
                    self.sound_lock2 = False
            else:
                self.lid_2  = self.display.blit(self.lid2, (105, 0))
                self.is_it_time = None

        #Third lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid3_x = 199 >= self.x-self.lid3.get_width() and 305 <= self.x+self.lid3.get_width()
        self.lid3_y = -10 >= self.y-self.lid3.get_height() and 77 <= self.y+self.lid3.get_height()
        if self.opened3:
            if self.lid3_x and self.lid3_y:
                self.lid_3 = None
            else:
                self.lid_3 = None
        else:
            if self.lid3_x and self.lid3_y:
                self.lid_3 = self.display.blit(self.lid3_hover_over, (209, 0))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "24.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened3 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened3 = True
                            self.lid_3 = None
                            self.opened3 = True
                    else:
                        if self.sound_lock3 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock3 = True
                        self.lid_3 = self.display.blit(self.lid3, (209, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (209, 0))
                else:
                    self.sound_lock3 = False
            else:
                self.lid_3  = self.display.blit(self.lid3, (209, 0))
                self.is_it_time = None

        #Fourth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid4_x = 303 >= self.x-self.lid4.get_width() and 409 <= self.x+self.lid4.get_width()
        self.lid4_y = -10 >= self.y-self.lid4.get_height() and 77 <= self.y+self.lid4.get_height()
        if self.opened4:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.lid4_hover_over, (313, 0))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "9.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock4 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock4 = True
                        self.lid_4 = self.display.blit(self.lid4, (313, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (313, 0))
                else:
                    self.sound_lock4 = False
            else:
                self.lid_4  = self.display.blit(self.lid4, (313, 0))
                self.is_it_time = None

        #Fifth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid5_x = -10 >= self.x-self.lid5.get_width() and 96 <= self.x+self.lid5.get_width()
        self.lid5_y = 76 >= self.y-self.lid5.get_height() and 163 <= self.y+self.lid5.get_height()
        if self.opened5:
            if self.lid5_x and self.lid5_y:
                self.lid_5 = None
            else:
                self.lid_5 = None
        else:
            if self.lid5_x and self.lid5_y:
                self.lid_5 = self.display.blit(self.lid5_hover_over, (0, 86))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "12.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened5 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened5 = True
                            self.lid_5 = None
                            self.opened5 = True
                    else:
                        if self.sound_lock5 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock5 = True
                        self.lid_5 = self.display.blit(self.lid5, (0, 86))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 86))
                else:
                    self.sound_lock5 = False
            else:
                self.lid_5  = self.display.blit(self.lid5, (0, 86))
                self.is_it_time = None

        #Sixth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid6_x = 95 >= self.x-self.lid6.get_width() and 201 <= self.x+self.lid6.get_width()
        self.lid6_y = 76 >= self.y-self.lid6.get_height() and 163 <= self.y+self.lid6.get_height()
        if self.opened6:
            if self.lid6_x and self.lid6_y:
                self.lid_6 = None
            else:
                self.lid_6 = None
        else:
            if self.lid6_x and self.lid6_y:
                self.lid_6 = self.display.blit(self.lid6_hover_over, (105, 86))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "6.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened6 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened6 = True
                            self.lid_6 = None
                            self.opened6 = True
                    else:
                        if self.sound_lock6 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock6 = True
                        self.lid_6 = self.display.blit(self.lid6, (105, 86))
                        self.is_it_time = self.display.blit(self.not_time_yet, (105, 86))
                else:
                    self.sound_lock6 = False
            else:
                self.lid_6  = self.display.blit(self.lid6, (105, 86))
                self.is_it_time = None

        #Seventh lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid7_x = 199 >= self.x-self.lid7.get_width() and 308 <= self.x+self.lid7.get_width()
        self.lid7_y = 76 >= self.y-self.lid7.get_height() and 163 <= self.y+self.lid7.get_height()
        if self.opened7:
            if self.lid7_x and self.lid7_y:
                self.lid_7 = None
            else:
                self.lid_7 = None
        else:
            if self.lid7_x and self.lid7_y:
                self.lid_7 = self.display.blit(self.lid7_hover_over, (209, 86))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "14.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened7 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened7 = True
                            self.lid_7 = None
                            self.opened7 = True
                    else:
                        if self.sound_lock7 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock7 = True
                        self.lid_7 = self.display.blit(self.lid7, (209, 86))
                        self.is_it_time = self.display.blit(self.not_time_yet, (209, 86))
                else:
                    self.sound_lock7 = False
            else:
                self.lid_7  = self.display.blit(self.lid7, (209, 86))
                self.is_it_time = None

        #Eighth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid8_x = 303 >= self.x-self.lid8.get_width() and 409 <= self.x+self.lid8.get_width()
        self.lid8_y = 76 >= self.y-self.lid8.get_height() and 163 <= self.y+self.lid8.get_height()
        if self.opened8:
            if self.lid8_x and self.lid4_y:
                self.lid_8 = None
            else:
                self.lid_8 = None
        else:
            if self.lid8_x and self.lid8_y:
                self.lid_8 = self.display.blit(self.lid8_hover_over, (313, 86))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "3.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened8 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened8 = True
                            self.lid_8 = None
                            self.opened8 = True
                    else:
                        if self.sound_lock8 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock8 = True
                        self.lid_8 = self.display.blit(self.lid8, (313, 86))
                        self.is_it_time = self.display.blit(self.not_time_yet, (313, 86))
                else:
                    self.sound_lock8 = False
            else:
                self.lid_8  = self.display.blit(self.lid8, (313, 86))
                self.is_it_time = None

        #Ninth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid9_x = -10 >= self.x-self.lid9.get_width() and 96 <= self.x+self.lid9.get_width()
        self.lid9_y = 161 >= self.y-self.lid9.get_height() and 248 <= self.y+self.lid9.get_height()
        if self.opened9:
            if self.lid9_x and self.lid9_y:
                self.lid_9 = None
            else:
                self.lid_9 = None
        else:
            if self.lid9_x and self.lid9_y:
                self.lid_9 = self.display.blit(self.lid9_hover_over, (0, 171))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "4.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened9 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened9 = True
                            self.lid_9 = None
                            self.opened9 = True
                    else:
                        if self.sound_lock9 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock9 = True
                        self.lid_9 = self.display.blit(self.lid9, (0, 171))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 171))
                else:
                    self.sound_lock9 = False
            else:
                self.lid_9  = self.display.blit(self.lid9, (0, 171))
                self.is_it_time = None

        #Tenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid10_x = 95 >= self.x-self.lid10.get_width() and 201 <= self.x+self.lid10.get_width()
        self.lid10_y = 161 >= self.y-self.lid10.get_height() and 248 <= self.y+self.lid10.get_height()
        if self.opened10:
            if self.lid10_x and self.lid10_y:
                self.lid_10 = None
            else:
                self.lid_10 = None
        else:
            if self.lid10_x and self.lid10_y:
                self.lid_10 = self.display.blit(self.lid10_hover_over, (105, 171))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "19.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened10 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened10 = True
                            self.lid_10 = None
                            self.opened10 = True
                    else:
                        if self.sound_lock10 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock10 = True
                        self.lid_10 = self.display.blit(self.lid10, (105, 171))
                        self.is_it_time = self.display.blit(self.not_time_yet, (105, 171))
                else:
                    self.sound_lock10 = False
            else:
                self.lid_10  = self.display.blit(self.lid10, (105, 171))
                self.is_it_time = None

        #Eleventh lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid11_x = 199 >= self.x-self.lid11.get_width() and 305 <= self.x+self.lid11.get_width()
        self.lid11_y = 161 >= self.y-self.lid11.get_height() and 248 <= self.y+self.lid11.get_height()
        if self.opened11:
            if self.lid11_x and self.lid11_y:
                self.lid_11 = None
            else:
                self.lid_11 = None
        else:
            if self.lid11_x and self.lid11_y:
                self.lid_11 = self.display.blit(self.lid11_hover_over, (209, 171))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "22.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened11 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened11 = True
                            self.lid_11 = None
                            self.opened11 = True
                    else:
                        if self.sound_lock11 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock11 = True
                        self.lid_11 = self.display.blit(self.lid11, (209, 171))
                        self.is_it_time = self.display.blit(self.not_time_yet, (209, 171))
                else:
                    self.sound_lock11 = False
            else:
                self.lid_11  = self.display.blit(self.lid11, (209, 171))
                self.is_it_time = None

        #Twelfth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid12_x = 303 >= self.x-self.lid12.get_width() and 409 <= self.x+self.lid12.get_width()
        self.lid12_y = 161 >= self.y-self.lid12.get_height() and 248 <= self.y+self.lid12.get_height()
        if self.opened12:
            if self.lid12_x and self.lid12_y:
                self.lid_12 = None
            else:
                self.lid_12 = None
        else:
            if self.lid12_x and self.lid12_y:
                self.lid_12 = self.display.blit(self.lid12_hover_over, (313, 171))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "16.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened12 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened12 = True
                            self.lid_12 = None
                            self.opened12 = True
                    else:
                        if self.sound_lock12 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock12 = True
                        self.lid_12 = self.display.blit(self.lid12, (313, 171))
                        self.is_it_time = self.display.blit(self.not_time_yet, (313, 171))
                else:
                    self.sound_lock12 = False
            else:
                self.lid_12  = self.display.blit(self.lid12, (313, 171))
                self.is_it_time = None

        #Thirteenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid13_x = -10 >= self.x-self.lid13.get_width() and 96 <= self.x+self.lid13.get_width()
        self.lid13_y = 246 >= self.y-self.lid13.get_height() and 333 <= self.y+self.lid13.get_height()
        if self.opened13:
            if self.lid13_x and self.lid13_y:
                self.lid_13 = None
            else:
                self.lid_13 = None
        else:
            if self.lid13_x and self.lid13_y:
                self.lid_13 = self.display.blit(self.lid13_hover_over, (0, 256))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "21.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened13 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened13 = True
                            self.lid_13 = None
                            self.opened13 = True
                    else:
                        if self.sound_lock13 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock13 = True
                        self.lid_13 = self.display.blit(self.lid13, (0, 256))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 256))
                else:
                    self.sound_lock13 = False
            else:
                self.lid_13  = self.display.blit(self.lid13, (0, 256))
                self.is_it_time = None

        #Fourteenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid14_x = 95 >= self.x-self.lid14.get_width() and 201 <= self.x+self.lid14.get_width()
        self.lid14_y = 256 >= self.y-self.lid14.get_height() and 333 <= self.y+self.lid14.get_height()
        if self.opened14:
            if self.lid4_x and self.lid14_y:
                self.lid_14 = None
            else:
                self.lid_14 = None
        else:
            if self.lid14_x and self.lid14_y:
                self.lid_14 = self.display.blit(self.lid14_hover_over, (105, 256))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "15.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened14 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened14 = True
                            self.lid_14 = None
                            self.opened14 = True
                    else:
                        if self.sound_lock14 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock14 = True
                        self.lid_14 = self.display.blit(self.lid14, (105, 256))
                        self.is_it_time = self.display.blit(self.not_time_yet, (105, 256))
                else:
                    self.sound_lock14 = False
            else:
                self.lid_14  = self.display.blit(self.lid14, (105, 256))
                self.is_it_time = None

        #Fifteenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid15_x = 199 >= self.x-self.lid15.get_width() and 305 <= self.x+self.lid15.get_width()
        self.lid15_y = 246 >= self.y-self.lid15.get_height() and 333 <= self.y+self.lid15.get_height()
        if self.opened15:
            if self.lid15_x and self.lid15_y:
                self.lid_15 = None
            else:
                self.lid_15 = None
        else:
            if self.lid15_x and self.lid15_y:
                self.lid_15 = self.display.blit(self.lid15_hover_over, (209, 256))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "1.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened15 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened15 = True
                            self.lid_15 = None
                            self.opened15 = True
                    else:
                        if self.sound_lock15 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock15 = True
                        self.lid_15 = self.display.blit(self.lid15, (209, 256))
                        self.is_it_time = self.display.blit(self.not_time_yet, (209, 256))
                else:
                    self.sound_lock15 = False
            else:
                self.lid_15  = self.display.blit(self.lid15, (209, 256))
                self.is_it_time = None

        #Sixteenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid16_x = 303 >= self.x-self.lid16.get_width() and 409 <= self.x+self.lid16.get_width()
        self.lid16_y = 246 >= self.y-self.lid16.get_height() and 333 <= self.y+self.lid16.get_height()
        if self.opened16:
            if self.lid16_x and self.lid16_y:
                self.lid_16 = None
            else:
                self.lid_16 = None
        else:
            if self.lid16_x and self.lid16_y:
                self.lid_16 = self.display.blit(self.lid16_hover_over, (313, 256))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "7.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened16 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened16 = True
                            self.lid_16 = None
                            self.opened16 = True
                    else:
                        if self.sound_lock16 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock16 = True
                        self.lid_16 = self.display.blit(self.lid16, (313, 256))
                        self.is_it_time = self.display.blit(self.not_time_yet, (313, 256))
                else:
                    self.sound_lock16 = False
            else:
                self.lid_16  = self.display.blit(self.lid16, (313, 256))
                self.is_it_time = None

        #Seventeenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid17_x = -10 >= self.x-self.lid17.get_width() and 96 <= self.x+self.lid17.get_width()
        self.lid17_y = 331 >= self.y-self.lid17.get_height() and 418 <= self.y+self.lid17.get_height()
        if self.opened17:
            if self.lid17_x and self.lid17_y:
                self.lid_17 = None
            else:
                self.lid_17 = None
        else:
            if self.lid17_x and self.lid17_y:
                self.lid_17 = self.display.blit(self.lid17_hover_over, (0, 341))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "10.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened17 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened17 = True
                            self.lid_17 = None
                            self.opened17 = True
                    else:
                        if self.sound_lock17 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock17 = True
                        self.lid_17 = self.display.blit(self.lid17, (0, 341))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 341))
                else:
                    self.sound_lock17 = False
            else:
                self.lid_17  = self.display.blit(self.lid17, (0, 341))
                self.is_it_time = None

        #Eighteenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid18_x = 95 >= self.x-self.lid18.get_width() and 201 <= self.x+self.lid18.get_width()
        self.lid18_y = 331 >= self.y-self.lid18.get_height() and 418 <= self.y+self.lid18.get_height()
        if self.opened18:
            if self.lid18_x and self.lid18_y:
                self.lid_18 = None
            else:
                self.lid_18 = None
        else:
            if self.lid18_x and self.lid18_y:
                self.lid_18 = self.display.blit(self.lid18_hover_over, (105, 341))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "23.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened18 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened18 = True
                            self.lid_18 = None
                            self.opened18 = True
                    else:
                        if self.sound_lock18 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock18 = True
                        self.lid_18 = self.display.blit(self.lid18, (105, 341))
                        self.is_it_time = self.display.blit(self.not_time_yet, (105, 341))
                else:
                    self.sound_lock18 = False
            else:
                self.lid_18  = self.display.blit(self.lid18, (105, 341))
                self.is_it_time = None

        #Nineteenth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid19_x = 199 >= self.x-self.lid19.get_width() and 305 <= self.x+self.lid19.get_width()
        self.lid19_y = 331 >= self.y-self.lid19.get_height() and 418 <= self.y+self.lid19.get_height()
        if self.opened19:
            if self.lid19_x and self.lid19_y:
                self.lid_19 = None
            else:
                self.lid_19 = None
        else:
            if self.lid19_x and self.lid19_y:
                self.lid_19 = self.display.blit(self.lid19_hover_over, (209, 341))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "18.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened19 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened19 = True
                            self.lid_19 = None
                            self.opened19 = True
                    else:
                        if self.sound_lock19 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock19 = True
                        self.lid_19 = self.display.blit(self.lid19, (209, 341))
                        self.is_it_time = self.display.blit(self.not_time_yet, (209, 341))
                else:
                    self.sound_lock19 = False
            else:
                self.lid_19  = self.display.blit(self.lid19, (209, 341))
                self.is_it_time = None

        #Twentieth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid20_x = 303 >= self.x-self.lid20.get_width() and 409 <= self.x+self.lid20.get_width()
        self.lid20_y = 331 >= self.y-self.lid20.get_height() and 418 <= self.y+self.lid20.get_height()
        if self.opened20:
            if self.lid20_x and self.lid20_y:
                self.lid_20 = None
            else:
                self.lid_20 = None
        else:
            if self.lid20_x and self.lid20_y:
                self.lid_20 = self.display.blit(self.lid20_hover_over, (313, 341))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "11.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened20 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened20 = True
                            self.lid_20 = None
                            self.opened20 = True
                    else:
                        if self.sound_lock20 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock20 = True
                        self.lid_20 = self.display.blit(self.lid20, (313, 341))
                        self.is_it_time = self.display.blit(self.not_time_yet, (313, 341))
                else:
                    self.sound_lock20 = False
            else:
                self.lid_20  = self.display.blit(self.lid20, (313, 341))
                self.is_it_time = None

        #Twenty-first lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid21_x = -10 >= self.x-self.lid21.get_width() and 96 <= self.x+self.lid21.get_width()
        self.lid21_y = 416 >= self.y-self.lid21.get_height() and 503 <= self.y+self.lid21.get_height()
        if self.opened21:
            if self.lid21_x and self.lid21_y:
                self.lid_21 = None
            else:
                self.lid_21 = None
        else:
            if self.lid21_x and self.lid21_y:
                self.lid_21 = self.display.blit(self.lid21_hover_over, (0, 426))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "2.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened21 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened21 = True
                            self.lid_21 = None
                            self.opened21 = True
                    else:
                        if self.sound_lock21 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock21 = True
                        self.lid_21 = self.display.blit(self.lid21, (0, 426))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 426))
                else:
                    self.sound_lock21 = False
            else:
                self.lid_21  = self.display.blit(self.lid21, (0, 426))
                self.is_it_time = None

        #Twenty-second lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid22_x = 95 >= self.x-self.lid22.get_width() and 201 <= self.x+self.lid22.get_width()
        self.lid22_y = 416 >= self.y-self.lid22.get_height() and 503 <= self.y+self.lid22.get_height()
        if self.opened22:
            if self.lid22_x and self.lid22_y:
                self.lid_22 = None
            else:
                self.lid_22 = None
        else:
            if self.lid22_x and self.lid22_y:
                self.lid_22 = self.display.blit(self.lid22_hover_over, (105, 426))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "8.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened22 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened22 = True
                            self.lid_22 = None
                            self.opened22 = True
                    else:
                        if self.sound_lock22 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock22 = True
                        self.lid_22 = self.display.blit(self.lid22, (105, 426))
                        self.is_it_time = self.display.blit(self.not_time_yet, (105, 426))
                else:
                    self.sound_lock22 = False
            else:
                self.lid_22  = self.display.blit(self.lid22, (105, 426))
                self.is_it_time = None

        #Twenty-third lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid23_x = 199 >= self.x-self.lid23.get_width() and 305 <= self.x+self.lid23.get_width()
        self.lid23_y = 416 >= self.y-self.lid23.get_height() and 503 <= self.y+self.lid23.get_height()
        if self.opened23:
            if self.lid23_x and self.lid23_y:
                self.lid_23 = None
            else:
                self.lid_23 = None
        else:
            if self.lid23_x and self.lid23_y:
                self.lid_23 = self.display.blit(self.lid23_hover_over, (209, 426))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "13.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened23 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened23 = True
                            self.lid_23 = None
                            self.opened23 = True
                    else:
                        if self.sound_lock23 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock23 = True
                        self.lid_23 = self.display.blit(self.lid23, (209, 426))
                        self.is_it_time = self.display.blit(self.not_time_yet, (209, 426))
                else:
                    self.sound_lock23 = False
            else:
                self.lid_23  = self.display.blit(self.lid23, (209, 426))
                self.is_it_time = None

        #Twenty-fourth lid
        #X = -10 and +96
        #Y = -10 +77
        self.lid24_x = 303 >= self.x-self.lid24.get_width() and 409 <= self.x+self.lid24.get_width()
        self.lid24_y = 416 >= self.y-self.lid24.get_height() and 503 <= self.y+self.lid24.get_height()
        if self.opened24:
            if self.lid24_x and self.lid24_y:
                self.lid_24 = None
            else:
                self.lid_24 = None
        else:
            if self.lid24_x and self.lid24_y:
                self.lid_24 = self.display.blit(self.lid24_hover_over, (313, 426))
                if self.mouse_button_down:
                    if self.what_time_is_it() == "5.12.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened24 is False:
                            if self.sounds_on:
                                self.opening_sound.play()
                            self.opened24 = True
                            self.lid_24 = None
                            self.opened24 = True
                    else:
                        if self.sound_lock24 is False:
                            if self.sounds_on:
                                self.locked_sound.play()
                            self.sound_lock24 = True
                        self.lid_24 = self.display.blit(self.lid24, (313, 426))
                        self.is_it_time = self.display.blit(self.not_time_yet, (313, 426))
                else:
                    self.sound_lock24 = False
            else:
                self.lid_24  = self.display.blit(self.lid24, (313, 426))
                self.is_it_time = None

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
                self.x = event.pos[0]-self.mouse.get_width()/2
                self.y = event.pos[1]-self.mouse.get_height()/2

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down = True
                print("You pushed the button", event.button, "At the", event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_down = False
                print("You stopped pushing the button", event.button, "At the", event.pos)
            if event.type == pygame.QUIT:
                exit()

    def draw_the_calendar(self):
        """Funktion that basically draws the calendar."""

        self.display.fill((0,100,100))

        self.display.blit(self.background, (0, 0))

        self.sound_management()

        self.lids()

        self.display.blit(self.mouse, (self.x, self.y))

        pygame.display.flip()

if __name__ == "__main__":
    ChristmasCalendar()
