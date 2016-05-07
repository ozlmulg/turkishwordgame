# -*- coding: utf-8 -*-
from pygame import *
font.init()
from math import cos, radians
import webbrowser
import scrabble,sys,pygame,help

def menu(menu, pos='center', font1=None, font2=None, color1=(128, 128, 128), color2=None, interline=5, justify=True, light=5, speed=300, lag=30):
  
    class Item(Rect):

        def __init__(self, menu, label):
            Rect.__init__(self, menu)
            self.label = label

    def show():
        i = Rect((0, 0), font2.size(menu[idx].label))
        if justify:
            i.center = menu[idx].center
        else:
            i.midleft = menu[idx].midleft
        display.update(
            (scr.blit(bg, menu[idx], menu[idx]), scr.blit(font2.render(menu[idx].label, 1, (255, 255, 255)), i)))

        time.wait(50)
        scr.blit(bg, r2, r2)
        [scr.blit(font1.render(item.label, 1, color1), item)
         for item in menu if item != menu[idx]]
        r = scr.blit(font2.render(menu[idx].label, 1, color2), i)
        display.update(r2)

        return r

    def anim():
        clk = time.Clock()
        a = [menu[0]] if lag else menu[:]
        c = 0
        while a:
            for i in a:
                g = i.copy()
                i.x = i.animx.pop(0)
                r = scr.blit(font1.render(i.label, 1, color1), i)
                display.update((g, r))

                scr.blit(bg, r, r)
            c += 1
            if not a[0].animx:
                a.pop(0)
                if not lag:
                    break
            if lag:
                foo, bar = divmod(c, lag)
                if not bar and foo < len(menu):
                    a.append(menu[foo])
            clk.tick(speed)

    events = event.get()
    scr = display.get_surface()
    scrrect = scr.get_rect()
    bg = scr.copy()
    if not font1:
        font1 = font.Font(None, scrrect.h // len(menu) // 3)
    if not font2:
        font2 = font1
    if not color1:
        color1 = (128, 128, 128)
    if not color2:
        color2 = list(map(lambda x: x + (255 - x) * light // 10, color1))
    m = max(menu, key=font1.size)
    r1 = Rect((0, 0), font1.size(m))
    ih = r1.size[1]
    r2 = Rect((0, 0), font2.size(m))
    r2.union_ip(r1)
    w, h = r2.w - r1.w, r2.h - r1.h
    r1.h = (r1.h + interline) * len(menu) - interline
    r2 = r1.inflate(w, h)

    try:
        setattr(r2, pos, getattr(scrrect, pos))
    except:
        r2.topleft = pos
    if justify:
        r1.center = r2.center
    else:
        r1.midleft = r2.midleft

    menu = [Item(((r1.x, r1.y + e * (ih + interline)), font1.size(i)), i)
            for e, i in enumerate(menu)if i]
    if justify:
        for i in menu:
            i.centerx = r1.centerx

    if speed:
        for i in menu:
            z = r1.w - i.x + r1.x
            i.animx = [
                cos(radians(x)) * (i.x + z) - z for x in list(range(90, -1, -1))]
            i.x = i.animx.pop(0)
        anim()
        for i in menu:
            z = scrrect.w + i.x - r1.x
            i.animx = [
                cos(radians(x)) * (-z + i.x) + z for x in list(range(0, -91, -1))]
            i.x = i.animx.pop(0)

    mpos = Rect(mouse.get_pos(), (0, 0))
    event.post(
        event.Event(MOUSEMOTION, {'pos': mpos.topleft if mpos.collidelistall(menu) else menu[0].center}))
    idx = -1
    display.set_caption("KELiME OYUNU")

    while True:

        ev = event.wait()
	if ev.type == pygame.QUIT: 
	    pygame.quit()
	    sys.exit()

        if ev.type == MOUSEMOTION:
            idx_ = Rect(ev.pos, (0, 0)).collidelist(menu)
            if idx_ > -1 and idx_ != idx:
                idx = idx_
                r = show()
        elif ev.type == MOUSEBUTTONUP and r.collidepoint(ev.pos):
            ret = menu[idx].label, idx
            break
        elif ev.type == KEYDOWN:
            try:
                idx = (idx + {K_UP: -1, K_DOWN: 1}[ev.key]) % len(menu)
                r = show()
            except:
                if ev.key in (K_RETURN, K_KP_ENTER):
                    ret = menu[idx].label, idx
                    break
                elif ev.key == K_ESCAPE:
                    ret = None, None
                    break
    scr.blit(bg, r2, r2)

    if speed:
        [scr.blit(font1.render(i.label, 1, color1), i) for i in menu]
        display.update(r2)
        time.wait(50)
        scr.blit(bg, r2, r2)
        anim()
    else:
        display.update(r2)

    for ev in events:
        event.post(ev)
    return ret


class run(object):
    def runm(self):       
        time.Clock()
        from os.path import dirname, join

        here = dirname(__file__)
        scr = display.set_mode((800, 700))
        f = font.Font(join('data/font/FEASFBRG.ttf'), 85)
        f1 = font.Font(join('data/font/FEASFBRG.ttf'), 95)
        f2 = font.Font(join('data/font/FEASFBRG.ttf'), 75) 
        mainmenu = f.render('KELiME OYUNU', 1, (255,192, 0))
        r = mainmenu.get_rect()
        r.centerx, r.top = 400, 100
        
        #background_main = image.load('data/images/bg.png').convert()
        #scr.blit(background_main, (0,0))
	scr.fill((132,24,2)) # clear screen
	
        bg = scr.copy()
        scr.blit(mainmenu, r)
        display.flip()
    
	menu1 = {"menu": ['OYNA', 'YARDIM','DEMO', 'KAPAT'], "font1": f2,"font2": f1, "pos":
		 'center', "color1": (154, 180, 61), "light": 6, "speed": 200, "lag": 20}

        menus = (menu1)
        playlist = [menu1]

        resp = "re-show"

	while True:
	    if resp == "re-show":
		resp = menu(**menu1)[0]
	    
	    if resp == 'OYNA':
		scrabble.run(False)  
	
	    if resp == 'YARDIM':
                help.showHelp()
		
	    if resp == 'DEMO':
	        scrabble.run(True)	    

	    if resp == 'KAPAT':
		pygame.quit()
		sys.exit()