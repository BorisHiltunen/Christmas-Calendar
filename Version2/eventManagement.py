import pygame

#Funktion that is responsible for making the game's mouse work as intended
def analyse_events(self):

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            self.x = event.pos[0]-self.mouse.get_width()/2
            self.y = event.pos[1]-self.mouse.get_height()/2

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.buttonDown = True
            print("You pushed the button", event.button, "At the", event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            self.buttonDown = False
            print("You stopped pushing the button", event.button, "At the", event.pos)
        if event.type == pygame.QUIT:
            exit()