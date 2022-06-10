# Needed modules 
import pygame

# This is the square class that will be used for each of thr 64 squares on the chess board
class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece 

    def has_piece(self):
        return self.piece != None
        
