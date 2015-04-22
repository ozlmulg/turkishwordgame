'''
This class creates a player which automatically plays (NOTE: the meat of this class
is actually located in the superclass, Player. This was moved so that human players
can get "hints")
'''
import pygame, player, tile
from pygame.locals import *

class AI(player.Player):
	
	TRAY_COLOR = (219,166,100)
	TRAY_BOTTOM_COLOR = (187, 121,63)
	TRAY_LEFT = 100
	TRAY_TOP = 550
	TRAY_FIRSTLEFT = TRAY_LEFT + tile.Tile.SQUARE_BORDER + tile.Tile.SQUARE_SIZE * .5
	TRAY_FIRSTTOP = TRAY_TOP + tile.Tile.SQUARE_BORDER + 50
	FIRST_TIME = True
	score = 0
	
	'''
	Initializes the AI
	'''
	def __init__(self, name, theBoard, theBag, theDifficulty = 10, theHeuristic = None):
		player.Player.__init__(self, name, theBoard, theBag, theDifficulty, theHeuristic)
	        self.hand = -1
	'''
	Draws the tray at the bottom of the screen
	'''	
	def drawTray(self, SCREEN):
		
		#Draw a basic tray
		pygame.draw.rect(SCREEN, AI.TRAY_COLOR, (AI.TRAY_LEFT, AI.TRAY_TOP, 
						(tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8, 
						tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER*2))
			
		pygame.draw.rect(SCREEN, AI.TRAY_BOTTOM_COLOR, (AI.TRAY_LEFT-5, AI.TRAY_TOP+37, 
		                                (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8+10,10))			
		
		#Draw each tile
		i = 0
		for t in self.tray:
			if self.FIRST_TIME == True:
				top = AI.TRAY_FIRSTTOP
				left = (AI.TRAY_FIRSTLEFT + (i * (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)))
				t.setCoordinate((left,top))
			
			if i == self.hand:
				highlight = True
			else:
				highlight = False
			
			t.draw(highlight)
			i += 1
			
		self.FIRST_TIME=False

# #####################################
	def getTray(self):
		self.tray
# #####################################		