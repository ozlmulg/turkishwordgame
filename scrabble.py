import pygame,sys
from pygame.locals import *
import board,bag,menu
global SCREEN

def main():
    pygame.init() #start pygame 
    getScreen()
    pygame.display.set_caption("SCRABBLE GAME") #name of the window
    
    tilebag = bag.Bag()
    gameboard = board.Board()
    gamemenu = menu.GameMenu()
    while True: #show screen until not close
	for event in pygame.event.get(): #get event from pygame
	    if event.type == pygame.QUIT: #if user click close button
		pygame.quit()#finish pygame
		sys.exit()
	gameboard.draw()
	
	pygame.display.update()

def getScreen():
    size = (800,700) #size of the screen   
    SCREEN = pygame.display.set_mode(size) # show screen 
    return SCREEN


if __name__ == '__main__': # if the screen module is firstly run then call the main of menu.
	menu.main()