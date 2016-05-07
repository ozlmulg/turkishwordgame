import pygame, time
import board, tile, bag
from pygame.locals import *
FONT = 'data/font/FreeSansBold.ttf'

class Player:
	
	PROGRESS_TOP = 220
	PROGRESS_LEFT = 570
	PROGRESS_WIDTH = 140
	PROGRESS_HEIGHT = 7
	PROGRESS_MARGIN = 25
	
	PROGRESS_COLOR_BACK = (200, 200, 255)
	PROGRESS_COLOR_FRONT = (100, 100, 255)
	
	FONT_COLOR = (55, 46, 40)
	BACKGROUND_COLOR = (255, 255, 255)
	

	TIMEOUT = 15	
	
	TRAY_SIZE = 7
	
	initialized = False
	
	@staticmethod
	def initialize():
		Player.FONT = pygame.font.Font(FONT, 18)
		Player.initialized = True
		#Player.aiStats = aistats.AIStats()	
	
	
	'''
	Initialize a new player with a tray and score
	'''
	def __init__(self, name, theBoard, theBag):
		if not Player.initialized:
			Player.initialize()
		
		self.tray = []  #table of player
		self.justTray = [] #holds the tiles of the player that are just on the tray not on table
		self.score = 0
		self.name = name
		self.theBoard = theBoard
		self.theBag = theBag
		self.lastScorePulse = 0
		self.lastScore = 0
		
		##start with a full set of tiles
		self.grab()
			
		
	def drawTray(self, SCREEN):
		return None		
		
	'''
	Returns the value of the players tray in points
	'''
	def trayValue(self):
		value = 0
		for tile in self.tray:
			value += tile.points
		return value
		
	'''
	Returns False if the player tries to draw new tiles and none exist in the bag (i.e. the
	game is finished), True if either tiles were successfully removed, or the tray isn't empty 
	'''	
	def grab(self):#take a tile from bag
		
		if not self.theBag.isEmpty() : #take tile with necessary
			#Attempt to withdraw the needed number of tiles
			numNeeded = Player.TRAY_SIZE-len(self.tray)
			for i in range(numNeeded):
				newTile = self.theBag.take()
				if newTile != None:
					self.tray.append(newTile) #add taken tile to player
					self.justTray.append(newTile) 
			
		#If the bag was empty AND our tray is empty, signal that play is over		
		elif len(self.tray) == 0:
			return False
		
		#elif self.theBag.isEmpty() :
			#return False
			
		return True		