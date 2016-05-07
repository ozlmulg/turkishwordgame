import pygame, player, tile ,scrabble
from pygame.locals import *

class AI(player.Player):
	
	TRAY_COLOR = (219,166,100)
	TRAY_BOTTOM_COLOR = (187, 121,63)
	TRAY_LEFT = 100
	TRAY_TOP = 550
	TRAY_FIRSTLEFT = TRAY_LEFT + tile.Tile.SQUARE_BORDER + tile.Tile.SQUARE_SIZE * .5
	TRAY_FIRSTTOP = TRAY_TOP + tile.Tile.SQUARE_BORDER
	FIRST_TIME = True
	score = 0
	IS_DEMO = False
	
	'''
	Initializes the AI
	'''
	def __init__(self, name, theBoard, theBag):
		player.Player.__init__(self, name, theBoard, theBag)
	        self.hand = -1
		self.players = scrabble.getPlayers()
		
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
		
		for i in range(0,8):
			pygame.draw.rect(SCREEN, AI.TRAY_BOTTOM_COLOR, (AI.TRAY_LEFT+17+i*36, AI.TRAY_TOP+30,3,10))			

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
		
		if not self.IS_DEMO:
		    #Draw each tile
			#for t in self.players[0].tray:
				#t.draw(False) 
			self.players[0].drawTray(SCREEN)
				
# #####################################
	def getTray(self):
		self.tray
# #####################################		