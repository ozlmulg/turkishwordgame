from Tkinter import *
from pygame.locals import *
import tkFont,pygame,sys
import scrabble,button

class MainMenu():
    def __init__(self):
        # create buttons!
        self.centerWindow()
        self.playbutton = Button(text="PLAY",height=3,width=20, bg="Green", fg="Black",font=tkFont.Font(family="Verdana", size=12, weight=tkFont.BOLD), command=self.runGame)
        self.playbutton.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.helpbutton = Button(text="HELP",height=3,width=20, bg="Blue", fg="Black",font=tkFont.Font(family="Times", size=12, weight=tkFont.BOLD), command=screen.destroy)
        self.helpbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.exitbutton = Button(text="EXIT",height=3,width=20, bg="Red", fg="Black",font=tkFont.Font(family="Times", size=12, weight=tkFont.BOLD),command=screen.destroy)
        self.exitbutton.place(relx=0.5, rely=0.7, anchor=CENTER)
    def runGame(self):
        screen.destroy()
        scrabble.main()#close the menu and start game
    def centerWindow(self):            
        w = 800
        h = 700
        
        sw = screen.winfo_screenwidth()
        sh = screen.winfo_screenheight()
                
        x = (sw - w)/2
        y = (sh - h)/2
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))    
 
def main():       
    #create main screen!        
    global screen
    screen= Tk("Scrabble Game")
    screen.resizable(width=FALSE, height=FALSE) #not resizable
    screen.configure(background="Black")#background color of screen
    screen.title("SCRABBLE GAME")#title of the screen
    MainMenu()
    mainloop()


#==================== GAME MENU =====================

class GameMenu():
	def __init__(self):
	    global SCREEN
	    SCREEN = scrabble.getScreen()
	    SCREEN.fill((0,0,0))
	    
	#Update the display and show the button
	def createButtons(self):
	    #global SCREEN
	    SCREEN.fill((0,0,0))
	    global playButton,shuffleButton,exitButton
	    playButton = button.Button()
	    shuffleButton = button.Button()
	    exitButton = button.Button()
	    
	    #Parameters:               surface,      color, x,   y,   length, height, width,    text,      text_color
	    playButton.create_button(SCREEN, (0,128,255), 600, 290, 120,    40,    0,    "Play", (255,255,255))
	    shuffleButton.create_button(SCREEN, (0,128,255), 600, 350, 120,    40,    0,  "Shuffle", (255,255,255))
	    exitButton.create_button(SCREEN, (0,128,255), 600, 410, 120,    40,    0,     "Back", (255,255,255))
		
    