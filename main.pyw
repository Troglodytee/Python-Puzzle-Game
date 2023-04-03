from tkinter import *
from random import *

def clavier(event) :
    global coord
    global positions1
    if ecran == 2 :
        touche = event.keysym
        if touche == "Up" and coord[1] > 0 :
            coord[1] -= 1
        elif touche == "Down" and coord[1] < 2 :
            coord[1] += 1
        elif touche == "Left" and coord[0] > 0 :
            coord[0] -= 1
        elif touche == "Right" and coord[0] < 2 :
            coord[0] += 1
        elif touche == "space" :
            a = positions1[coord[0]+coord[1]*4]
            positions1[coord[0]+coord[1]*4] = positions1[coord[0]+coord[1]*4+4]
            positions1[coord[0]+coord[1]*4+4] = positions1[coord[0]+coord[1]*4+5]
            positions1[coord[0]+coord[1]*4+5] = positions1[coord[0]+coord[1]*4+1]
            positions1[coord[0]+coord[1]*4+1] = a
        placement()

def creajeu() :
    global positions1
    global positions2
    global coord
    global ecran
    ecran = 1
    positions1 = [1,1,2,2,1,1,2,2,3,3,4,4,3,3,4,4]
    b = positions1
    positions2 = []
    for loop in range (len(positions1)) :
        a = randint(0,len(b)-1)
        positions2 += [b[a]]
        del b[a:a+1]
    positions1 = [1,1,2,2,1,1,2,2,3,3,4,4,3,3,4,4]
    coord = [0,0]
    placement()

def placement() :
    global canvas
    global positions1
    global positions2
    global coord
    global ecran
    global score
    canvas.delete('all')
    for y in range (4) :
        for x in range (4) :
            if positions1[y*4+x] == 1 :
                couleur = 'yellow'
            elif positions1[y*4+x] == 2 :
                couleur = 'red'
            elif positions1[y*4+x] == 3 :
                couleur = 'blue'
            elif positions1[y*4+x] == 4 :
                couleur = 'green'
            rec = canvas.create_polygon(x*100,y*100,x*100+100,y*100,x*100+100,y*100+100,x*100,y*100+100,fill=couleur)
    for y in range (4) :
        for x in range (4) :
            if positions2[y*4+x] == 1 :
                couleur = 'yellow'
            elif positions2[y*4+x] == 2 :
                couleur = 'red'
            elif positions2[y*4+x] == 3 :
                couleur = 'blue'
            elif positions2[y*4+x] == 4 :
                couleur = 'green'
            rec = canvas.create_polygon(x*25+400,y*25,x*25+425,y*25,x*25+425,y*25+25,x*25+400,y*25+25,fill=couleur)
    rec = canvas.create_rectangle(400,0,500,100)
    rec = canvas.create_polygon(coord[0]*100,coord[1]*100,coord[0]*100+5,coord[1]*100,coord[0]*100+5,coord[1]*100+200,coord[0]*100,coord[1]*100+200,fill='white')
    rec = canvas.create_polygon(coord[0]*100+200,coord[1]*100,coord[0]*100+195,coord[1]*100,coord[0]*100+195,coord[1]*100+200,coord[0]*100+200,coord[1]*100+200,fill='white')
    rec = canvas.create_polygon(coord[0]*100,coord[1]*100,coord[0]*100+200,coord[1]*100,coord[0]*100+200,coord[1]*100+5,coord[0]*100,coord[1]*100+5,fill='white')
    rec = canvas.create_polygon(coord[0]*100,coord[1]*100+200,coord[0]*100+200,coord[1]*100+200,coord[0]*100+200,coord[1]*100+195,coord[0]*100,coord[1]*100+195,fill='white')
    rec = canvas.create_text(450,350,text=score,font="Arial 20",fill='white')
    ecran = 2
    if positions1 == positions2 :
        ecran = 1
        score += 1
        canvas.after(2000,creajeu)

fenetre = Tk()
fenetre.title("Casse tête")

canvas = Canvas(fenetre,width=500,height=400,bg='black')
canvas.pack()
canvas.focus_set()
canvas.bind("<Key>",clavier)

score = 0

creajeu()

fenetre.mainloop()