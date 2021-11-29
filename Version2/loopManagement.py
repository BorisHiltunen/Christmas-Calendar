import pygame

#Funktion that loops over and over
#Thus making the use of the calendar feel comfortable
def loop(self):
    clock = pygame.time.Clock()

    while True:
        self.draw_the_calendar()
        self.analyse_events()
        clock.tick(60)