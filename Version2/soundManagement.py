import pygame

def sound_management(self):

    #Testing
    #Sound button
    self.sound_button_x = 224 >= self.x-self.sound_button_on.get_width() and 309 <= self.x+self.sound_button_on.get_width()
    self.sound_button_y = 510 >= self.y-self.sound_button_on.get_height() and 595 <= self.y+self.sound_button_on.get_height()
    if self.sound_button_x and self.sound_button_y:

        #It maybe needed to edit this?
        if self.soundsOn == True:
            self.sound_button = self.display.blit(self.sound_button_on_hover_over, (224, 510))
        else:
            self.sound_button = self.display.blit(self.sound_button_off_hover_over, (224, 510))

        if self.buttonDown == True:
            if self.locked == False:
                self.locked = True
                if self.soundsOn == True:
                    self.soundsOn = False
                else:
                    self.soundsOn = True
        else:
            self.locked = False

    else:
        if self.soundsOn == True:
            self.sound_button = self.display.blit(self.sound_button_on, (224, 510))
        else:
            self.sound_button = self.display.blit(self.sound_button_off, (224, 510))

    #Music button
    self.music_button_x = 324 >= self.x-self.music_button_on.get_width() and 409 <= self.x+self.music_button_on.get_width()
    self.music_button_y = 510 >= self.y-self.music_button_on.get_height() and 595 <= self.y+self.music_button_on.get_height()
    if self.music_button_x and self.music_button_y:

        #It maybe needed to edit this?
        if self.musicOn == True:
            self.music_button = self.display.blit(self.music_button_on_hover_over, (324, 510))
        else:
            self.music_button = self.display.blit(self.music_button_off_hover_over, (324, 510))

        if self.buttonDown == True:
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
            self.music_button = self.display.blit(self.music_button_off, (324, 510))