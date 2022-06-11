# Needed modules 
import pygame

# Import universal constants 
from constants import *

# Import needed classes 
from board import Board
from dragger import Dragger
from square import Square

# This is the class that defines a chess game in our app

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # Show methods below here

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #Light green on evens 
                else:
                    color = (119, 154, 88) #Dark green on odds
                
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # First check to see if there is a piece on the square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # Blit all pieces except dragger piece 
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
   
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            # Looping through all valid moves for the piece being dragged 
            for move in piece.moves:
                # create color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # create a rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

        
