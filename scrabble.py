import pygame,sys
from pygame.locals import *
import board,bag,menu

#Run the game
def main():
  
    display() #display screen!
    
    tilebag = bag.Bag() #create a bag of tiles
    gameboard = board.Board()#crate game board        

    while True: #show SCREEN until not close
	for event in pygame.event.get(): #get event from pygame
	    if event.type == pygame.QUIT: #if user click close button
		pygame.quit()#finish pygame
		sys.exit()#close window
	    elif event.type == MOUSEBUTTONDOWN:
		if menu.playButton.pressed(pygame.mouse.get_pos()):
		    print "Play pressed!"
		if menu.shuffleButton.pressed(pygame.mouse.get_pos()):
		    print "Shuffle pressed!"
		if menu.exitButton.pressed(pygame.mouse.get_pos()):
		    print "Exit pressed!"		
	    
	#draw game board	
	gameboard.draw()
	pygame.display.update() 
	#draw game menu
	gamemenu = menu.GameMenu()
	gamemenu.createButtons()

#retun global SCREEN
def getScreen():
    return SCREEN

#Create a display
def display():
    #Initialize pygame
    pygame.init()    
    global SCREEN #create a global Screen
    size = (800,700) #size of the SCREEN   
    SCREEN = pygame.display.set_mode(size) # show SCREEN     
    pygame.display.set_caption("SCRABBLE GAME") #name of the window

#initially create main menu
if __name__ == '__main__': # if the SCREEN module is firstly run then call the main of menu.
    menu.main()

	
