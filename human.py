# -*- coding: cp1254 -*-
'''
This class extends the basic player class to implement actions using the GUI
so that a human-controlled player can make moves
'''

import pygame, player, tile

class Human(player.Player):
	
	TRAY_COLOR = (110, 92, 80)
	TRAY_LEFT = 100
	TRAY_TOP = 550
	TRAY_FIRSTLEFT = TRAY_LEFT + tile.Tile.SQUARE_BORDER + tile.Tile.SQUARE_SIZE * .5
	TRAY_FIRSTTOP = TRAY_TOP + tile.Tile.SQUARE_BORDER
	
	'''
	Initialize the human-controlled player (currently does nothing but call's player initialization)
	'''
	def __init__(self, name, theBoard, theBag, theHeuristic = None):
		player.Player.__init__(self, name, theBoard, theBag, 10.0, theHeuristic)
		self.hand = -1
	

		
	'''
	Draws the tray at the bottom of the screen
	'''	
	def drawTray(self, SCREEN):
		
		#Draw a basic tray
		pygame.draw.rect(SCREEN, Human.TRAY_COLOR, (Human.TRAY_LEFT, Human.TRAY_TOP, 
						(tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8, 
						tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER*2))
			
		#Draw each tile
		i = 0
		for t in self.tray:
			top = Human.TRAY_FIRSTTOP
			left = (Human.TRAY_FIRSTLEFT + (i * (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)))
			
			if i == self.hand:
				highlight = True
			else:
				highlight = False
			
			t.setCoordinate((left,top))
			t.draw(left, top, highlight)	
			i += 1

# #####################################
	def getTray(self):
		self.tray
# #####################################