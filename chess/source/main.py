# Importing needed modules 
import pygame 
import sys

# Importing the baord's constants 
from constants import *

# Import needed classes 
from game import Game

# Main class for game 
class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('CHESS')
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen
        
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            for event in pygame.event.get(): 

                # This is the user clicking on a piece 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                #Allowing user to quit app if desired
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            



            pygame.display.update() #Last line of code in the main loop... to update screen 


# Creating an instance of the Main class and calling the main loop
main = Main()
main.mainloop()