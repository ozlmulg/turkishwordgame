# -*- coding: cp1254 -*-
from Tkinter import *
from pygame.locals import *
import tkFont,pygame,sys
import scrabble,button

class MainMenu():
    def __init__(self):
        # create buttons!
        self.centerWindow()
        self.playbutton = Button(text="OYNA",height=3,width=20, bg="Green", fg="Black",font=tkFont.Font(family="Verdana", size=12, weight=tkFont.BOLD), command=self.runGame)
        self.playbutton.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.helpbutton = Button(text="YARDIM",height=3,width=20, bg="Blue", fg="Black",font=tkFont.Font(family="Times", size=12, weight=tkFont.BOLD), command=screen.destroy)
        self.helpbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.exitbutton = Button(text=u"ÇIKIŞ",height=3,width=20, bg="Red", fg="Black",font=tkFont.Font(family="Times", size=12, weight=tkFont.BOLD),command=screen.destroy)
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
	def draw(self):
	    #global SCREEN
	    global playButton,changeButton,backButton
	    playButton = button.Button()
	    changeButton = button.Button()
	    backButton = button.Button()
	    
	    #Parameters:               surface,      color, x,   y,   length, height, width,    text,      text_color
	    playButton.create_button(SCREEN, (0,204,102), 600, 290, 120,    40,    0,    "Oyna", (0,0,0))
	    changeButton.create_button(SCREEN, (0,204,102), 600, 350, 120,    40,    0,  u"Değiştir", (0,0,0))
	    backButton.create_button(SCREEN, (0,204,102), 600, 410, 120,    40,    0,     "Geri Al", (0,0,0))
		
    