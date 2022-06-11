# Import universal constants
from constants import *

# Import other needed classes 
from square import Square
from piece import *
from move import Move 

# This is the class that will represent the whole board and will have a ref to each individual square
class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    # This method will calculate all the valid moves for a given piece
    def calc_moves(self, piece, row, col):

        def knight_moves():
            # There are 8 possible moves for a knight
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                        # create squares for the move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # add piece here later 
                        # craete a new move
                        move = Move(initial, final)
                        # Append a new valid move
                        piece.add_move(move)
        
        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            pass

        elif isinstance(piece, Rook):
            pass

        elif isinstance(piece, Queen):
            pass

        elif isinstance(piece, King):
            pass

    # This method creates a board full of squares 
    def _create(self): #private method (only called inside Board class)
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    
    # This method adds the pieces to the squares 
    def _add_pieces(self, color): #private method (only called inside Board class)
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # This creates all pawns 
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # This creates all the knights 
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        # Test knight
        # self.squares[3][5] = Square(3, 5, Knight(color))

        # This creates all the bishops 
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # This creates the rooks 
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # This creates the queens 
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # This creates the kings
        self.squares[row_other][4] = Square(row_other, 4, King(color))
