from __future__ import division
from arduinoControls import *
from changeFunctions import *
from clickFunctions import *
from loopFunctions import *
from generalDicts import *
from GUI import *
from tkinter import *
from pyo import *
import os
import threading
import pyfirmata
import serial
import time
####################################
# Non-importable/Extraneous Functions:
# These functions resulted in errors when being used from other files and thus
# exist in the main __init__ file
####################################




def startSound(data):
    s.start()


def stopSound(data):
    s.stop()




# https://www.cs.cmu.edu/~112/notes/notes-debugging-and-testing.html
def isPrime(n):
    if (n < 2): return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True


def setLoopMetLength(data):
    if isPrime(data.loopLength+3) == True and data.loopLength+3 > 10:
        data.loopMetIn = Beat(time=60/data.BPM, taps=data.loopLength+4,
        w1=100, w2=100, w3=100, onlyonce = True)
    else:
        data.loopMetIn = Beat(time=60/data.BPM, taps=data.loopLength+3,
        w1=100, w2=100, w3=100, onlyonce = True)
    data.loopMetOut.setMul(data.loopMetIn) 



def numConsoleIncrease(data):
    if data.numConSelect == "Octave":
        if data.curOctave < 10:
            data.curOctave += 1
            data.pitch.freq *= 2
    elif data.numConSelect == "BPM":
        if data.loop1IsRec == True or data.loop2IsRec == True or \
        data.loop2IsRec == True or data.loop3IsRec == True:
            pass
        elif data.BPM < 400:
            data.BPM += 5
            data.metroIn.setTime(60/data.BPM)
            data.loopMetIn.setTime(60/data.BPM)
    else:
        if data.loop1IsRec == True or data.loop2IsRec == True or \
        data.loop2IsRec == True or data.loop3IsRec == True:
            pass
        else:
            data.loopLength += 1
            setLoopMetLength(data)


def numConsoleDecrease(data):
    if data.numConSelect == "Octave":
        if data.curOctave > 0:
            data.curOctave -= 1
            data.pitch.freq /= 2
    elif data.numConSelect == "BPM":
        if data.loop1IsRec == True or data.loop2IsRec == True or \
        data.loop2IsRec == True or data.loop3IsRec == True:
            pass
        elif data.BPM > 50:
            data.BPM -= 5
            data.metroIn.setTime(60/data.BPM)
            data.loopMetIn.setTime(60/data.BPM)
    else:
        if data.loop1IsRec == True or data.loop2IsRec == True or \
        data.loop2IsRec == True or data.loop3IsRec == True:
            pass
        elif data.loopLength > 1:
            data.loopLength -= 1
            setLoopMetLength(data)

####################################
# Main Tkinter framework
####################################


def init(data):
    data.pitch = Sine(440, mul = 0.6)
    data.curHarm = None
    data.curHarmString = None
    data.curHarmFactor = None
    data.curOctave = 4
    data.curWaveType = Sine
    data.curFilter = Biquadx(data.pitch, type = 4).out()
    data.curHarmFilter = Biquadx(data.pitch, type = 4)
    data.curFilterType = 4
    data.BPM = 120
    data.loopLength = 4
    data.loopTime = convertBPMToTime(data)
    data.metroIn = Metro(time=60/data.BPM).play()
    data.metroOut = RCOsc(freq=220, mul=data.metroIn)
    data.loopMetIn = Beat(time=60/data.BPM, taps=data.loopLength+3,
    w1=100, w2=100, w3=100, onlyonce = True).play()
    data.loopMetOut = RCOsc(freq=220, mul=data.loopMetIn)
    data.loopMetIsPrime = False
    data.filterDict = {0: "Low-Pass", 1: "High-Pass", 4: "No Filter!"}
    data.thereControl = data.pitchSnap = False
    data.numConSelect = "Octave"
    data.loop1 = data.loop2 = data.loop3 = data.loop4 = None
    data.loop1IsRec = data.loop2IsRec = data.loop3IsRec = data.loop4IsRec = False
    data.loop1Full = data.loop2Full = data.loop3Full = data.loop4Full = False
    startSound(data)
    pass



def mousePressed(event, data):
    waveMousePressed(event, data)
    filterMousePressed(event, data)
    metMousePressed(event, data)
    harmMousePressed(event, data)
    consoleMousePressed(event, data)
    numConsoleMousePressed(event, data)
    loopMousePressed(event, data)
    pass



def timerFired(data):
    data.loopTime = convertBPMToTime(data)
    if data.thereControl == True:
        if data.pitchSnap == True:
            runPitchSnap(data)
        else:
            runThereNormal(data)
    pass



def keyPressed(event, data):
    if event.keysym == "Return":
        if s.getIsStarted() == 1:
            stopSound(data)
        else:
            startSound(data)
    elif event.keysym == "Up":
        numConsoleIncrease(data)
    elif event.keysym == "Down":
        numConsoleDecrease(data)
    elif data.thereControl == False:
        numPadKeyboard(data, event)


def redrawAll(canvas, data):
    makeGUI(canvas, data)
    pass

####################################
# Run function taken from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
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
    data.timerDelay = 1 # milliseconds
    root = Tk()

    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Thanks for playing!")

run(1200, 800)
s.stop()