import sys,codecs
import pygame
import button,slidemenu

ScrSize = (800,700)
Origin  = (0,0)
BackColor    = (128,64,0)
FONT = 'data/font/FEASFBRG.ttf'
def showHelp():
    pygame.init()
    screen = pygame.display.set_mode(ScrSize)
    MousePressed=False # Pressed down THIS FRAME
    MouseDown=False # mouse is held down
    MouseReleased=False # Released THIS FRAME
    bg = pygame.Surface(ScrSize).convert()
    img = pygame.image.load('data/images/help.png') 
    imgback = pygame.image.load('data/images/back.png') 
    screen.blit(bg,Origin)
    backButton = button.Button()
    backButton.create_button(screen,BackColor, 681, 639, 4, 40,    0, "", (0,0,255),20)   
    screen.blit(pygame.font.Font(FONT, 20).render("BACK", True, (255,255,102)), (681,675))
    pygame.display.flip()
    while True:	
	screen.blit(bg,Origin)
	screen.blit(img,Origin)
	backButton = button.Button()
	backButton.create_button(screen,BackColor, 681, 639, 40, 40,    0, "", (128,45,255),20)  
	screen.blit(imgback,(681,629))
	screen.blit(pygame.font.Font(FONT, 20).render("BACK", True, (255,255,102)),  (681,675))
	pos=pygame.mouse.get_pos() #get the mouse position
	for event in pygame.event.get(): #get event from pygame	
	    if event.type is pygame.QUIT:
		pygame.quit()#finish pygame
		sys.exit()
	    
	    if event.type == pygame.MOUSEBUTTONDOWN:
		MousePressed = True 
		MouseDown = True 
			   
	    if event.type == pygame.MOUSEBUTTONUP:
		MouseReleased = True
		MouseDown = False	 
	    
	    if MousePressed == True:
		if backButton.pressed(pygame.mouse.get_pos()):	   	
		    mainmenu = slidemenu.run()
		    mainmenu.runm()  
	     
	    pygame.display.flip()		
	    MousePressed = False # Reset these to False
	    MouseReleased = False # Ditto	    
if __name__ == '__main__':
    showHelp()