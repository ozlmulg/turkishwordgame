# -*- coding: cp1254 -*-
import pygame, player, tile

class Human(player.Player): # extends Player
	
	TRAY_COLOR = (219,166,100)
	TRAY_BOTTOM_COLOR = (187, 121,63)
	TRAY_LEFT = 100
	TRAY_TOP = 550
	TRAY_FIRSTLEFT = TRAY_LEFT + tile.Tile.SQUARE_BORDER + tile.Tile.SQUARE_SIZE * .5
	TRAY_FIRSTTOP = TRAY_TOP + tile.Tile.SQUARE_BORDER
	FIRST_TIME = True
	ISCHANGE = "no"
	score = 0
	
	'''
	Initialize the human-controlled player (currently does nothing but call's player initialization)
	'''
	def __init__(self, name, theBoard, theBag):
		player.Player.__init__(self, name, theBoard, theBag)
		self.hand = -1
		
	'''
	Draws the tray at the bottom of the screen
	'''	
	def drawTray(self, SCREEN):
		
		#Draw a basic tray
		if self.ISCHANGE == "no":
			pygame.draw.rect(SCREEN, Human.TRAY_COLOR, (Human.TRAY_LEFT, Human.TRAY_TOP, 
				                        (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8, 
				                        tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER*2))
			
			pygame.draw.rect(SCREEN, Human.TRAY_BOTTOM_COLOR, (Human.TRAY_LEFT-5, Human.TRAY_TOP+37, 
				                        (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8+10,10))			
			
			for i in range(0,8):
				pygame.draw.rect(SCREEN, Human.TRAY_BOTTOM_COLOR, (Human.TRAY_LEFT+17+i*36, Human.TRAY_TOP+30,3,10))			
	
			#Draw each tile
			i = 0
			for t in self.tray:
				if self.FIRST_TIME == True:
					top = Human.TRAY_FIRSTTOP
					left = (Human.TRAY_FIRSTLEFT + (i * (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)))					
					t.setCoordinate((left,top))
				
				if i == self.hand:
					highlight = True
				else:
					highlight = False
				
				t.draw(highlight)	
				i += 1
				
			self.FIRST_TIME=False		
		
		
		elif self.ISCHANGE == "changing":
			
			
			pygame.draw.rect(SCREEN, Human.TRAY_COLOR, (Human.TRAY_LEFT, Human.TRAY_TOP, 
						                                (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8, 
						                                tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER*2))
						
			pygame.draw.rect(SCREEN, Human.TRAY_BOTTOM_COLOR, (Human.TRAY_LEFT-5, Human.TRAY_TOP+37, 
		                                        (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8+10,10))			
			
			for i in range(0,8):
				pygame.draw.rect(SCREEN, Human.TRAY_BOTTOM_COLOR, (Human.TRAY_LEFT+17+i*36, Human.TRAY_TOP+30,3,10))			


			#Draw each tile
			i = 0
			for t in self.tray:
				top = 250
				left = (Human.TRAY_FIRSTLEFT + (i * (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)))	+33
				t.setCoordinate((left,top))
			
				if i == self.hand:
					highlight = True
				else:
					highlight = False
				
				t.draw(highlight)	
				i += 1
			
		elif self.ISCHANGE == "finishchanging":
			#Draw each tile
			i = 0
			for t in self.tray:
				top = Human.TRAY_FIRSTTOP
				left = (Human.TRAY_FIRSTLEFT + (i * (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)))					
				t.setCoordinate((left,top))
				
				if i == self.hand:
					highlight = True
				else:
					highlight = False
				
				t.draw(highlight)	
				i += 1		
	
# #####################################
	def getTray(self):
		self.tray
# #####################################