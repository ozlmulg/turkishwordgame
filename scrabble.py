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
# ##############save initial image
    global asurf
    asurf = pygame.image.load('Board.jpg') 
    playedTiles = []
# ##################### All positions that any tile can be at and their status of occupy, both board and tray 
    
    squares = {}
    isFirstMove = True
    MIDDLE_SQUARE = (257, 257)    
    
    for i in range (board.Board.GRID_SIZE):
	for j in range (board.Board.GRID_SIZE):
	    squares[(5 + j * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER), 5 + i * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER))] = 0
	    
	    
    for i in range (player.Player.TRAY_SIZE):
	    squares[human.Human.TRAY_FIRSTLEFT + i * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER), human.Human.TRAY_FIRSTTOP] = 1
    
	                 
    
# ##################### All positions that any tile can be at and their status of occupy, both board and tray 


    Target=None # target of Drag/Drop 
    while True: #show SCREEN until not close
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
		    
	    if event.type == pygame.MOUSEBUTTONDOWN:
		MousePressed = True 
		MouseDown = True 
			   
	    if event.type == pygame.MOUSEBUTTONUP:
		MouseReleased = True
		MouseDown = False	 
		
	    if MousePressed == True:
		if menu.playButton.pressed(pygame.mouse.get_pos()):
		    print "Play pressed!"
		    # important !!: tiles must be together

		    # take the list of x and y coordinates of the palyed tiles
		    xArr = []
		    yArr = []
		    for til in playedTiles:
			xArr.append(til.coordinate[0])
			yArr.append(til.coordinate[1])
		    
		    # find the min and max value for x and y coordinate
		    minX = min(xArr)
		    maxX = max(xArr)	
		    minY = min(yArr)
		    maxY = max(yArr)

		    isAccepted = True # accepted move or not?
		    isInPlayArea = True #played tiles are in play area or not
		    
		    #range(playedTiles[0].coordinate[0],playedTiles[-1].coordinate[0],36):
		    # if in the same row all, there will be no gap between the first and last tile
		    if minY == maxY: # if all played tiles in the same row
		        print "c 44"
		        for xCoor in range(minX,maxX,36):
			    if squares[(xCoor,playedTiles[0].coordinate[1])] == 0:
			       isAccepted = False
			       break
		    elif minX == maxX:# if all played tiles in the same column
			print "c 55"
			# if in the same column all, there will be no gap between the first and last tile
			for yCoor in range(minY,maxY,36):
			    if squares[(playedTiles[0].coordinate[0],yCoor)] == 0:
				isAccepted = False
				break
		    #played tiles must be same row or same column otherwise not will be accepted
		    else:
			print "c 66"
			isAccepted = False
		    
		    # CONTROL for the played tiles are in PLAY AREA or not!!
                    if isAccepted:
			print "c 11"
			if len(playedTiles) == 1:
			    if squares[(playedTiles[0].coordinate[0]+36,playedTiles[0].coordinate[1])] == 0 and squares[(playedTiles[0].coordinate[0]-36,playedTiles[0].coordinate[1])] == 0 and squares[(playedTiles[0].coordinate[0],playedTiles[0].coordinate[1]+36)] == 0 and squares[(playedTiles[0].coordinate[0],playedTiles[0].coordinate[1]-36)] == 0 and not isFirstMove:
				isInPlayArea = False
			else:
			    for i in range(0, len(playedTiles)-1):
				print "c aaa"
				if (squares[(playedTiles[i].coordinate[0]+36,playedTiles[i].coordinate[1])] == 1 and playedTiles[i].coordinate[0]+36 not in xArr) or (squares[(playedTiles[i].coordinate[0]-36,playedTiles[i].coordinate[1])] == 1 and playedTiles[i].coordinate[0]-36 not in xArr) or (squares[(playedTiles[i].coordinate[0],playedTiles[i].coordinate[1]+36)] == 1 and playedTiles[i].coordinate[1]+36 not in yArr) or (squares[(playedTiles[i].coordinate[0],playedTiles[i].coordinate[1]-36)] == 1 and playedTiles[i].coordinate[1]-36 not in yArr):
				    isInPlayArea = True
				    print "c 22"
				    break
				else:
				    print "c 33"
				    isInPlayArea = False
						  
		      
		    if isFirstMove and squares[MIDDLE_SQUARE] == 0:
			print "First move must be done to middle of the board"
			
                    elif not isAccepted:
			print "There will be no gap between tiles"
			
		    elif not isInPlayArea and not isFirstMove:
			print "Please put your tiles to played area." 
			
		    else:
			if isFirstMove:
			    isFirstMove = False		    
			# #################save image when the tiles are played#########
			players[active].drawTray(SCREEN)
			for Tar in playedTiles:
			    players[active].tray.remove(Tar)		    
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
		for item in players[active].tray: # search all items
		    if (pos[0] >= (item.coordinate[0]) and # ######## Changed
		        pos[0] <= (item.coordinate[0] + item.SQUARE_SIZE) and 
		        pos[1] >= (item.coordinate[1]) and # ######## Changed
		        pos[1] <= (item.coordinate[1] + item.SQUARE_SIZE) ): # inside the bounding box
			Target = item # "pick up" item
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

	    if MouseDown and Target is not None: # if we are dragging something
		Target.coordinate = (pos[0] - tile.Tile.SQUARE_SIZE/2, pos[1] - tile.Tile.SQUARE_SIZE/2) # move the target with us ############Holds the tile from the middle
	    
	    if MouseReleased and Target is not None:
		print "Target old post:",Target.oldPos
		sys.stdout.flush()
		#  fit the tile in the positions
		if (Target.coordinate[0] < board.Board.GRID_SIZE * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER) - board.Board.SQUARE_SIZE/2 + 1 and Target.coordinate[1] < board.Board.GRID_SIZE * (board.Board.SQUARE_SIZE + board.Board.SQUARE_BORDER) - board.Board.SQUARE_SIZE/2 + 1 and Target.coordinate[0] > board.Board.SQUARE_BORDER + 1 - board.Board.SQUARE_SIZE/2 and Target.coordinate[1] > board.Board.SQUARE_BORDER + 1 - board.Board.SQUARE_SIZE/2) :
		    i = 5
		    a = Target.coordinate[:]
		    while i <= Target.coordinate[0] + 16 :
			i = i + 36
			
		    Target.coordinate = (i - 36, Target.coordinate[1])
		    
		    
		    i = 5
		    while i <= Target.coordinate[1] + 16 :
			i = i + 36
		    
		    Target.coordinate = (Target.coordinate[0], i - 36)	
		    # ###############will remove from tray when played######
		    if(Target not in playedTiles):
			playedTiles.append(Target)
		    # ######################################################		    
		    
		# if the tile put on tray
		elif (Target.coordinate[0] + 16 > human.Human.TRAY_LEFT and Target.coordinate[1] + 16 > human.Human.TRAY_TOP and Target.coordinate[0] + 16 < human.Human.TRAY_LEFT + (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)*8 and Target.coordinate[1] + 16 < human.Human.TRAY_TOP + tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER*2):
		    onTray = True
		    i = human.Human.TRAY_FIRSTLEFT
		    a = Target.coordinate[:]
		    while i <= Target.coordinate[0] + 16 :
			i = i + 36		    
			
		    Target.coordinate = (i - 36, human.Human.TRAY_FIRSTTOP)
		    # ###############will remove add back to tray when played######
		    if(Target in playedTiles):
			playedTiles.remove(Target)
		    # ######################################################		    

		    
		else:
		    Target.coordinate = Target.oldPos # if tile put out of board bring it back
		# fit the tile in the positions - end
		
		
		# slide the tile if it is dropped on another tile
		#for t in players[active].tray[:player.Player.TRAY_SIZE-1]: # search all the tray but not last element which is the tile itself
		    #if t.coordinate == Target.coordinate:
		try:
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
				
			#if onTray == False: ## NOT FINISHED
			while squares[Target.coordinate] == 1:
			    if slidingTo == 0:
				Target.coordinate = (Target.coordinate[0] + 36, Target.coordinate[1])
			    elif slidingTo == 1:
				Target.coordinate = (Target.coordinate[0] - 36, Target.coordinate[1])
			    elif slidingTo == 2:
				Target.coordinate = (Target.coordinate[0], Target.coordinate[1] + 36)
			    elif slidingTo == 3:
				Target.coordinate = (Target.coordinate[0], Target.coordinate[1] - 36)
				    
			#else:  # NOT FINISHED
			    #if Target.oldPos[0] <= Target.coordinate[0]
			    
		except KeyError:
		    Target.coordinate = Target.oldPos # if tile slid out of board bring it back	
			
	    # slide the tile if it is dropped on another tile
			    
		squares[Target.coordinate] = 1
		print "Target coordinate:",Target.coordinate

		Target = None # Drop item, if we have any
				
	    MousePressed = False # Reset these to False
	    MouseReleased = False # Ditto

# ###############
	players[active].drawTray(SCREEN)#draw tiles of the player ## SILINECEK NOT: BU KOD SATIRININ YERI ONEMLI 
	
# #############
        pygame.display.update()    


# ####################################DRAW#############################################
def draw():
    tilebag = bag.Bag() #create a bag of tiles
    global gameboard
    gameboard = board.Board()#crate game board

    global gamemenu
    gamemenu = menu.GameMenu()#create game menu
    SCREEN.fill((0,0,0))
    
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

	
