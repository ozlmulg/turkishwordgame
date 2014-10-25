import pygame,scrabble

class Tile:
    
    SQUARE_SIZE = 32
    SQUARE_BORDER = 4   
    TILE_OUTLINE = (55, 46, 40)
    TILE_HIGHLIGHT = (100, 100, 255) 
 

    def __init__(self, letter, points):
	    self.letter = letter
	    self.points = points
	    
    def draw(self, left, top, highlight = False):
	    SCREEN = scrabble.getScreen()
	    LETTER_FONT = pygame.font.Font('freesansbold.ttf', 24)
	    POINTS_FONT = pygame.font.Font('freesansbold.ttf', 7)   	    
	    if highlight:
		    pygame.draw.rect(SCREEN, None , (left, top, Tile.SQUARE_SIZE, Tile.SQUARE_SIZE))
	    else:
		    pygame.draw.rect(SCREEN, None , (left+1, top+1, Tile.SQUARE_SIZE-2, Tile.SQUARE_SIZE-2))
		    
	    backColor = (0,0,0)
	    pygame.draw.rect(SCREEN, backColor, (left+2, top+2, Tile.SQUARE_SIZE-4, Tile.SQUARE_SIZE-4))
	    
	    #Display the letter of the tile
	    letterText = LETTER_FONT.render(self.letter, True, Tile.TILE_OUTLINE, backColor)
	    letterRect = letterText.get_rect()
	    letterRect.center = (left + Tile.SQUARE_SIZE/2 - 3, top + Tile.SQUARE_SIZE/2)
	    SCREEN.blit(letterText, letterRect)
    
	    #Display the points of the tile
	    pointsText = POINTS_FONT.render(str(self.points), True, Tile.TILE_OUTLINE, backColor)
	    pointsRect = pointsText.get_rect()
	    pointsRect.center = (left + Tile.SQUARE_SIZE/2 + Tile.SQUARE_SIZE/3, top + Tile.SQUARE_SIZE/2 + Tile.SQUARE_SIZE/3)
	    SCREEN.blit(pointsText, pointsRect)	