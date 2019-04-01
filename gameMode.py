# __main__
# Modules and files to import
from tkinter import *
from Zombie import *
from Weapon import *
from buttonClass import *
import random
##############################

class gameMode(object):

    width, height = 800, 400

    # Model
    def __init__(self, temp):
        self.initImg()
        self.initButts()
        self.zomb = Zombie(gameMode.width, gameMode.height/2, self.zombImg)
        self.gunn = Gun(self.gunImg)
        
        diff = random.randint(50, 150)
        self.zombs = \
        [Zombie(gameMode.width+i*random.randint(200, 400),\
            random.choice(range(100, gameMode.height-100,50)), self.zombImg) for i in range(temp)]
        self.temp = temp

        self.bulls = []
        self.originNum = len(self.zombs)
        self.isReloading = False
        self.reload = 500
        self.HP = 1
        self.origin = self.HP

        # game status:
        self.isLost = False
        self.isWon = False
        self.isPause = False

    # bullet's position start at (135, data.gunn.cy - 7.5)

    def initImg(self): # initialize images for objects
        self.backImg = PhotoImage(file = 'img/background.gif')
        self.zombImg = PhotoImage(file = 'img/zombie.gif').subsample(3)
        self.gunImg = PhotoImage(file = 'img/gun.gif').subsample(10)
        self.bullImg = PhotoImage(file = 'img/bullet.gif').subsample(20)
        self.bombImg = PhotoImage(file = 'img/bomb.gif').subsample(10)

    def initButts(self):
        cx1, cx2, cy = gameMode.width/4, gameMode.width*3/4, gameMode.height*8/9
        self.pauseButt = Elegant(cx1,cy,100,50,"Pause")
        self.returnButt = Elegant(cx2,cy,100,50,"Stop")


    # Controller
    def mousePressed(self, event):
        if self.pauseButt.isInside(event.x, event.y) and self.isPause==False:
            self.isPause = True
            self.pauseButt.label = "Resume"
        elif self.pauseButt.isInside(event.x, event.y) and self.isPause==True:
            self.isPause = False
            self.pauseButt.label = "Pause"

        elif self.returnButt.isInside(event.x, event.y):
            return "Start"


    def mouseMoved(self, event):
        self.pauseButt.magicPrompt(event.x, event.y)
        self.returnButt.magicPrompt(event.x, event.y)

    def keyPressed(self, event):
        self.gunn.keyController(event.keysym)
        if event.keysym == 's':
            self.bulls.append(Bullet(123, self.gunn.cy-7.5, self.bullImg))
        elif (event.keysym == 'b' and self.isReloading == False):
            # release a bomb
            self.bulls.append(Bomb(123, self.gunn.cy-7.5, self.bombImg))
            self.isReloading = True
            self.reload = 500
            
    def timerFired(self):
        if not self.isPause:
            for zomb in self.zombs:
                zomb.move()
                if zomb.cx <= 0:
                    self.HP -= 1
                    self.zombs.remove(zomb)

            for bul in self.bulls:
                bul.move()
                if bul.cx > gameMode.width: self.bulls.remove(bul)

            if len(self.bulls)>0 and len(self.zombs)>0:
            # check if the bullet hit the monster
                for bul in self.bulls:
                    for zomb in self.zombs:
                        d = ((bul.cx - zomb.cx)**2 + (bul.cy - zomb.cy)**2)**0.5
                        if d <= 30:
                            try: self.bulls.remove(bul)
                            except: pass
                            # data.zombs.remove(zomb)
                            zomb.takeHurt()
                            if isinstance(bul, Bomb): bul.explode(self.zombs)
                            if zomb.isDead: self.zombs.remove(zomb)
                        else:
                            # nothing
                            pass
            # check game status
            if len(self.zombs) == 0: return 'Win'
            elif self.HP == 0: return 'Lose'
            if self.isReloading and self.reload != 0:
                self.reload = (self.reload - 1) % 500
            if self.reload == 0:
                self.reload = 500
                self.isReloading = False

    # Viewer
    def redrawAll(self, canvas):
        # draw in canvas
        self.drawBackground(canvas)
        self.showButts(canvas)
        self.gunn.show(canvas)
        for zomb in self.zombs:
            zomb.show(canvas)
        for bul in self.bulls:
            bul.show(canvas)
        self.showReload(canvas)

        canvas.create_text(gameMode.width/2, 20, \
            text = 'Number of Monsters left %d/%d' %(len(self.zombs), self.originNum), \
            fill = 'dark red', font = 'impact 30')


    def drawBackground(self, canvas):
        canvas.create_image(gameMode.width/2, gameMode.height/2, image = self.backImg)

    def showButts(self, canvas):
        self.pauseButt.showButton(canvas)
        self.returnButt.showButton(canvas)

    def showReload(self, canvas):
        if self.isReloading == True:
            canvas.create_text(gameMode.width/2, gameMode.height*9/10, fill = 'red3',\
                text='Time for reload bomb: %d' %(self.reload), font = 'impact 20')
