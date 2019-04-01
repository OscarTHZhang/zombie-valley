
'''
This mode allows user to type in or choose some game basics
such as number of monster they want to play, difficulty(speed)
MVC from: pd43.github.io
'''

from tkinter import *
from buttonClass import *
import random

###############################################################################
class typeMode(object):

    width = height = 600

    # Model
    def __init__(self):
        self.typeText = ""
        self.initButts()
        self.back = PhotoImage(file = "img/type.gif") # Background image


    def initButts(self):
        cx1 = typeMode.width/4
        cx2 = typeMode.width/2
        cx3 = 3*typeMode.width/4
        cy = 8*typeMode.height/9
        self.backButt = Control(cx1, cy, 130, 65, "Back")
        self.randButt = Control(cx2, cy, 130, 65, "Random")
        self.playButt = Control(cx3, cy, 130, 65, "Play") 
        # set #Zombie randomly


    # Controller
    def mousePressed(self, event):
        if self.randButt.isInside(event.x, event.y): 
            self.typeText = str(random.randint(10,99))

        elif self.backButt.isInside(event.x, event.y): return "Start"
        elif self.playButt.isInside(event.x, event.y):
            if (len(self.typeText)==2) and (10 <= int(self.typeText) <= 99):
                print("True")
                temp = ("Game", int(self.typeText))
                return temp

    def mouseMoved(self, event):
        self.backButt.magicPrompt(event.x, event.y)
        self.randButt.magicPrompt(event.x, event.y)
        self.playButt.magicPrompt(event.x, event.y)

    def keyPressed(self, event):
        if (len(self.typeText) < 2 and event.keysym.isdigit()):
            self.typeText += event.keysym
        elif event.keysym == "BackSpace":
            self.typeText = self.typeText[:-1]


    def timerFired(self):
        pass


    # Viewer
    def redrawAll(self, canvas):
        self.showBack(canvas)
        self.showTypeText(canvas)
        self.showInfo(canvas)
        self.showButts(canvas)

    
    def showBack(self, canvas):
        cx, cy = typeMode.width/2, typeMode.height/2
        canvas.create_image(cx, cy, image=self.back)

    
    def showButts(self, canvas):
        self.backButt.showButton(canvas)
        self.randButt.showButton(canvas)
        self.playButt.showButton(canvas)

    def showTypeText(self, canvas):
        cx, cy = typeMode.width/2, typeMode.height/2
        canvas.create_text(cx, cy, text=self.typeText, fill="white", font='impact 80')

    
    def showInfo(self, canvas):
        cx, cy = typeMode.width/2, 70
        info = 'Please set #Zombies\nOR set it randomly'
        canvas.create_text(cx, cy, text=info, fill="white", font='impact 50')

