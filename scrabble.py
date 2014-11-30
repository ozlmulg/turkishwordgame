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
    #global tilem
    #tilem = None
# #####################
    playedTiles = []
# #####################
    Target=None # target of Drag/Drop 
    # ##############save initial image
    global asurf
    asurf = pygame.image.load('Board.jpg')   
    # ##############
    # ###############
    while True: #show SCREEN until not close
	
	#SCREEN.blit(asurf, imagerect)
	# #####################################
	SCREEN.fill((0,0,0)) # clear screen
	SCREEN.blit(asurf.convert_alpha(),[0,0])
	gamemenu.createButtons() #draw game menu
	# ####################################
	
	pos=pygame.mouse.get_pos()

	
	for event in pygame.event.get(): #get event from pygame
	    if event.type == pygame.QUIT: #if user click close button
		pygame.quit()#finish pygame
		sys.exit()#close window
		
	    if event.type == MOUSEBUTTONDOWN:
		if menu.playButton.pressed(pygame.mouse.get_pos()):
		    print "Play pressed!"
		    # #################save image when it placed#########
		    players[active].drawTray(SCREEN)
		    for Target in playedTiles:
			players[active].tray.remove(Target)		    
		    playedTiles = []
		    rect = pygame.Rect(0, 0, 545, 545)
		    sub = SCREEN.subsurface(rect)
		    pygame.image.save(sub, "Board.png")
		    asurf = pygame.image.load('Board.png')
		    #  ##############################################	    
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
			Target.oldPos = Target.coordinate[:]
			# ##############################################SWAP##############
			indexofTarget = players[active].tray.index(Target)
			temp = players[active].tray[-1] #last element of tray
			players[active].tray[indexofTarget] = temp
			players[active].tray[-1] = Target# now last element is Target
			# ####################################################
			break
	        '''
		for item in playedTiles: # search all items
		    if (pos[0] >= (item.coordinate[0]) and # ######## Changed
		        pos[0] <= (item.coordinate[0] + item.SQUARE_SIZE) and 
		        pos[1] >= (item.coordinate[1]) and # ######## Changed
		        pos[1] <= (item.coordinate[1] + item.SQUARE_SIZE) ): # inside the bounding box
			Target=item # "pick up" item
			break		
		'''
		
		#if Target is None: # didn't find any?
		    #Target=Disk((0,0,255),coordinate,32) # create a new one
		    #RenderList.append(Target) # add to list of things to draw
		
	    if MouseDown and Target is not None: # if we are dragging something
		Target.coordinate = (pos[0] - tile.Tile.SQUARE_SIZE/2, pos[1] - tile.Tile.SQUARE_SIZE/2) # move the target with us ############Holds the tile from the middle
	    
	    if MouseReleased and Target is not None:
		# ##############################
		if Target.coordinate[0] >= board.Board.GRID_SIZE * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER) + 1 or Target.coordinate[1] >= board.Board.GRID_SIZE * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER) + 1:
				    Target.coordinate = Target.oldPos		
		elif (Target.coordinate[0]%36-5) <= tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) <= tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] - (Target.coordinate[0] % 36)) + 5, (Target.coordinate[1] - (Target.coordinate[1] % 36)) + 5)
		    # ###############will remove from tray when played#############3
		    if(Target not in playedTiles):
			playedTiles.append(Target)
		    # ######################################################
		elif(Target.coordinate[0]%36-5) > tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) <= tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] + (36-Target.coordinate[0]%36)) + 5, (Target.coordinate[1] - (Target.coordinate[1] % 36)) + 5)
		    if(Target not in playedTiles):
		        playedTiles.append(Target)
		elif(Target.coordinate[0]%36-5) <= tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) > tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] - (Target.coordinate[0] % 36)) + 5, (Target.coordinate[1] + (36-Target.coordinate[1]%36)) + 5)
		    if(Target not in playedTiles):
		        playedTiles.append(Target)
		elif(Target.coordinate[0]%36-5) > tile.Tile.SQUARE_SIZE/2 and (Target.coordinate[1]%36-5) > tile.Tile.SQUARE_SIZE/2:
		    Target.coordinate = ((Target.coordinate[0] + (36-Target.coordinate[0]%36)) + 5, (Target.coordinate[1] + (36-Target.coordinate[1]%36)) + 5)
		    if(Target not in playedTiles):
		        playedTiles.append(Target)
		# ##############################
		# ############
		
		#if(Target in players[active].tray):
		    #players[active].tray.remove(Target)
		    #playedTiles.append(Target)

		# ############
		#Target.draw(False)
		#tilem = Target
		Target = None # Drop item, if we have any
		
		
	    MousePressed = False # Reset these to False
	    MouseReleased = False # Ditto

# ###############
	#gameboard.draw()
	players[active].drawTray(SCREEN)#draw tiles of the player ## SILINECEK NOT: BU KOD SATIRININ YERI ONEMLI 
	
	'''
	for item in playedTiles:
	    item.draw(False)
	'''
# #############
        pygame.display.update()    


# ####################################DRAW#############################################
def draw():
    tilebag = bag.Bag() #create a bag of tiles
# ############
    global gameboard
    gameboard = board.Board()#crate game board
# ###########

    global gamemenu
    gamemenu = menu.GameMenu()#create game menu
    #global asurf
    #global imagerect
    #asurf = pygame.image.load('Board.jpg')
    #imagerect = asurf.get_rect()
    SCREEN.fill((0,0,0))
    #SCREEN.blit(asurf.convert_alpha(),[0,0])
    #SCREEN.blit(asurf, imagerect)
   	
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

	
