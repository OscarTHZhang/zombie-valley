'''
This is a .py file that contains class Gun and Bullet

...
'''

class Gun(object):

	def __init__(self, prototype):
		self.cx = 0
		self.cy = 200
		self.prototype = prototype

	def show(self, canvas):
		canvas.create_image(self.cx, self.cy, image = self.prototype)

	def keyController(self, key): 
	# player press some key to control some actions of the gun
		if key == 'Up':
			self.moveUp()

		elif key == 'Down':
			self.moveDown()
		
		#elif key == 's':
		#	self.shoot()
			
	def moveUp(self):
		if self.cy >= 20:
			self.cy -= 10

	def moveDown(self):
		if self.cy <= 400:
			self.cy += 10

	#def shoot(self): This can be written into main


class Bullet(object):

	def __init__(self, cx, cy, prototype):
		self.cx = cx
		self.cy = cy
		self.prototype = prototype

	def show(self, canvas):
		canvas.create_image(self.cx, self.cy, image = self.prototype)

	def move(self):
		self.cx += 10
		
class Bomb(Bullet):

	def __init__(self, cx, cy, prototype):
		super().__init__(cx, cy, prototype)
		prototype = self.prototype # redefine a diff img

	def explode(self, zombs):
		# show an explosion animation
		# monster list contains a list of monster class
		for zomb in zombs:
			d = ((self.cx - zomb.cx)**2 + (self.cy - zomb.cy)**2)**0.5
			# calculate zomb and bullet distance
			if d <= 100:
				zomb.takeHurt(50)

	