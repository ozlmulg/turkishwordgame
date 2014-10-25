'''
Generic player object, can be inherited by Human or AI classes which
execute the actions of the player by either GUI interaction or algorithm
'''

import pygame, time
import board, tile, bag, aistats, heuristic
from pygame.locals import *

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
		Player.FONT = pygame.font.Font('freesansbold.ttf', 18)
		Player.initialized = True
		Player.aiStats = aistats.AIStats()	
	
	
	'''
	Initialize a new player with a tray and score
	'''
	def __init__(self, name, theBoard, theBag, theDifficulty = 10.0, theHeuristic = None):
		if not Player.initialized:
			Player.initialize()
		
		self.tray = []
		self.score = 0
		self.name = name
		self.theBoard = theBoard
		self.theBag = theBag
		self.lastScorePulse = 0
		self.lastScore = 0
		
		self.usageLimit = self.theBoard.dictionary.difficultyToUsage(theDifficulty)
		
		print str(theDifficulty)+", "+str(self.usageLimit)
		
		if theHeuristic == None:
			self.heuristic = heuristic.Heuristic()
		else:
			self.heuristic = theHeuristic
		
		#start with a full set of tiles
		self.grab()
			
		
	def drawTray(self, DISPLAYSURF):
		return None		
		
	'''
	Returns the value of the players tray in points
	'''
	def trayValue(self):
		value = 0
		for tile in self.tray:
			value += tile.points
		return value
		
