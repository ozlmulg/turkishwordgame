import pygame,sys
from pygame.locals import *
import scrabble,tile
FONT = 'data/font/FreeSansBold.ttf'
class Board:
	#board square
	SQUARE_SIZE = 32
	SQUARE_BORDER = 4
	GRID_SIZE = 15
	BOARD_TOP = 0
	BOARD_LEFT = 0	

	#bonus types!
	NORMAL = 'normal'
	DOUBLEWORD = 'doubleword'
	TRIPLEWORD = 'tripleword'
	DOUBLELETTER = 'doubleletter'
	TRIPLELETTER = 'tripleletter'
		
        #colors of the squares
	BOARD_BACKGROUND = (223, 236, 255)
	RED = (217, 28, 32)
	BLUE = (80,148,216)
	PINK = (206, 78, 33)
	LBLUE = (114, 180, 80)
	
		
	def __init__(self):
		#get SCREEN of the scrabble module
		self.SCREEN = scrabble.getScreen()		
		self.squares = []
		for x in range(Board.GRID_SIZE):
			self.squares.append([]) # adding each row to the board
			for y in range(Board.GRID_SIZE):
				#place all squares as normal
				self.squares[x].append((None, Board.NORMAL))  #filling each element in this rows
		
		#------------BONUS SQUARES------------------		
		triplewords = [(0,0), (7,0), (14,0), (0,7), (14,7), (0,14), (7,14), (14,14)]	
		for (x, y) in triplewords:
			self.squares[x][y] = (None, Board.TRIPLEWORD)
		
		doublewords = [(1,1), (2,2), (3,3), (4,4), (1,13), (2,12), (3,11), (4,10),
		                (13,1), (12,2), (11,3), (10,4), (13,13), (12,12), (11,11), (10,10)]
		for (x, y) in doublewords:
			self.squares[x][y] = (None, Board.DOUBLEWORD)
			
		tripleletters = [(5,1), (9,1), (1,5), (1,9), (5,13), (9,13), (13,5), (13,9), (5,5), (9,9), (5,9), (9,5)]
		for (x, y) in tripleletters:
			self.squares[x][y] = (None, Board.TRIPLELETTER)
		
		doubleletters = [(3,0), (0,3), (11,0), (0,11), (3,14), (11,14), (14,3), (14,11),
		                (2,6), (3,7), (2,8), (6,2), (7,3), (8,2), (6,12), (7,11), (8,12),
		                 (12,6), (11,7), (12,8), (6,6), (8,8), (6,8), (8,6)]
		for (x, y) in doubleletters:
			self.squares[x][y] = (None, Board.DOUBLELETTER)
			
			
	def draw(self):
		
		#draw each square
		for x in range(Board.GRID_SIZE):
			for y in range(Board.GRID_SIZE):
				#draw position
				xCorner = x * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_LEFT
				yCorner = y * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_TOP
					
				(tile, bonus) = self.squares[x][y]
				if(bonus == Board.NORMAL):
					color = Board.BOARD_BACKGROUND
					text = ' '
				elif(bonus == Board.DOUBLEWORD):
					color = Board.PINK
					if x == 7 and y == 7:
						text = '*'
					else:
						text = '2xK'
				elif(bonus == Board.TRIPLEWORD):
					color = Board.RED
					text = '3xK'
				elif(bonus == Board.DOUBLELETTER):
					color = Board.LBLUE
					text = '2xH'
				elif(bonus == Board.TRIPLELETTER):
					color = Board.BLUE
					text = '3xH'
				else:
					assert(False)
					
				pygame.draw.rect(self.SCREEN, color, (xCorner, yCorner, Board.SQUARE_SIZE, Board.SQUARE_SIZE))				
				self.SCREEN.blit(pygame.font.Font(FONT, 12).render(text, True, (255,255,255)), (xCorner+4, yCorner+6))	
				