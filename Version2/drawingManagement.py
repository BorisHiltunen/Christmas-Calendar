import pygame

#Funktion that basically draws the calendar
def draw_the_calendar(self):

    self.display.fill((0,100,100))

    self.display.blit(self.background, (0, 0))

    self.sound_management()

    self.lids()

    self.display.blit(self.mouse, (self.x, self.y))

    pygame.display.flip()