from pyo import *
from generalDicts import *
from tkinter import *

# File contains framework for changin certain audio signal attributes

# Note: not all functions that change attributes are in this file, as some
# produced errors when importing and exist in __init__.py

# Note: The server is booted in this file so that loopFunctions.py and 
# __init__.py reference the same server


s = Server(duplex = 1).boot()



def changeWaveType(data, waveType):
    curFreq = data.pitch.freq
    data.pitch = waveType(curFreq,  mul = 0.6)
    data.curFilter = Biquadx(data.pitch, type = data.curFilterType).out()
    data.curWaveType = waveType
    if data.curHarm != None:
        curHarmFreq = data.curHarm.freq
        data.curHarm = waveType(curHarmFreq, mul = 0.4)
        data.curHarmFilter = Biquadx(data.curHarm, type = data.curFilterType).out()



def changeNote(data, pitch):
    noteDict = notes()
    for note in noteDict:
        if pitch == note:
            data.pitch.setFreq(noteDict[note]*2**data.curOctave)
            data.curFilter = Biquadx(data.pitch, type = data.curFilterType).out()
            changeHarm(data)


def changeHarm(data):
    if data.curHarm != None:
        data.curHarm.freq = data.pitch.freq*data.curHarmFactor
        


def numPadKeyboard(data, event):
    if event.keysym == "1":
        changeNote(data, "C")
    elif event.keysym == "2":
        changeNote(data, "D")
    elif event.keysym == "3":
        changeNote(data, "E")
    elif event.keysym == "4":
        changeNote(data, "F")
    elif event.keysym == "5":
        changeNote(data, "G")
    elif event.keysym == "6":
        changeNote(data, "A")
    elif event.keysym == "7":
        changeNote(data, "B")
    elif event.keysym == "8":
        changeNote(data, "C2")
