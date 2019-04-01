
'''
Start mode is the main menu of the game
With buttons: start, help, and quit
citation: pd43.github.io
'''

from tkinter import *
from buttonClass import *
import sys


###############################################################################
class startMode(object):

    width = height = 600

# model
    def __init__(self):
    	self.initButts()
    	self.backImg = PhotoImage(file = "img/start.gif")
    	self.titleImg = PhotoImage(file = "img/title.gif")

    def initButts(self):
    	cx = startMode.width/2
    	y1 = startMode.height/2 + startMode.height/7
    	y2 = startMode.height/2 + 2*startMode.height/7
    	y3 = startMode.height/2 + 3*startMode.height/7
    	w, h = 100, 50
    	self.startButt = Butt(cx, y1, w, h, 'Start')
    	self.helpButt = Butt(cx, y2, w, h, 'Help')
    	self.quitButt = Butt(cx, y3, w, h, 'Quit')


    # controller
    def mousePressed(self, event):
        if self.quitButt.isInside(event.x, event.y): return "Quit"
        elif self.helpButt.isInside(event.x, event.y): return "Help"
        elif self.startButt.isInside(event.x, event.y): return "Type"
            

    def mouseMoved(self, event):
        self.startButt.magicPrompt(event.x, event.y)
        self.helpButt.magicPrompt(event.x, event.y)
        self.quitButt.magicPrompt(event.x, event.y)

    def keyPressed(self, event):
        pass

    def timerFired(self):
        pass


    # viewer
    def redrawAll(self, canvas):
    	self.showBack(canvas)
    	self.startButt.showButton(canvas)
    	self.helpButt.showButton(canvas)
    	self.quitButt.showButton(canvas)
    	self.showTitle(canvas)

    def showBack(self, canvas):
    	cx, cy = startMode.width/2, startMode.height/2
    	canvas.create_image(cx, cy, image=self.backImg)

    def showTitle(self, canvas):
    	title = "Zombie Valley"
    	cx, cy = startMode.width/2, startMode.height/7
    	#canvas.create_text(cx, cy, text=title, fill='white', font='impact 60')
    	canvas.create_image(cx, cy, image=self.titleImg)

