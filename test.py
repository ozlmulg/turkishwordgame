#from random import randint
#print randint(0,9)
#playedTiles = []

#playedTiles.append(1)

#for i in range(len(playedTiles)):
    #print i

    #if resp == 'BACK':
		#scr.blit(background_main, (0, 0))
		##display.update(scr.blit(f0.render('TURKISH WORD GAME', 1, (255, 255, 255))))
		#mainmenu = f0.render('TURKISH WORD GAME', 1, (255, 255, 255))
		#r = mainmenu.get_rect()
		#r.centerx, r.top = 400, 120	  
		#scr.blit(mainmenu, r)
		#display.flip()
		#resp = menu(**menu1)[0]
##toplevel
#from Tkinter import *
#pencere = Tk()
#pencere.tk_setPalette("#D0A9F5")
#gameResultButton = Button(pencere,text="TAMAM", command=pencere.destroy)
#gameResultButton.pack()
#mainloop()

##toplevel
#from Tkinter import *
#pencere = Tk()
#def ekle():
    #pencere2 = Toplevel()
    #btn_pen = Button(pencere2,text="çıkış", command=pencere2.destroy)
    #btn_pen.pack()
#btn_pen2 = Button(pencere,text="ekle", command=ekle)
#btn_pen2.pack()
#mainloop()

##listbox
#from Tkinter import *
#pencere = Tk()
#def yeni():
    #global giris
    #pencere2 = Toplevel()
    #giris = Entry(pencere2)
    #giris.pack()
    #btn2 = Button(pencere2, text="tamam",command=ekle)
    #btn2.pack()
#def ekle():
    #if not giris.get():
        #giris.insert(END, "Veri Yok!")
    #if not "Veri Yok!" in giris.get():
        #liste.insert(END, giris.get())
        #giris.delete(0, END)
#def sil():
    #liste.delete(ACTIVE)
#etiket = Label(text="#################", fg="magenta", bg="light green")
#etiket.pack()
#btn = Button(text="ekle", bg="orange", fg="navy", command=yeni)
#btn.pack()
#btn_sil = Button(text="sil", bg="orange", fg="navy",command=sil)
#btn_sil.pack()
#etiket2 = Label(text="#################", fg="magenta", bg="light green")
#etiket2.pack()
#mainloop()


#from Tkinter import *
#gameResultWindow = Tk()
#gameResultWindow.tk_setPalette("#FFB266")
#etiket = Label(text="#################", fg="magenta", bg="light green")
#etiket.pack()
#btn = Button(text="ekle", bg="orange", fg="navy", command=gameResultWindow.destroy)
#btn.pack()
#btn_sil = Button(text="sil", bg="orange", fg="navy",command=gameResultWindow.destroy)
#btn_sil.pack()
#gameResultButton = Button(gameResultWindow,text="TAMAM", command=gameResultWindow.destroy)
#gameResultButton.pack()
#etiket2 = Label(text="#################", fg="magenta", bg="light green")
#etiket2.pack()
#mainloop()
#import bag
#from collections import OrderedDict
#AIsearchWord = OrderedDict()
#word = "ozlem"
#print len(word)
#TurkishCharList = ['a','b','c','d','e','f','g','ğ','h','ı','i','j','k','l','m']

##tilebag = bag.Bag() #create a bag of tiles
 
#for x in range(1, 30):
    #for y in TurkishCharList:
	#AIsearchWord[(x,y)] = []

#for ch in word:
    #print ch
    #print word.index(ch)
    #AIsearchWord[(word.index(ch)+1,ch)].append(word)
    
#print AIsearchWord
#print AIsearchWord[(1,'z')]
	    
	    

x = [('A',1),('C',2)]

print range(15)