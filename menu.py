from Tkinter import *
import tkFont,pygame
import scrabble

class App():
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
    App()
    mainloop()


#==================== GAME MENU =====================

class GameMenu(Menu):

	PLAY_TURN = "play"
	RESHUFFLE = "shuffle"
	MAIN_MENU = "quit"
	HINT_TURN = "hint"

	def __init__(self, useHintBox = False):
	        self.buttons = {}
		self.rect = (570, 300, 150, 300)
		self.background = (0, 0, 0)
		self.buttons[GameMenu.PLAY_TURN] = Button("PLAY", (570, 300, 150, 30))
		self.buttons[GameMenu.RESHUFFLE] = Button("SHUFFLE", (570, 340, 150, 30))
		self.buttons[GameMenu.MAIN_MENU] = Button("QUIT", (570, 380, 150, 30))
		SCREEN.fill((0,0,0))
	    
	def redraw(self):
		pygame.draw.rect(SCREEN, self.background, self.rect)
		for button in self.buttons.values():
			button.redraw()		
			
			
    