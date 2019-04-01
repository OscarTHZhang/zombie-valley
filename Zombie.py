'''
This is a .py file that contains class Zombie

Zombie has following properties:
0. prototype (image)
1. location (x,y)
2. HP
3. moving speed
4. isDie

Zombie can do following things:
0. show itself (canvas.create_image)
1. move
2. take hurt
3. hurt the player
'''
import random


class Zombie(object):
	
	def __init__(self, cx, cy, prototype):
		self.prototype = prototype
		self.cx = cx
		self.cy = cy
		self.HP = 100
		self.speed = 3
		self.isDead = False
		'''
		I assumed these values 
		they could be changed after further testing
		'''

	def showBody(self, canvas): # it will show the zombie's body
		canvas.create_image(self.cx, self.cy, image = self.prototype)

	def showHP(self, canvas): # it will show the zombie's HP stripe
		lx = self.cx - 40
		canvas.create_rectangle(lx, self.cy - 50, lx + 100, \
			self.cy - 60, fill = 'black')

		canvas.create_rectangle(lx, self.cy - 50, lx + self.HP, \
			self.cy -60, fill = 'red')

	def show(self, canvas):
		self.showBody(canvas)
		self.showHP(canvas)

	def move(self): # the zombie is moving left
		self.cx = self.cx - self.speed

	def takeHurt(self, hurt = 10):
		if not self.isDead:
			self.HP -= hurt
		if self.HP <= 0:
			self.isDead = True

