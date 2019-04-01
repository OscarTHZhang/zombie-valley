####
# Button object


class Butt(object):

	def __init__(self,cx,cy,w,h,label):
		self.cx = cx 		  # x of central point of button
		self.cy = cy 		  # y of central point of button
		self.w = w   		  # width of button
		self.h = h   		  # height of button
		self.label = label    # text on the button
		self.color = 'black'  # button color
		self.labCol = 'black' # label color

	def isInside(self, curX, curY): # x,y: the current position of mouse
		lowerBoundX = self.cx - self.w/2
		upperBoundX = self.cx + self.w/2
		lowerBoundY = self.cy - self.h/2
		upperBoundY = self.cy + self.h/2
		return (lowerBoundX < curX < upperBoundX) and \
			(lowerBoundY < curY < upperBoundY)

	def promptChange(self):
		self.color = 'gold2'
		self.labCol = 'black'
	
	def changeBack(self):
		self.color = 'black'
		self.labCol = 'black'
		
	def magicPrompt(self, curX, curY):
		if self.isInside(curX, curY):
			self.promptChange()
		else:
			self.changeBack()

	def showButton(self,canvas):
		x, y = self.cx, self.cy
		halfW = self.w/2
		halfH = self.h/2
		color = self.color
		label = self.label
		labelColor = self.labCol
		canvas.create_rectangle(x-halfW, y-halfH, x+halfW, y+halfH, fill =color)
		canvas.create_text(x, y, text=label, fill = labelColor, font = 'impact 25')
		
		
		
class Control(Butt):
	def __init__(self,cx,cy,w,h,label):
		super().__init__(cx,cy,w,h,label)
		self.color = 'black'
		self.labCol = 'white'

	def promptChange(self):
		self.color = "white"
		self.labCol = "black"
	
	def changeBack(self):
		self.color = 'black'
		self.labCol = 'white'
		

class Elegant(Butt):
	def __init__(self,cx,cy,w,h,label):
		super().__init__(cx,cy,w,h,label)
		self.color = 'pale goldenrod'
		self.labCol = 'black'

	def promptChange(self):
		self.color = "goldenrod"
		self.labCol = "black"
	
	def changeBack(self):
		self.color = 'pale goldenrod'
		self.labCol = 'black'

class Bloody(Butt):
	def __init__(self,cx,cy,w,h,label):
		super().__init__(cx,cy,w,h,label)
		self.color = 'red4'
		self.labCol = 'black'

	def promptChange(self):
		self.color = "firebrick3"
		self.labCol = "black"
	
	def changeBack(self):
		self.color = 'red4'
		self.labCol = 'black'
		
				