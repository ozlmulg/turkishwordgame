# -*- coding: utf-8 -*-
import pygame, random
import tile
#SEED = 448
class Bag:
	
	def __init__(self):
		self.tiles = []
		#self.TurkishCharList = []
		
		#tiles
		self.add('A', 1, 12)
		self.add('B', 3, 2)
		self.add('C', 4, 2)
		self.add(u'Ç', 4, 2)		
		self.add('D', 3, 2)
		self.add('E', 1, 8)
		self.add('F', 7, 1)
		self.add('G', 5, 1)
		self.add(u'Ğ', 8, 1)
		self.add('H', 5, 1)
		self.add(u'ı', 2, 4)
		self.add(u'İ', 1, 7)
		self.add('J', 10, 1)
		self.add('K', 1, 7)
		self.add('L', 1, 7)
		self.add('M', 2, 4)
		self.add('N', 1, 5)
		self.add('O', 2, 3)
		self.add(u'Ö', 7, 1)
		self.add('P', 5, 1)
		self.add('R', 1, 6)
		self.add('S', 2, 3)
		self.add(u'Ş', 4, 2)
		self.add('T', 1, 5)
		self.add('U', 2, 3)
		self.add(u'Ü', 3, 2)
		self.add('V', 7, 1)
		self.add('Y', 3, 2)
		self.add('Z', 4, 2)
		#self.add('*', 0, 2);  #-->>JOKER TILE
		
		self.shuffle()
		
	def take(self):
		if self.isEmpty():
			return None
		else:
			tile = self.tiles[0]
			self.tiles = self.tiles[1:]
			return tile
			
	def isEmpty(self):
		if len(self.tiles) == 0:
			return True
		return False
		
	def shuffle(self):
		#random.seed(SEED)
		random.shuffle(self.tiles)
		
	def putBack(self, tile):
		self.tiles.append(tile)
			
	def add(self, letter, points, n):# n = number of letter in bag
		for i in range(n):
			self.tiles.append(tile.Tile(letter, points ,(None,None)))
		#self.TurkishCharList.append(unicode(letter.lower()))
		