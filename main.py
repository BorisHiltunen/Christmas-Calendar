import pygame
import datetime 

class ChristmasCalendar:
    def __init__(self):
        pygame.init()

        self.download_pictures()

        self.opening_sound = pygame.mixer.Sound('opening_sound.wav')
        self.locked_sound = pygame.mixer.Sound('locked_sound.wav')
        #self.hover_over = pygame.mixer.Sound('hover_over.wav')

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

        #Tells whether mousebutton is pushed or not
        self.buttonDown = False

        self.soundsOn = True
        self.musicOn = True

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
 
        self.display = pygame.display.set_mode((self.width, self.height))
 
        pygame.display.set_caption("ChristmasCalendar")
 
        self.loop()

    def download_pictures(self):

        self.background = pygame.image.load("background.png")
        self.background = pygame.image.load("background2.png")
        self.mouse = pygame.image.load("mouse.png")
        self.not_time_yet = pygame.image.load("not_time_yet.png")
        self.sound_button_on = pygame.image.load("sound_button_on.png")
        #self.sound_button_off = pygame.image.load("sounds_Off.png")
        self.music_button_on = pygame.image.load("music_button_on.png")
        #self.music_button_off = pygame.image.load("music_Off.png")

        self.sound_button_on_hover_over = pygame.image.load("sound_button_on_hover_over.png")
        #self.sound_button_off_hover_over = pygame.image.load("sounds_Off_hover_over.png")
        self.music_button_on_hover_over = pygame.image.load("music_button_on_hover_over.png")
        #self.music_button_off_hover_over = pygame.image.load("music_Off_hover_over.png")
        self.background_real_cubes_lid1 = pygame.image.load("background_real_cubes_lid1.png")
        self.background_real_cubes_lid2 = pygame.image.load("background_real_cubes_lid2.png")
        self.background_real_cubes_lid3 = pygame.image.load("background_real_cubes_lid3.png")
        self.background_real_cubes_lid4 = pygame.image.load("background_real_cubes_lid4.png")
        self.background_real_cubes_lid5 = pygame.image.load("background_real_cubes_lid5.png")
        self.background_real_cubes_lid6 = pygame.image.load("background_real_cubes_lid6.png")
        self.background_real_cubes_lid7 = pygame.image.load("background_real_cubes_lid7.png")
        self.background_real_cubes_lid8 = pygame.image.load("background_real_cubes_lid8.png")
        self.background_real_cubes_lid9 = pygame.image.load("background_real_cubes_lid9.png")
        self.background_real_cubes_lid10 = pygame.image.load("background_real_cubes_lid10.png")
        self.background_real_cubes_lid11 = pygame.image.load("background_real_cubes_lid11.png")
        self.background_real_cubes_lid12 = pygame.image.load("background_real_cubes_lid12.png")
        self.background_real_cubes_lid13 = pygame.image.load("background_real_cubes_lid13.png")
        self.background_real_cubes_lid14 = pygame.image.load("background_real_cubes_lid14.png")
        self.background_real_cubes_lid15 = pygame.image.load("background_real_cubes_lid15.png")
        self.background_real_cubes_lid16 = pygame.image.load("background_real_cubes_lid16.png")
        self.background_real_cubes_lid17 = pygame.image.load("background_real_cubes_lid17.png")
        self.background_real_cubes_lid18 = pygame.image.load("background_real_cubes_lid18.png")
        self.background_real_cubes_lid19 = pygame.image.load("background_real_cubes_lid19.png")
        self.background_real_cubes_lid20 = pygame.image.load("background_real_cubes_lid20.png")
        self.background_real_cubes_lid21 = pygame.image.load("background_real_cubes_lid21.png")
        self.background_real_cubes_lid22 = pygame.image.load("background_real_cubes_lid22.png")
        self.background_real_cubes_lid23 = pygame.image.load("background_real_cubes_lid23.png")
        self.background_real_cubes_lid24 = pygame.image.load("background_real_cubes_lid24.png")

        self.background_real_cubes_lid1_hover_over = pygame.image.load("background_real_cubes_lid1_hover_over.png")
        self.background2_real_cubes_lid2_hover_over = pygame.image.load("background_real_cubes_lid2_hover_over.png")
        #self.background2_lid3_hover_over = pygame.image.load("background2_lid3_hover_over.png")
        #self.background2_lid4_hover_over = pygame.image.load("background2_lid4_hover_over.png")
        #self.background2_lid5_hover_over = pygame.image.load("background2_lid5_hover_over.png")
        #self.background2_lid6_hover_over = pygame.image.load("background2_lid6_hover_over.png")
        #self.background2_lid7_hover_over = pygame.image.load("background2_lid7_hover_over.png")
        #self.background2_lid8_hover_over = pygame.image.load("background2_lid8_hover_over.png")
        #self.background2_lid9_hover_over = pygame.image.load("background2_lid9_hover_over.png")
        #self.background2_lid10_hover_over = pygame.image.load("background2_lid10_hover_over.png")
        #self.background2_lid11_hover_over = pygame.image.load("background2_lid11_hover_over.png")
        #self.background2_lid12_hover_over = pygame.image.load("background2_lid12_hover_over.png")
        #self.background2_lid13_hover_over = pygame.image.load("background2_lid13_hover_over.png")
        #self.background2_lid14_hover_over = pygame.image.load("background2_lid14_hover_over.png")
        #self.background2_lid15_hover_over = pygame.image.load("background2_lid15_hover_over.png")
        #self.background2_lid16_hover_over = pygame.image.load("background2_lid16_hover_over.png")
        #self.background2_lid17_hover_over = pygame.image.load("background2_lid17_hover_over.png")
        #self.background2_lid18_hover_over = pygame.image.load("background2_lid18_hover_over.png")
        #self.background2_lid19_hover_over = pygame.image.load("background2_lid19_hover_over.png")
        #self.background2_lid20_hover_over = pygame.image.load("background2_lid20_hover_over.png")
        #self.background2_lid21_hover_over = pygame.image.load("background2_lid21_hover_over.png")
        #self.background2_lid22_hover_over = pygame.image.load("background2_lid22_hover_over.png")
        #self.background2_lid23_hover_over = pygame.image.load("background2_lid23_hover_over.png")
        #self.background2_lid24_hover_over = pygame.image.load("background2_lid24_hover_over.png")

    #Use datetime?
    def what_time_is_it(self):
        time = datetime.datetime.now()
        day = time.day
        month = time.month
        year = time.year
        return f"{day}.{month}.{year}"

    def sound_management(self):

        #Testing
        #Sound button
        self.sound_button_x = 224 >= self.x-self.sound_button_on.get_width() and 309 <= self.x+self.sound_button_on.get_width()
        self.sound_button_y = 510 >= self.y-self.sound_button_on.get_height() and 595 <= self.y+self.sound_button_on.get_height()
        if self.sound_button_x and self.sound_button_y:

            #It maybe needed to edit this?
            if self.musicOn == True:
                self.sound_button = self.display.blit(self.sound_button_on_hover_over, (224, 510))
            else:
                self.sound_button = self.display.blit(self.sound_button_on_hover_over, (224, 510))

            if self.buttonDown == True:
                print(self.soundsOn)
                if self.locked == False:
                    self.locked = True
                    if self.soundsOn == True:
                        #check how to darken and brighten an image
                        #dark = pg.Surface(self.sound_button_on.get_size()).convert_alpha()
                        #dark.fill((0, 0, 0, darken_percent*255))
                        #self.sound_button_on.blit(dark, (0, 0))
                        print("toimiiko")

                        pygame.mixer.pause()
                        self.soundsOn = False
                    else:
                        self.sound_button_on.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_ADD)
                        print("toimiiko2")
                        
                        pygame.mixer.unpause()
                        self.soundsOn = True
            else:
                self.locked = False

        else:
            if self.musicOn == True:
                self.sound_button = self.display.blit(self.sound_button_on, (224, 510))
            else:
                self.sound_button = self.display.blit(self.sound_button_on, (224, 510))

        #Music button
        self.music_button_x = 324 >= self.x-self.music_button_on.get_width() and 409 <= self.x+self.music_button_on.get_width()
        self.music_button_y = 510 >= self.y-self.music_button_on.get_height() and 595 <= self.y+self.music_button_on.get_height()
        if self.music_button_x and self.music_button_y:

            #It maybe needed to edit this?
            if self.musicOn == True:
                self.music_button = self.display.blit(self.music_button_on_hover_over, (324, 510))
            else:
                self.music_button = self.display.blit(self.music_button_on_hover_over, (324, 510))

            if self.buttonDown == True:
                print(self.musicOn)
                if self.locked == False:
                    self.locked = True
                    if self.musicOn == True:
                        pygame.mixer.music.pause()
                        self.musicOn = False
                    else:
                        pygame.mixer.music.unpause()
                        self.musicOn = True
            else:
                self.locked = False
        else:
            if self.musicOn == True:
                self.music_button = self.display.blit(self.music_button_on, (324, 510))
            else:
                self.music_button = self.display.blit(self.music_button_on, (324, 510))



    def lids(self):

        #Testing
        #First lid
        self.lid1_x = 0 >= self.x-self.background_real_cubes_lid1.get_width() and 0 <= self.x+self.background_real_cubes_lid1.get_width()
        self.lid1_y = 0 >= self.y-self.background_real_cubes_lid1.get_height() and 0 <= self.y+self.background_real_cubes_lid1.get_height()
        if self.opened1 == True:
            if self.lid1_x and self.lid1_y:
                self.lid_1 = None
            else:
                self.lid_1 = None
        else:
            if self.lid1_x and self.lid1_y:
                self.lid_1 = self.display.blit(self.background_real_cubes_lid1, (0, 0))
                if self.buttonDown == True:
                    print(self.locked)
                    if self.locked == False:
                        self.locked = True
                        if self.what_time_is_it() == "26.11.2021":
                            if self.opened1 == False:
                                self.opening_sound.play()
                                self.opened1 = True
                                self.lid_1 = None
                                self.opened1 = True
                        else:
                            if self.sound_lock1 == False:
                                self.locked_sound.play()
                                self.sound_lock1 = True
                            #For testing
                            print(self.what_time_is_it())
                            self.lid_1 = self.display.blit(self.background_real_cubes_lid1, (0, 0))
                            self.is_it_time = self.display.blit(self.not_time_yet, (0, 0))
                else:
                    self.sound_lock1 = False
                    self.locked = False
            else:
                self.lid_1 = self.display.blit(self.background_real_cubes_lid1, (0, 0))
                #Delete this?
                self.is_it_time = None

        #Second lid
        #So pretty much X goes 85 over and y 50
        self.lid2_x = 104 >= self.x-self.background_real_cubes_lid2.get_width() and 189 <= self.x+self.background_real_cubes_lid2.get_width()
        self.lid2_y = 0 >= self.y-self.background_real_cubes_lid2.get_height() and 0 <= self.y+self.background_real_cubes_lid2.get_height()
        if self.opened2 == True:
            if self.lid2_x and self.lid2_y:
                self.lid_2 = None
            else:
                self.lid_2 = None
        else:
            if self.lid2_x and self.lid2_y:
                self.lid_2 = self.display.blit(self.background_real_cubes_lid2, (104, 0))
                if self.buttonDown == True:
                    if self.locked == False:
                        self.locked = True
                        if self.what_time_is_it() == "25.11.2021":
                            #Here will be a question
                            #Think how would be the best way to implement the questions
                            if self.opened2 == False:
                                self.opening_sound.play()
                                self.opened2 = True
                                self.lid_2 = None
                                self.opened2 = True
                        else:
                            if self.sound_lock1 == False:
                                self.locked_sound.play()
                                self.sound_lock1 = True
                            #For testing
                            print(self.what_time_is_it())
                            self.lid_2 = self.display.blit(self.background_real_cubes_lid2, (104, 0))
                            self.is_it_time = self.display.blit(self.not_time_yet, (104, 0))
                else:
                    self.sound_lock1 = False
                    self.locked = False
            else:
                self.lid_2  = self.display.blit(self.background_real_cubes_lid2, (104, 0))
                #Delete this?
                self.is_it_time = None

        #Third lid
        #So pretty much X goes 85 over and y 50
        self.lid3_x = 208 >= self.x-self.background_real_cubes_lid3.get_width() and 293 <= self.x+self.background_real_cubes_lid3.get_width()
        self.lid3_y = 0 >= self.y-self.background_real_cubes_lid3.get_height() and 0 <= self.y+self.background_real_cubes_lid3.get_height()
        if self.opened2 == True:
            if self.lid3_x and self.lid3_y:
                self.lid_3 = None
            else:
                self.lid_3 = None
        else:
            if self.lid3_x and self.lid3_y:
                self.lid_3 = self.display.blit(self.background_real_cubes_lid3, (208, 0))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened3 == False:
                            self.opening_sound.play()
                            self.opened3 = True
                            self.lid_3 = None
                            self.opened3 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_3 = self.display.blit(self.background_real_cubes_lid3, (208, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (208, 0))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid3, (208, 0))
                #Delete this?
                self.is_it_time = None

        #Fourth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 0 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 0))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 0))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 0))
                #Delete this?
                self.is_it_time = None

        #Fifth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 0 >= self.x-self.background_real_cubes_lid4.get_width() and 85 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 85 >= self.y-self.background_real_cubes_lid4.get_height() and 170 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (0, 85))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (0, 85))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 85))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (0, 85))
                #Delete this?
                self.is_it_time = None

        #Sixth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 104 >= self.x-self.background_real_cubes_lid4.get_width() and 189 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 85 >= self.y-self.background_real_cubes_lid4.get_height() and 170 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (104, 85))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (104, 85))
                        self.is_it_time = self.display.blit(self.not_time_yet, (104, 85))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (104, 85))
                #Delete this?
                self.is_it_time = None

        #Seventh lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 208 >= self.x-self.background_real_cubes_lid4.get_width() and 293 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 85 >= self.y-self.background_real_cubes_lid4.get_height() and 85 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 85))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 85))
                        self.is_it_time = self.display.blit(self.not_time_yet, (208, 85))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (208, 85))
                #Delete this?
                self.is_it_time = None

        #Eighth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 0 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 85 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 85))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 85))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 85))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 85))
                #Delete this?
                self.is_it_time = None

        #Ninth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 0 >= self.x-self.background_real_cubes_lid4.get_width() and 85 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 170 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (0, 170))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (0, 170))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 170))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (0, 170))
                #Delete this?
                self.is_it_time = None

        #Tenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 104 >= self.x-self.background_real_cubes_lid4.get_width() and 0 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 170 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (104, 170))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (104, 170))
                        self.is_it_time = self.display.blit(self.not_time_yet, (104, 170))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (104, 170))
                #Delete this?
                self.is_it_time = None

        #Eleventh lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 208 >= self.x-self.background_real_cubes_lid4.get_width() and 0 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 170 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 170))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 170))
                        self.is_it_time = self.display.blit(self.not_time_yet, (208, 170))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (208, 170))
                #Delete this?
                self.is_it_time = None

        #Twelfth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 208 >= self.x-self.background_real_cubes_lid4.get_width() and 0 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 170 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 170))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 170))
                        self.is_it_time = self.display.blit(self.not_time_yet, (208, 170))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (208, 170))
                #Delete this?
                self.is_it_time = None

        #Thirteenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 208 >= self.x-self.background_real_cubes_lid4.get_width() and 0 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (208, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (208, 255))
                #Delete this?
                self.is_it_time = None

        #Fourteenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                #Delete this?
                self.is_it_time = None

        #Fifteenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 0 >= self.x-self.background_real_cubes_lid4.get_width() and 85 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (0, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (0, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (0, 255))
                #Delete this?
                self.is_it_time = None

        #Sixteenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 104 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (104, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (104, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (104, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (104, 255))
                #Delete this?
                self.is_it_time = None

        #Seventeenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 208 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (208, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (208, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (208, 255))
                #Delete this?
                self.is_it_time = None

        #Eighteenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                #Delete this?
                self.is_it_time = None

        #Nineteenth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                #Delete this?
                self.is_it_time = None

        #Twentieth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 255 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 255))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 255))
                #Delete this?
                self.is_it_time = None

        #Twenty-first lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 340 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 340))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                #Delete this?
                self.is_it_time = None

        #Twenty-second lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 340 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 340))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                #Delete this?
                self.is_it_time = None

        #Twenty-third lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 340 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 340))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                #Delete this?
                self.is_it_time = None

        #Twenty-fourth lid
        #So pretty much X goes 85 over and y 50
        self.lid4_x = 312 >= self.x-self.background_real_cubes_lid4.get_width() and 393 <= self.x+self.background_real_cubes_lid4.get_width()
        self.lid4_y = 340 >= self.y-self.background_real_cubes_lid4.get_height() and 0 <= self.y+self.background_real_cubes_lid4.get_height()
        if self.opened2 == True:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = None
            else:
                self.lid_4 = None
        else:
            if self.lid4_x and self.lid4_y:
                self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                if self.buttonDown == True:
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
                        if self.opened4 == False:
                            self.opening_sound.play()
                            self.opened4 = True
                            self.lid_4 = None
                            self.opened4 = True
                    else:
                        if self.sound_lock1 == False:
                            self.locked_sound.play()
                            self.sound_lock1 = True
                        #For testing
                        print(self.what_time_is_it())
                        self.lid_4 = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                        self.is_it_time = self.display.blit(self.not_time_yet, (312, 340))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_3  = self.display.blit(self.background_real_cubes_lid4, (312, 340))
                #Delete this?
                self.is_it_time = None

    def loop(self):
        clock = pygame.time.Clock()

        while True:
            self.draw_the_calendar()
            self.analyse_events()
            clock.tick(60)

    def analyse_events(self):

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.x = event.pos[0]-self.mouse.get_width()/2
                self.y = event.pos[1]-self.mouse.get_height()/2

                self.display.blit(self.mouse, (self.x, self.y))
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.buttonDown = True
                print("You pushed the button", event.button, "At the", event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                self.buttonDown = False
                print("You stopped pushing the button", event.button, "At the", event.pos)
            if event.type == pygame.QUIT:
                exit()

    def draw_the_calendar(self):
 
        self.display.fill((0,100,100))

        self.display.blit(self.background, (0, 0))

        self.sound_management()

        self.lids()

        self.display.blit(self.mouse, (self.x, self.y))
 
        pygame.display.flip()

if __name__ == "__main__":
    ChristmasCalendar()