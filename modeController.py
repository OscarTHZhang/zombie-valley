'''
Main program
'''
from tkinter import *
from startMode import *
from typeMode import *
from gameMode import *
from winMode import *
from loseMode import *
import sys
import webbrowser

def init(data):
	data.curMode = startMode();root.geometry("600x600")

def mousePressed(event, data):
	message = data.curMode.mousePressed(event)
	if message == "Quit": root.quit();root.destroy();sys.exit()
	elif message == "Help": webbrowser.open("https://oscarthzhang.github.io/")
	elif message == "Type": data.curMode = typeMode();root.geometry("600x600")
	elif isinstance(message, tuple): data.curMode = gameMode(message[1]);root.geometry("800x400")
	elif message == "Start": data.curMode = startMode();root.geometry("600x600")

# geometry: https://stackoverflow.com/questions/13327659/python-tkinter-attempt-to-get-widget-size

def mouseMoved(event, data):
	data.curMode.mouseMoved(event)

def keyPressed(event, data):
	data.curMode.keyPressed(event)

def timerFired(data):
	message = data.curMode.timerFired()
	if message == 'Win': data.curMode = winMode()
	elif message == 'Lose': data.curMode = loseMode()


def redrawAll(canvas, data):
	data.curMode.redrawAll(canvas)

###############################################################################
# Run function
def run(width=800, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def mouseMovedWrapper(event, canvas, data):
    	mouseMoved(event, data)
    	redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    # create the root and the canvas
    global root # globalize root; bad style !
    root = Tk()
    root.title("Zombie Valley")
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
    						mouseMovedWrapper(event, canvas, data))
    init(data)
    timerFiredWrapper(canvas, data)

    root.mainloop()  # blocks until window is closed
    print("bye!")

run()
