# -*- coding: cp1254 -*-
from pygame.locals import *
import pygame,sys
import scrabble
from modul_utils import button,slidemenu

def main():       
    #create main screen!        
    mainmenu = slidemenu.run()
    mainmenu.runm()      

BG =(132,24,2)
FONT = pygame.font.SysFont("comicsansms", 16)
FONT2 = pygame.font.Font('data/font/FreeSansBold.ttf', 16)
imgplay = pygame.image.load('data/images/play.png')
imgsurrender = pygame.image.load('data/images/teslimol.png')
imgmix = pygame.image.load('data/images/shuffle.png')
imgchange = pygame.image.load('data/images/change.png')
imgpass = pygame.image.load('data/images/pass.png')
imgretrieveback = pygame.image.load('data/images/retrieveback.png')
imgexit = pygame.image.load('data/images/exit.png')
imghome = pygame.image.load('data/images/home.png')

pop_change = pygame.image.load('data/images/pop_change.png')
pop_surrender = pygame.image.load('data/images/pop_surrender.png')  
pop_exit = pygame.image.load('data/images/pop_exit.png')

gameresult_surrender = pygame.image.load('data/images/gameresult_surrender.png')
gameresult_lose = pygame.image.load('data/images/gameresult_lose.png')
gameresult_win = pygame.image.load('data/images/gameresult_win.png')
gameresult_draw = pygame.image.load('data/images/gameresult_draw.png')
#==================== GAME MENU =====================

class GameMenu():
    def __init__(self):
	global SCREEN
	SCREEN = scrabble.getScreen()
	
    #Update the display and show the button
    def createButtons(self):
	#global SCREEN
	global playButton,changeButton,backButton,mixButton,passButton,surrenderButton,exitButton,homeButton
	playButton = button.Button()
	changeButton = button.Button()
	backButton = button.Button()
	passButton = button.Button()
	mixButton = button.Button()
	surrenderButton = button.Button()
	exitButton = button.Button()
	homeButton = button.Button()
	
	#Parameters:               surface,      color, x,   y,   length, height, width,    text,      text_color
	playButton.create_button(SCREEN,BG,425, 560, 40,    30,    0, "", (255,0,0),20)
	SCREEN.blit(imgplay,(420,550))	

	mixButton.create_button(SCREEN, BG,25, 620, 40,    30,    0, "", (255,255,255),12)
	SCREEN.blit(imgmix,(25,610))
	SCREEN.blit(FONT.render(u"KARIŞTIR", True, (255,255,255)), (10, 660))
	
	changeButton.create_button(SCREEN,BG, 140, 620, 40,    30,    0, "", (255,255,255),12)
	SCREEN.blit(imgchange,(140,610))
	SCREEN.blit(FONT.render(u"DEĞİŞTİR", True, (255,255,255)), (125, 660))	
	
	backButton.create_button(SCREEN,BG, 255, 620, 40,    30,    0, "", (255,255,255),12)
	SCREEN.blit(imgretrieveback,(255,610))
	SCREEN.blit(FONT.render(u"GERİ AL", True, (255,255,255)), (245, 660))		
	
	passButton.create_button(SCREEN,  BG, 370, 620, 40,    30,    0,    "", (255,255,255),12)
	SCREEN.blit(imgpass,(370,610))
	SCREEN.blit(FONT.render("PAS", True, (255,255,255)), (375, 660))		
	
	homeButton.create_button(SCREEN,BG, 660, 660, 32,    32,    0,"", (255,255,255),12)
	SCREEN.blit(imghome,(660,660))		

	surrenderButton.create_button(SCREEN,BG, 705, 660, 32,    32,    0,"", (255,255,255),12)
	SCREEN.blit(imgsurrender,(705,660))
	
	exitButton.create_button(SCREEN,BG, 750, 660, 32,    32,    0,"", (255,255,255),12)
	SCREEN.blit(imgexit,(750,660))	

    def createOkCancelButtons(self,type):
	global okButton,cancelButton
	okButton = button.Button()
	cancelButton = button.Button()
	okButton.create_button(SCREEN, (100, 171, 28), 280, 310, 75,   20,    0,  u"   DEĞİŞTİR", (255,255,255),15)
	cancelButton.create_button(SCREEN,(195,32,32), 170, 310, 75,   20,    0,    u" VAZGEÇ", (255,255,255),15)	
        if type == "change":
	    popup = pop_change
	elif type == "surrender":
	    popup = pop_surrender
	elif type == "exit":
	    popup = pop_exit	
	SCREEN.blit(popup,(150, 200))

    def drawGameResult(self,humanScore,aiScore,type,remainingTilesPoints):
	global closeButton,againButton
	closeButton = button.Button()
	againButton = button.Button()
	closeButton.create_button(SCREEN, (100, 171, 28), 170 ,400, 85,   20,    0,  u"   KAPAT", (255,255,255),15)
	againButton.create_button(SCREEN,(195,32,32), 290, 400, 85,   20,    0,    u" TEKRAR OYNA", (255,255,255),15)	
	if type == "surrender":
	    result = gameresult_surrender
        else:
	    if humanScore < aiScore:
	        result = gameresult_lose
	    elif humanScore > aiScore:
	        result = gameresult_win
	    else:
		result = gameresult_draw
		
	SCREEN.blit(result,(150, 200))
	SCREEN.blit(FONT2.render(str(humanScore), True, (0,0,0)), (350, 274))
	SCREEN.blit(FONT2.render(str(aiScore), True, (0,0,0)), (350, 312))	
	if type == "gameover" and remainingTilesPoints != 0:
	    SCREEN.blit(FONT2.render(u"Ceza puanı:"+str(remainingTilesPoints), True, (255,0,0)), (200, 352))