# Importing needed modules 
import pygame 
import sys

# Importing the baord's constants 
from constants import *

# Import needed classes 
from game import Game
from square import Square
from move import Move

# Main class for game 
class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('CHESS')
        self.game = Game()

    def mainloop(self):

        game = self.game
        board = self.game.board
        screen = self.screen
        dragger = self.game.dragger
        
        while True:

            # These are the show methods
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get(): 

                # This is the user clicking on a piece 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # This checks to see if the clicked square has a piece 
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                        # These are the show methods 
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                    
                # User moving piece 
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        # These are the show mwthods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # User releasig piece on a new square
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move and check to see if it is valid

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)

                        move = Move(initial, final)
                        
                        # print(board.valid_move(dragger.piece, move))
                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)
                            # Show methods 
                            game.show_bg(screen)
                            game.show_pieces(screen)

                    dragger.undrag_piece()



                #Allowing user to quit app if desired
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            



            pygame.display.update() #Last line of code in the main loop... to update screen 


# Creating an instance of the Main class and calling the main loop
main = Main()
main.mainloop()