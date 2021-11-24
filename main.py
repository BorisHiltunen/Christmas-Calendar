import pygame

class ChristmasCalendar:
    def __init__(self):
        pygame.init()

        self.download_pictures()

        #self.opening_sound = pygame.mixer.Sound('opening_sound.wav')
        #self.locked_sound = pygame.mixer.Sound('locked_sound.wav')
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

        self.done = False

        #Making the mouse invisible by making it appear outside of the window
        self.x = 1000
        self.y = 1000
 
        self.display = pygame.display.set_mode((self.width, self.height))
 
        pygame.display.set_caption("ChristmasCalendar")
 
        self.loop()

    def download_pictures(self):

        self.background7 = pygame.image.load("background.png")
        self.lid1 = pygame.image.load("lid1.png")
        self.lid2 = pygame.image.load("lid2.png")
        self.lid1_open = pygame.image.load("lid1_open.png")
        self.lid2_open = pygame.image.load("lid2_open.png")
        self.lid1_hover_over = pygame.image.load("lid1_hover_over.png")
        self.lid2_hover_over = pygame.image.load("lid2_hover_over.png")
        self.lid1_open_hover_over = pygame.image.load("lid1_open_hover_over.png")
        self.lid2_open_hover_over = pygame.image.load("lid2_open_hover_over.png")
        self.mouse = pygame.image.load("mouse.png")

    def lids(self):

        self.first_lid_x = 300 >= self.x-self.lid1.get_width() and 300 <= self.x+self.lid1.get_width()
        self.first_lid_y = 150 >= self.y-self.lid1.get_height() and 150 <= self.y+self.lid1.get_height()

        if self.first_lid_x and self.first_lid_y:
            self.firstrow_1 = self.display.blit(self.lid1_open, (300, 150))
        else:
            self.firstrow_1 = self.display.blit(self.lid1, (300, 150))

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
                print("You pushed the button", event.button, "At the", event.pos)
 
            if event.type == pygame.MOUSEBUTTONUP:
                print("You stopped pushing the button", event.button, "At the", event.pos)
            if event.type == pygame.QUIT:
                exit()

    def draw_the_calendar(self):
 
        self.display.fill((0,100,100))

        self.display.blit(self.background7, (0, 0))

        self.lids()

        self.display.blit(self.mouse, (self.x, self.y))
 
        pygame.display.flip()

if __name__ == "__main__":
    ChristmasCalendar()