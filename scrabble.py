import pygame,sys
from pygame.locals import *
import board,bag,menu,human,tile

#Run the game
def main():
  
    display() #display screen!
    draw()#draw game board,game menu and player tiles
# #############################################################
    RenderList=[] # list of objects
    MousePressed=False # Pressed down THIS FRAME
    MouseDown=False # mouse is held down
    MouseReleased=False # Released THIS FRAME
    Target=None # target of Drag/Drop    
# ################################################################

    while True: #show SCREEN until not close
	SCREEN.fill((0,0,0)) # clear screen
	pos=pygame.mouse.get_pos()
	
	for event in pygame.event.get(): #get event from pygame
	    if event.type == pygame.QUIT: #if user click close button
		pygame.quit()#finish pygame
		sys.exit()#close window
		
	    if event.type == MOUSEBUTTONDOWN:
		if menu.playButton.pressed(pygame.mouse.get_pos()):
		    print "Play pressed!"
		if menu.changeButton.pressed(pygame.mouse.get_pos()):
		    print "Shuffle pressed!"
		if menu.backButton.pressed(pygame.mouse.get_pos()):
		    print "Back pressed!"
		    
	    if event.type == pygame.MOUSEBUTTONDOWN:
		MousePressed=True 
		MouseDown=True 
			   
	    if event.type == pygame.MOUSEBUTTONUP:
		MouseReleased=True
		MouseDown=False	 
		
	    if MousePressed==True:
		for item in players[active].getTray(): # search all items
		    if (pos[0]>=(item.coordinate[0]-item.SQUARE_SIZE) and 
		        pos[0]<=(item.coordinate[0]+item.SQUARE_SIZE) and 
		        pos[1]>=(item.coordinate[1]-item.SQUARE_SIZE) and 
		        pos[1]<=(item.coordinate[1]+item.SQUARE_SIZE) ): # inside the bounding box
			Target=item # "pick up" item
		
		
		#if Target is None: # didn't find any?
		    #Target=Disk((0,0,255),coordinate,32) # create a new one
		    #RenderList.append(Target) # add to list of things to draw
		
	    if MouseDown and Target is not None: # if we are dragging something
		Target.coordinate=coordinate # move the target with us
	    
	    if MouseReleased:
		Target=None # Drop item, if we have any
		
	    players[active].drawTray(SCREEN)#draw tiles of the player
		
	    MousePressed=False # Reset these to False
	    MouseReleased=False # Ditto 	    
        pygame.display.update()    


# ####################################DRAW#############################################
def draw():
    tilebag = bag.Bag() #create a bag of tiles
    gameboard = board.Board()#crate game board        
    gamemenu = menu.GameMenu()#create game menu
   	
    # ######## tile trial #######
    global players
    players = []
    global active
    active = 0 # MIGHT 0 represents the first player	    
    players.append(human.Human("Player", gameboard, tilebag))
    
    # ########### tile trial end  ################
    
    gameboard.draw() #draw game board
    #players[active].drawTray(SCREEN)#draw tiles of the player
    gamemenu.createButtons() #draw game menu	

# ####################################DRAW#############################################
 
    
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
    pygame.display.set_caption("SCRABBLE") #name of the window


#initially create main menu
if __name__ == '__main__': # if the SCREEN module is firstly run then call the main of menu.
    menu.main()

	
