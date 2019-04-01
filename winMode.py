'''
winnig mode
citation: pd43.github.io
'''


from tkinter import *
from buttonClass import *
###############################################################################
class winMode(object):

	width, height = 800, 400

	# MODEL
	def __init__(self):
	    self.wonImg = PhotoImage(file = "img/won.gif")
	    self.initButts()


	def initButts(self):
		cx1 = winMode.width/3
		cx2 = winMode.width*2/3
		cy = winMode.height*4/5
		w, h = 130, 65
		self.setButt = Elegant(cx1, cy, w, h, "Settings")
		# go to type mode to re-set the game
		self.mainButt = Elegant(cx2, cy, w, h, "Main menu")
		# go to the main menu, start mode


	# CONTROLLER
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


	# VIEW
	def redrawAll(self, canvas):
	    self.showBack(canvas)
	    self.showInfo(canvas)
	    self.showButts(canvas)

	def showBack(self, canvas):
		cx, cy= winMode.width/2, winMode.height/2
		canvas.create_image(cx, cy, image = self.wonImg)

	def showInfo(self, canvas):
		cx, cy = winMode.width/3, winMode.height/5
		info = "You survived"
		canvas.create_text(cx, cy, text=info, fill='black', font='impact 80')

	def showButts(self, canvas):
		self.mainButt.showButton(canvas)
		self.setButt.showButton(canvas)

