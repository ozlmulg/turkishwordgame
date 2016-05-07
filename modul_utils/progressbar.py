import sys
import pygame
from pygame.locals import *
import scrabble
 
class ProgressImage:
    def __init__(self, size, initcolor, barcolor):
        global SCREEN
	SCREEN = scrabble.getScreen()
        self.bar = pygame.Surface((size[0]-10,size[1]-10))
        self.bar.fill(initcolor)
	SCREEN.blit(self.bar, (575,485))
	pygame.display.update()
                             
class ProgressBar(ProgressImage):
    def __init__(self, whole, step, size, initcolor, barcolor):
        ProgressImage.__init__(self, size, initcolor, barcolor)
        self.size = size
        self.initcolor = initcolor
        self.barcolor = barcolor
        self.whole = whole
        self.step = step
        if whole < step:
            print "Error: ProgressBar length can't be smaller than step"
            sys.exit(1)
        #self.slice = float(step)/float(whole)
        self.percent = 0.0
 
    def showprogress(self):
        #SCREEN.fill(self.initcolor)
        barwidth = (self.size[0]-10)*self.percent
        barheight = self.size[1]-10
        self.bar = pygame.Surface((barwidth,barheight))
        self.bar.fill(self.barcolor)
	SCREEN.blit(self.bar, (575,485))
        pygame.display.update()
 
    def reset(self):
        self.percent = 0.0
        self.showprogress()
       
    def makestep(self,slice):
        if self.percent <= 1.0:
            self.percent = slice
            self.showprogress()
	else:
	    self.reset()
 
    def quit(self):
        pygame.display.quit()
 
    def isEnd(self):
        if self.percent<=1.0:
            return False
        else:
            return True
           
if __name__ == "__main__":
    pb = ProgressBar(1000, 10, (100,40), (255,255,255), (0,0,255))
    i, j, k = 0, 0, 0
    while not pb.isEnd():
        pygame.time.delay(40)
        pb.makestep()
    pb.quit()
    
