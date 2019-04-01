'''
losing mode
pd43.github.io
'''

from tkinter import *
from buttonClass import *
###############################################################################
class loseMode(object):

	width, height = 800, 400

	# MODEL
	def __init__(self):
	    self.lostImg = PhotoImage(file = "img/lost.gif")
	    self.initButts()

	def initButts(self):
		cx1 = loseMode.width/3
		cx2 = loseMode.width*2/3
		cy = loseMode.height*4/5
		w, h = 130, 65
		self.setButt = Bloody(cx1, cy, w, h, "Settings")
		# go to type mode to re-set the game
		self.mainButt = Bloody(cx2, cy, w, h, "Main menu")
		# go to the main menu, start mode

	# Controller
	def mousePressed(self, event):
	    if self.setButt.isInside(event.x, event.y):
	    	return 'Type'
	    elif self.mainButt.isInside(event.x, event.y):
	    	return 'Start'

	def mouseMoved(self, event):
		self.setButt.magicPrompt(event.x, event.y)
		self.mainButt.magicPrompt(event.x, event.y)

	def keyPressed(self, event):
	    pass

	def timerFired(self):
	    pass


	# View
	def redrawAll(self, canvas):
	    self.showBack(canvas)
	    self.showInfo(canvas)
	    self.showButts(canvas)

	def showBack(self, canvas):
		cx, cy = loseMode.width/2, loseMode.height/2
		canvas.create_image(cx, cy, image = self.lostImg)

	def showInfo(self, canvas):
		cx, cy = loseMode.width/2, loseMode.height/4
		info = "You become a ZOMBIE"
		canvas.create_text(cx, cy, text=info, fill='white', font='impact 80')

	def showButts(self, canvas):
		self.mainButt.showButton(canvas)
		self.setButt.showButton(canvas)

