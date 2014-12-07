
#elif True:
     # control the first element of played tiles for there are a tile in up,down,right or left of it
    #squares[playedTiles[0]
    #print "1:",playedTiles[0]
    #print "2:",squares[playedTiles[0].coordinate]
    #print "3:",playedTiles[0].coordinate	-> palyed tiles da ilk tasýn yanýnda saðýnda solunda üstünde altýnda eleman var mý diye bakicam. x ve y de 36, 36 artiyor coordinate	


    print "0",squares[playedTiles[0]]
    print "1:",playedTiles[0]
    print "2:",squares[playedTiles[0].coordinate]
    print "3:",playedTiles[0].coordinate	

import pygame,sys

class Disk: # Something we can create and manipulate
    def __init__(self,color,pos,size): # initialze the properties of the object
        self.color=color
        self.pos=pos
        self.size=size
    
    def Render(self,screen):
        pygame.draw.rect(screen,self.color,(self.pos[0],self.pos[1],self.size,self.size))

def main(): # Where we start
    screen=pygame.display.set_mode((600,400))
    running=True
    RenderList=[] # list of objects
    MousePressed=False # Pressed down THIS FRAME
    MouseDown=False # mouse is held down
    MouseReleased=False # Released THIS FRAME
    Target=None # target of Drag/Drop
    #draw(screen)
    #pygame.display.flip()
    while running:
        screen.fill((0,0,0)) # clear screen
        pos=pygame.mouse.get_pos()
	
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()#finish pygame
		sys.exit()#close window
               
            if Event.type == pygame.MOUSEBUTTONDOWN:
                MousePressed=True 
                MouseDown=True 
               
            if Event.type == pygame.MOUSEBUTTONUP:
                MouseReleased=True
                MouseDown=False
             
        if MousePressed==True:
            for item in RenderList: # search all items
                if (pos[0]>=(item.pos[0]-item.size) and 
                    pos[0]<=(item.pos[0]+item.size) and 
                    pos[1]>=(item.pos[1]-item.size) and 
                    pos[1]<=(item.pos[1]+item.size) ): # inside the bounding box
                    Target=item # "pick up" item
            
            
            if Target is None: # didn't find any?
                Target=Disk((0,0,255),pos,32) # create a new one
                RenderList.append(Target) # add to list of things to draw
            
        if MouseDown and Target is not None: # if we are dragging something
            Target.pos=pos # move the target with us
        
        if MouseReleased:
            Target=None # Drop item, if we have any
            
        for item in RenderList:
            item.Render(screen) # Draw all items
            
        MousePressed=False # Reset these to False
        MouseReleased=False # Ditto   
       
        #pygame.draw.rect(screen,(205,255,255),(150,150,32,32))
        pygame.display.flip()
        '''
        pygame.display.flip()
        pygame.draw.rect(screen,(205,255,255),(200,400,32,32)) 
        #pygame.display.flip()
        pygame.draw.rect(screen,(205,255,255),(250,400,32,32))
        pygame.draw.rect(screen,(205,255,255),(300,400,32,32)) 
        pygame.draw.rect(screen,(205,255,255),(350,400,32,32)) 
        pygame.draw.rect(screen,(205,255,255),(400,400,32,32)) 
        pygame.draw.rect(screen,(205,255,255),(450,400,32,32)) 
	'''

'''    
def draw(screen):
    pygame.draw.rect(screen,(205,255,255),(450,400,32,32))   
'''       
    #return # End of function
    
if __name__ == '__main__': # Are we RUNNING from this module?
    main() # Execute our main function