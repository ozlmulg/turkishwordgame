import pygame,sys
from pygame.locals import *
import board,bag,menu
import Buttons

global SCREEN

'''
def main():
    pygame.init() #start pygame 
    getScreen()
    pygame.display.set_caption("SCRABBLE GAME") #name of the window
    
    tilebag = bag.Bag()
    gameboard = board.Board()
	
    while True: #show SCREEN until not close
	for event in pygame.event.get(): #get event from pygame
	    if event.type == pygame.QUIT: #if user click close button
		pygame.quit()#finish pygame
		sys.exit()
	    elif event.type == MOUSEBUTTONDOWN:
		if playButton.pressed(pygame.mouse.get_pos()):
		    print "Play pressed!"
		if shuffleButton.pressed(pygame.mouse.get_pos()):
			print "Shuffle pressed!"
			
	gamemenu = GameMenu(gameboard)
	#draw game board and game menu		
	#gameboard.draw()
	pygame.display.update()

def getScreen():
    size = (800,700) #size of the SCREEN   
    SCREEN = pygame.display.set_mode(size) # show SCREEN 
    return SCREEN

def GameMenu(gameboard): 
    #getScreen().fill((0,0,0))
    
    global playButton
    playButton = Buttons.Button()
    #Parameters:               surface,      color,  x,   y,   length, height, width,    text,      text_color
    playButton.create_button(getScreen(), (107,142,35), 585, 390, 100,    40,    100,        "Play", (255,255,255))
   # pygame.display.update()   
    
    global shuffleButton
    shuffleButton = Buttons.Button()
    #Parameters:               surface,      color,  x,   y,   length, height, width,    text,      text_color
    shuffleButton.create_button(getScreen(), (107,142,35), 585, 510, 100,    40,    100,        "Shuffle", (255,255,255))
    #pygame.display.update() 
    gameboard.draw()
    
if __name__ == '__main__': # if the SCREEN module is firstly run then call the main of menu.
	menu.main()
	
'''	
	
	
#Initialize pygame
pygame.init()

class Scrabble:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        size = (800,700) #size of the SCREEN   
        self.SCREEN = pygame.display.set_mode(size) # show SCREEN 
        pygame.display.set_caption("SCRABBLE GAME") #name of the window

    #Update the display and show the button
    def update_display(self):
        self.SCREEN.fill((0,0,0))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.SCREEN, (107,142,35), 600, 335, 100,    50,    0,        "Play", (255,255,255))
        self.Button2.create_button(self.SCREEN, (107,142,35), 600, 255, 100,    50,    0,        "Shuffle", (255,255,255))
	self.Button3.create_button(self.SCREEN, (107,142,35), 600, 155, 100,    50,    0,        "Back", (255,255,255))
        #pygame.display.flip()


    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
	self.Button3 = Buttons.Button()
        self.display()
        
        tilebag = bag.Bag()
        gameboard = board.Board()        

        while True:
         
	                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print "Give me a command!"
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                                            print "Give me a command 2!"                        
	    gameboard.draw()
	    pygame.display.update() 
	    self.update_display()
	    #pygame.display.update()           


def getScreen():
    size = (800,700) #size of the SCREEN   
    SCREEN = pygame.display.set_mode(size) # show SCREEN 
    return SCREEN


if __name__ == '__main__':
    scrabble = Scrabble()

	
