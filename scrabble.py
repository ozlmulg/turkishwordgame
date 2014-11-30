import pygame,sys
from pygame.locals import *
import board,bag,menu,human,tile,player


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
    global tilem
    tilem = None
# ##################### All positions that any tile can be at and their status of occupy, both board and tray 
    
    squares = {}
    
    for i in range (board.Board.GRID_SIZE):
	for j in range (board.Board.GRID_SIZE):
	    squares[(5 + j * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER), 5 + i * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER))] = 0
	    
	    
    for i in range (player.Player.TRAY_SIZE):
	    squares[human.Human.TRAY_FIRSTLEFT + i * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER), human.Human.TRAY_FIRSTTOP] = 1
    
	                 
    
# ##################### All positions that any tile can be at and their status of occupy, both board and tray 


    Target=None # target of Drag/Drop 
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
			# ####   NEW
			squares[Target.coordinate] = 0 # Update the position as empty
			# ####   NEW
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
		
		slideTile = 4 # if a tile is dropped on another tile, slide the tile to the position which was closer
	    
	    if MouseReleased and Target is not None:
		#  fit the tile in the positions
		if (Target.coordinate[0] < board.Board.GRID_SIZE * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER) - board.Board.SQUARE_SIZE/2 + 1 and Target.coordinate[1] < board.Board.GRID_SIZE * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER) - board.Board.SQUARE_SIZE/2 + 1 and Target.coordinate[0] > board.Board.SQUARE_BORDER + 1 - board.Board.SQUARE_SIZE/2 and Target.coordinate[1] > board.Board.SQUARE_BORDER + 1 - board.Board.SQUARE_SIZE/2) :
		    i = 5
		    a = Target.coordinate
		    while i <= Target.coordinate[0] + 16 :
			i = i + 36
			
		    Target.coordinate = (i - 36, Target.coordinate[1])
		    
		    i = 5
		    while i <= Target.coordinate[1] + 16 :
			i = i + 36
		    
		    Target.coordinate = (Target.coordinate[0], i - 36)	
		    
		# if the tile put on tray
		elif (Target.coordinate[0] > human.Human.TRAY_LEFT and Target.coordinate[1] > human.Human.TRAY_TOP and Target.coordinate[0] < human.Human.TRAY_LEFT + (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8 and Target.coordinate[1] < human.Human.TRAY_TOP + tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER*2):
		    i = human.Human.TRAY_FIRSTLEFT
		    a = Target.coordinate
		    while i <= Target.coordinate[0] + 16 :
			i = i + 36		    
			
		    Target.coordinate = (i - 36, human.Human.TRAY_FIRSTTOP)
		    
		    
		    
		else:
		    Target.coordinate = Target.oldPos # if tile put out of board bring it back
		# fit the tile in the positions - end
		
		
		# slide the tile if it is dropped on another tile
		#for t in players[active].tray[:player.Player.TRAY_SIZE-1]: # search all the tray but not last element which is the tile itself
		    #if t.coordinate == Target.coordinate:
		slidingTo = 4
		if squares[Target.coordinate] == 1:
		    if Target.coordinate[0] <= a[0] and Target.coordinate[1] <= a[1]:
			if a[0]-Target.coordinate[0]>=a[1]-Target.coordinate[1]:
			    Target.coordinate = (Target.coordinate[0] + 36, Target.coordinate[1])
			    slidingTo = 1
			else:
			    Target.coordinate = (Target.coordinate[0], Target.coordinate[1] + 36)
			    slidingTo = 3
			    
		    elif Target.coordinate[0] > a[0] and Target.coordinate[1] <= a[1]:
			if Target.coordinate[0] - a[0] >= a[1] - Target.coordinate[1]:
			    Target.coordinate = (Target.coordinate[0] - 36, Target.coordinate[1])
			    slidingTo = 0
			else:
			    Target.coordinate = (Target.coordinate[0], Target.coordinate[1] + 36)
			    slidingTo = 3
			    
		    elif Target.coordinate[0] > a[0] and Target.coordinate[1] > a[1]:
			if Target.coordinate[0] - a[0] >= Target.coordinate[1] - a[1]:
			    Target.coordinate = (Target.coordinate[0] - 36, Target.coordinate[1])
			    slidingTo = 0
			else:
			    Target.coordinate = (Target.coordinate[0], Target.coordinate[1] - 36)
			    slidingTo = 2
			    
		    elif Target.coordinate[0] <= a[0] and Target.coordinate[1] > a[1]:
			if a[0]-Target.coordinate[0] >= Target.coordinate[1] - a[1]:
			    Target.coordinate = (Target.coordinate[0] + 36, Target.coordinate[1])
			    slidingTo = 1
			else:
			    Target.coordinate = (Target.coordinate[0], Target.coordinate[1] - 36)
			    slidingTo = 2
			    
		    while squares[Target.coordinate] == 1:
			if slidingTo == 0:
			    Target.coordinate = (Target.coordinate[0] + 36, Target.coordinate[1])
			elif slidingTo == 1:
			    Target.coordinate = (Target.coordinate[0] - 36, Target.coordinate[1])
			elif slidingTo == 2:
			    Target.coordinate = (Target.coordinate[0], Target.coordinate[1] + 36)
			elif slidingTo == 3:
			    Target.coordinate = (Target.coordinate[0], Target.coordinate[1] - 36)
			    
			
	    # slide the tile if it is dropped on another tile
			    
		squares[Target.coordinate] = 1

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
    global asurf
    global imagerect
    asurf = pygame.image.load('Board.jpg')
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

	
