# Needed modules 
import pygame
# Universal constants
from constants import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False 
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
    
    # This method is resposible for showing the piece dragging on the screen 
    def update_blit(self, surface):
        # Set texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # Load image 
        img = pygame.image.load(texture)
        # Set rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # Blit
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos #pos will be in the form of (Xpos, Ypos)

    # This method saves the initial position of a piece being dragged 
    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False 
    