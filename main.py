import pygame
import datetime 

class ChristmasCalendar:
    def __init__(self):
        pygame.init()

        self.download_pictures()

        self.opening_sound = pygame.mixer.Sound('opening_sound.wav')
        self.locked_sound = pygame.mixer.Sound('locked_sound.wav')
        #self.hover_over = pygame.mixer.Sound('hover_over.wav')

        #self.music = pygame.mixer.music.load('music.wav')
        #pygame.mixer.music.play(loops=-1)

        self.height = 700
        self.width = 600

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
        self.lid1 = pygame.image.load("lid1.png")
        self.lid2 = pygame.image.load("lid2.png")
        self.lid1_open = pygame.image.load("lid1_open.png")
        self.lid2_open = pygame.image.load("lid2_open.png")
        self.lid1_hover_over = pygame.image.load("lid1_hover_over.png")
        self.lid2_hover_over = pygame.image.load("lid2_hover_over.png")
        self.lid1_open_hover_over = pygame.image.load("lid1_open_hover_over.png")
        self.lid2_open_hover_over = pygame.image.load("lid2_open_hover_over.png")
        self.mouse = pygame.image.load("mouse.png")
        self.not_time_yet = pygame.image.load("not_time_yet.png")
        self.sounds_On = pygame.image.load("sounds_On.png")
        self.sounds_Off = pygame.image.load("sounds_Off.png")
        self.music_On = pygame.image.load("music_On.png")
        self.music_Off = pygame.image.load("music_Off.png")
        self.background2_lid1 = pygame.image.load("background2_lid1.png")
        self.background2_lid2 = pygame.image.load("background2_lid2.png")

        #Will be used soon
        #self.background2_lid3 = pygame.image.load("background2_lid3.png")
        #self.background2_lid4 = pygame.image.load("background2_lid4.png")
        #self.background2_lid5 = pygame.image.load("background2_lid5.png")
        #self.background2_lid6 = pygame.image.load("background2_lid6.png")
        #self.background2_lid7 = pygame.image.load("background2_lid7.png")
        #self.background2_lid8 = pygame.image.load("background2_lid8.png")
        #self.background2_lid9 = pygame.image.load("background2_lid9.png")
        #self.background2_lid10 = pygame.image.load("background2_lid10.png")
        #self.background2_lid11 = pygame.image.load("background2_lid11.png")
        #self.background2_lid12 = pygame.image.load("background2_lid12.png")
        #self.background2_lid13 = pygame.image.load("background2_lid13.png")
        #self.background2_lid14 = pygame.image.load("background2_lid14.png")
        #self.background2_lid15 = pygame.image.load("background2_lid15.png")
        #self.background2_lid16 = pygame.image.load("background2_lid16.png")
        #self.background2_lid17 = pygame.image.load("background2_lid17.png")
        #self.background2_lid18 = pygame.image.load("background2_lid18.png")
        #self.background2_lid19 = pygame.image.load("background2_lid19.png")
        #self.background2_lid20 = pygame.image.load("background2_lid20.png")
        #self.background2_lid21 = pygame.image.load("background2_lid21.png")
        #self.background2_lid22 = pygame.image.load("background2_lid22.png")
        #self.background2_lid23 = pygame.image.load("background2_lid23.png")
        #self.background2_lid24 = pygame.image.load("background2_lid24.png")

        self.background2_lid1_hover_over = pygame.image.load("background2_lid1_hover_over.png")
        self.background2_lid2_hover_over = pygame.image.load("background2_lid2_hover_over.png")

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
        self.sound_button_x = 0 >= self.x-self.background2_lid1.get_width() and 0 <= self.x+self.background2_lid1.get_width()
        self.sound_button_y = 0 >= self.y-self.background2_lid1.get_height() and 0 <= self.y+self.background2_lid1.get_height()
        if self.sound_button_x and self.sound_button_y:
            self.sound_button = self.display.blit(self.background2_lid1_hover_over, (550, 0))
            if self.buttonDown == True:
                if self.soundsOn == True:
                    pygame.mixer.pause()
                else:
                    pygame.mixer.unpause()
        else:
            self.sound_button = self.display.blit(self.background2_lid1, (550, 0))

        #Music button
        self.music_button_x = 0 >= self.x-self.music_On.get_width() and 0 <= self.x+self.music_On.get_width()
        self.music_button_y = 0 >= self.y-self.music_On.get_height() and 0 <= self.y+self.music_On.get_height()
        if self.music_button_x and self.music_button_y:
            if self.musicOn == True:
                self.music_button = self.display.blit(self.musicOn, (550, 0))
            else:
                self.music_button = self.display.blit(self.musicOff, (550, 0))
            if self.buttonDown == True:
                if self.musicOn == True:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        else:
            if self.musicOn == True:
                self.music_button = self.display.blit(self.music_On, (550, 0))
            else:
                self.music_button = self.display.blit(self.music_Off, (550, 0))



    def lids(self):

        #Testing
        #First lid
        self.lid1_x = 0 >= self.x-self.background2_lid1.get_width() and 0 <= self.x+self.background2_lid1.get_width()
        self.lid1_y = 0 >= self.y-self.background2_lid1.get_height() and 0 <= self.y+self.background2_lid1.get_height()
        if self.opened1 == True:
            if self.lid1_x and self.lid1_y:
                self.lid_1 = None
            else:
                self.lid_1 = None
        else:
            if self.lid1_x and self.lid1_y:
                self.lid_1 = self.display.blit(self.background2_lid1_hover_over, (0, 0))
                if self.buttonDown == True:
                    #if self.what_time_is_it() == "1.12.2021":
                    #<Date>
                    if self.what_time_is_it() == "21.11.2021":
                        #Here will be a question
                        #Think how would be the best way to implement the questions
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
                        self.lid_1 = self.display.blit(self.background2_lid1_hover_over, (0, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (0, 0))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_1 = self.display.blit(self.background2_lid1, (0, 0))
                #Delete this?
                self.is_it_time = None

        #Second lid
        #So pretty much X goes 85 over and y 50
        self.lid2_x = 150 >= self.x-self.background2_lid2.get_width() and 285 <= self.x+self.background2_lid2.get_width()
        self.lid2_y = 0 >= self.y-self.background2_lid2.get_height() and 0 <= self.y+self.background2_lid2.get_height()
        if self.opened2 == True:
            if self.lid2_x and self.lid2_y:
                self.lid_2 = None
            else:
                self.lid_2 = None
        else:
            if self.lid2_x and self.lid2_y:
                self.lid_2 = self.display.blit(self.background2_lid2_hover_over, (150, 0))
                if self.buttonDown == True:
                    #if self.what_time_is_it() == "1.12.2021":
                    #<Date>
                    if self.what_time_is_it() == "21.11.2021":
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
                        self.lid_2 = self.display.blit(self.background2_lid2_hover_over, (150, 0))
                        self.is_it_time = self.display.blit(self.not_time_yet, (150, 0))
                else:
                    self.sound_lock1 = False
            else:
                self.lid_2  = self.display.blit(self.background2_lid2, (150, 0))
                #Delete this?
                self.is_it_time = None

        #Third lid
        #Fourth lid
        #Fifth lid
        #Sixth lid
        #Seventh lid
        #Eighth lid
        #Ninth lid
        #Tenth lid
        #Eleventh lid
        #Twelfth lid
        #Thirteenth lid
        #Fourteenth lid
        #Fifteenth lid
        #Sixteenth lid
        #Seventeenth lid
        #Eighteenth lid
        #Nineteenth lid
        #Twentieth lid
        #Twenty-first lid
        #Twenty-second lid
        #Twenty-third lid
        #Twenty-fourth lid

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