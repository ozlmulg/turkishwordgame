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
	#SCREEN.fill((0,0,0)) # clear screen
	SCREEN.blit(asurf, imagerect)
	
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
		MousePressed = True 
		MouseDown = True 
			   
	    if event.type == pygame.MOUSEBUTTONUP:
		MouseReleased = True
		MouseDown = False	 
		
	    if MousePressed == True:
		for item in players[active].tray: # search all items
		    if (pos[0] >= (item.coordinate[0]) and # ######## Changed
		        pos[0] <= (item.coordinate[0] + item.SQUARE_SIZE) and 
		        pos[1] >= (item.coordinate[1]) and # ######## Changed
		        pos[1] <= (item.coordinate[1] + item.SQUARE_SIZE) ): # inside the bounding box
			Target=item # "pick up" item
			break
		
		
		#if Target is None: # didn't find any?
		    #Target=Disk((0,0,255),coordinate,32) # create a new one
		    #RenderList.append(Target) # add to list of things to draw
		
	    if MouseDown and Target is not None: # if we are dragging something
		Target.coordinate = (pos[0] - tile.Tile.SQUARE_SIZE/2, pos[1] - tile.Tile.SQUARE_SIZE/2) # move the target with us ############Holds the tile from the middle
	    
	    if MouseReleased:
		# ##############################
		if (Target.coordinate[0]%36-5) <= tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) <= tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] - (Target.coordinate[0] % 36)) + 5, (Target.coordinate[1] - (Target.coordinate[1] % 36)) + 5)
		elif(Target.coordinate[0]%36-5) > tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) <= tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] + (36-Target.coordinate[0]%36)) + 5, (Target.coordinate[1] - (Target.coordinate[1] % 36)) + 5)
		elif(Target.coordinate[0]%36-5) <= tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) > tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] - (Target.coordinate[0] % 36)) + 5, (Target.coordinate[1] + (36-Target.coordinate[1]%36)) + 5)
		elif(Target.coordinate[0]%36-5) > tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) > tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] + (36-Target.coordinate[0]%36)) + 5, (Target.coordinate[1] + (36-Target.coordinate[1]%36)) + 5)
		# ##############################
				    
		Target = None # Drop item, if we have any
		
		
		
	    MousePressed = False # Reset these to False
	    MouseReleased = False # Ditto

# ###############
	#gameboard.draw()
	players[active].drawTray(SCREEN)#draw tiles of the player ## SILINECEK NOT: BU KOD SATIRININ YERI ONEMLI   
# #############
        pygame.display.update()    


# ####################################DRAW#############################################
def draw():
    tilebag = bag.Bag() #create a bag of tiles
# ############
    global gameboard
    gameboard = board.Board()#crate game board
# ###########


    gamemenu = menu.GameMenu()#create game menu
    global asurf
    global imagerect
    asurf = pygame.image.load('Board.jpg')
    imagerect = asurf.get_rect()
    SCREEN.fill((0,0,0))
    SCREEN.blit(asurf, imagerect)
   	
    # ######## tile trial #######
    global players
    players = []
    global active
    active = 0 # MIGHT 0 represents the first player	    
    players.append(human.Human("Player", gameboard, tilebag))
    
    # ########### tile trial end  ################
    
    gameboard.draw() #draw game board
    players[active].drawTray(SCREEN)#draw tiles of the player
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

	
