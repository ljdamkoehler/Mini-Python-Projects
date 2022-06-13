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

        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    # This method moves the pices on the actual display
    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # Update console board with move
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # Update moved attribute on piece
        piece.moved = True

        # Clear valid moves 
        piece.clear_moves()

        # Save last move
        self.last_move = move

    # This method determines whether a move a player is trying to make is allowed 
    def valid_move(self, piece, move):
        # print('valid move')
        # print(move)
        # print(piece.moves)
        return move in piece.moves

    # This method will calculate all the valid moves for a given piece
    def calc_moves(self, piece, row, col):

        def pawn_moves():
            # Max pawn move 
            max_move = 1 if piece.moved else 2

            # vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1 + max_move))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].is_empty():
                        # Create initial and final squares for move
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # Create new move
                        move = Move(initial, final)
                        # Append the new move
                        piece.add_move(move)
                    # This breaks the loop if the pawn is blocked by another piece 
                    else: break
                # Break loop if not in range
                else: break

            # diagnol moves 
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        # Create initial and final squares for move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move
                        move = Move(initial, final)
                        # Apepnd the new move
                        piece.add_move(move)
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
        
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        # Empty square... continue checking
                        if self.squares[possible_move_row][possible_move_col].is_empty():
                            # append a new move
                            piece.add_move(move)
                        
                        # Square has enemy piece 
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            # append a new move
                            piece.add_move(move)
                            break
                        # Add increment each pass through the while loop

                        # Square has a non-rival piece 
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    # Break while loop if not in range
                    else:
                        break
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col  + col_incr

        def king_moves():
            adjs = [
                (row+1, col), # down
                (row-1, col), # up
                (row, col+1), # right
                (row, col-1), # left
                (row-1, col+1), # up and right
                (row-1, col-1), # up and left
                (row+1, col+1), # down and right
                (row+1, col-1) # down and left
            ]
            # Regular moves
            for adj in adjs:
                possible_move_row, possible_move_col = adj

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

            # Caslting moves

            # King-side castle

            # Queen-side castle

        # Check which piece is being moved
        if isinstance(piece, Pawn): 
            pawn_moves()

        elif isinstance(piece, Knight): 
            knight_moves()

        elif isinstance(piece, Bishop): 
            straightline_moves([
                (-1, 1), #up and to right
                (1, 1), # down and to right
                (-1, -1), # up and to left
                (1, -1) # down and to left
            ])

        elif isinstance(piece, Rook): 
            straightline_moves([
                (0, 1), #right
                (0, -1), #left
                (-1, 0), #up 
                (1, 0) #down
            ])

        elif isinstance(piece, Queen): 
            straightline_moves([
                (-1, 1), #up and to right
                (1, 1), # down and to right
                (-1, -1), # up and to left
                (1, -1), # down and to left
                (0, 1), #right
                (0, -1), #left
                (-1, 0), #up 
                (1, 0) #down
            ])

        elif isinstance(piece, King): 
            king_moves()

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
