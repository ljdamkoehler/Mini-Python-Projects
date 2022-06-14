# Needed modules 
import pygame

# This is the square class that will be used for each of thr 64 squares on the chess board
class Square:

    ALPHA_COLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece 
        self.alpha_col = self.ALPHA_COLS[col]

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece != None

    def is_empty(self):
        return not self.has_piece()


    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    # This method returns true if a square has a rival piece 
    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color

    # This method returns true if a given square is empty or has a rival piece 
    def is_empty_or_rival(self, color):
        return self.is_empty() or self.has_rival_piece(color)
        
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False 
        return True

    @staticmethod
    def get_alpha_col(col):
        ALPHA_COLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHA_COLS[col]