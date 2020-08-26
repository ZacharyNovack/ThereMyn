from __future__ import division
from Tkinter import *
from pyo import *
from generalDicts import *
import os
import threading
import time
from changeFunctions import *

# Contains framework for recording, playing, and pausing loops.



def convertBPMToTime(data):
    secondsPerBeat = 60/data.BPM
    return secondsPerBeat*(data.loopLength)



# General concept for creating file from server used from E-Pyo example
# 04-record-perf.py
def createLoopFile(loopTime, loopNum):
    path = os.path.join(os.path.expanduser("~"), "Desktop", "%s.aif" % loopNum)
    s.recordOptions(dur=-1, filename=path, fileformat=1, sampletype=1)
    s.recstart()
    time.sleep(loopTime)
    s.recstop()
    print("Loop Finished!")



### Loop Run functions
# Concept for running sound files as tables from E-Pyo example
# 03-read-from-ram.py
def runLoop1(data):
    path = os.path.join(os.path.expanduser("~"), "Desktop" + "/loop1.aif")
    loopAsFile = SndTable(path)
    freq = loopAsFile.getRate()
    if data.loop1 != None and data.loop1.isPlaying() == False:
        data.loop1 = Osc(table=loopAsFile, freq=freq, mul = 0.4)
    else:
        data.loop1 = Osc(table=loopAsFile, freq=freq, mul = 0.4).out()
        pass 
    data.curFilter = Biquadx(data.pitch, type = data.curFilterType).out()
    
def runLoop2(data):
    path = os.path.join(os.path.expanduser("~"), "Desktop" + "/loop2.aif")
    loopAsFile = SndTable(path)
    freq = loopAsFile.getRate()
    if data.loop2 != None and data.loop2.isPlaying() == False:
        data.loop2 = Osc(table=loopAsFile, freq=freq, mul = 0.4)
    else: data.loop2 = Osc(table=loopAsFile, freq=freq, mul = 0.4).out()
    data.curFilter = Biquadx(data.pitch, type = data.curFilterType).out()
    
def runLoop3(data):
    path = os.path.join(os.path.expanduser("~"), "Desktop" + "/loop3.aif")
    loopAsFile = SndTable(path)
    freq = loopAsFile.getRate()
    if data.loop3 != None and data.loop3.isPlaying() == False:
        data.loop3 = Osc(table=loopAsFile, freq=freq, mul = 0.4)
    else: data.loop3 = Osc(table=loopAsFile, freq=freq, mul = 0.4).out()
    data.curFilter = Biquadx(data.pitch, type = data.curFilterType).out()
    
def runLoop4(data):
    path = os.path.join(os.path.expanduser("~"), "Desktop" + "/loop4.aif")
    loopAsFile = SndTable(path)
    freq = loopAsFile.getRate()
    if data.loop4 != None and data.loop4.isPlaying() == False:
        data.loop4 = Osc(table=loopAsFile, freq=freq, mul = 0.4)
    else: data.loop4 = Osc(table=loopAsFile, freq=freq, mul = 0.4).out()
    data.curFilter = Biquadx(data.pitch, type = data.curFilterType).out()
    



### Main Loop Button Functions
def loop1Button(data):
    if data.loop1 != None:
        data.loop1.stop()
    data.loop1 = None
    loopTime = data.loopTime
    t = threading.Thread(target = createLoopFile, args = (loopTime, "loop1"))
    t.start()
    if data.loopMetIn.isPlaying() == True:
        data.loopMetIn.stop()
    data.loopMetIn.play()
    data.loopMetOut.out()
    data.loop1IsRec = True
    data.loop1Full = True


def loop2Button(data):
    if data.loop2 != None:
        data.loop2.stop()
    data.loop2 = None
    loopTime = data.loopTime
    t = threading.Thread(target = createLoopFile, args = (loopTime, "loop2"))
    t.start()
    if data.loopMetIn.isPlaying() == True:
        data.loopMetIn.stop()
    data.loopMetIn.play()
    data.loopMetOut.out()
    data.loop2IsRec = True

    data.loop2Full = True

def loop3Button(data):
    if data.loop3 != None:
        data.loop3.stop()
    data.loop3 = None
    loopTime = data.loopTime
    t = threading.Thread(target = createLoopFile, args = (loopTime, "loop3"))
    t.start()
    if data.loopMetIn.isPlaying() == True:
        data.loopMetIn.stop()
    data.loopMetIn.play()
    data.loopMetOut.out()
    data.loop3IsRec = True

    data.loop3Full = True

def loop4Button(data):
    if data.loop4 != None:
        data.loop4.stop()
    data.loop4 = None
    loopTime = data.loopTime
    t = threading.Thread(target = createLoopFile, args = (loopTime, "loop4"))
    t.start()
    if data.loopMetIn.isPlaying() == True:
        data.loopMetIn.stop()
    data.loopMetIn.play()
    data.loopMetOut.out()
    data.loop4IsRec = True

    data.loop4Full = True



### Loop Play Functions
def loop1Play(event, data, playLeft, playRight):
    if playLeft < event.x < playRight:
        if data.loop1 != None and data.loop1.isPlaying() == False:
            data.loop1.out()
        elif data.loop1 == None:
            runLoop1(data)
        elif data.loop2 != None:
            runLoop2(data)
        elif data.loop3 != None:
            runLoop3(data)
        elif data.loop4 != None:
            runLoop4(data)
            

def loop2Play(event, data, playLeft, playRight):
    if playLeft < event.x < playRight:
        if data.loop2 != None and data.loop2.isPlaying() == False:
            data.loop2.out()
        elif data.loop2 == None:
            runLoop2(data)
        elif data.loop1 != None:
            runLoop1(data)
        elif data.loop3 != None:
            runLoop3(data)
        elif data.loop4 != None:
            runLoop4(data)

def loop3Play(event, data, playLeft, playRight):
    if playLeft < event.x < playRight:
        if data.loop3 != None and data.loop3.isPlaying() == False:
            data.loop3.out()
        elif data.loop3 == None:
            runLoop3(data)
        elif data.loop2 != None:
            runLoop2(data)
        elif data.loop1 != None:
            runLoop1(data)
        elif data.loop4 != None:
            runLoop4(data)

def loop4Play(event, data, playLeft, playRight):
    if playLeft < event.x < playRight:
        if data.loop4 != None and data.loop4.isPlaying() == False:
            data.loop4.out()
        elif data.loop4 == None:
            runLoop4(data)
        elif data.loop2 != None:
            runLoop2(data)
        elif data.loop3 != None:
            runLoop3(data)
        elif data.loop1 != None:
            runLoop1(data)





### Loop Pause Functions
def loop1Pause(event, data, pauseLeft, pauseRight):
    if pauseLeft < event.x < pauseRight:
        if data.loop1 != None and data.loop1.isPlaying() == True:
            data.loop1.stop()

def loop2Pause(event, data, pauseLeft, pauseRight):
    if pauseLeft < event.x < pauseRight:
        if data.loop2 != None and data.loop2.isPlaying() == True:
            data.loop2.stop()

def loop3Pause(event, data, pauseLeft, pauseRight):
    if pauseLeft < event.x < pauseRight:
        if data.loop3 != None and data.loop3.isPlaying() == True:
            data.loop3.stop()

def loop4Pause(event, data, pauseLeft, pauseRight):
    if pauseLeft < event.x < pauseRight:
        if data.loop4 != None and data.loop4.isPlaying() == True:
            data.loop4.stop()


