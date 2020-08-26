from generalDicts import *
from pyo import *
from changeFunctions import *
from loopFunctions import *


# File contains mousePressed framework for each clickable object in the GUI


def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2 - y1)**2)**0.5



def waveMousePressed(event, data):
    waveButtonDict = buttonDimensions(data)
    for button in waveButtonDict:
        cx = waveButtonDict[button][0]
        cy = waveButtonDict[button][1]
        r = waveButtonDict[button][2]
        if distance(event.x, event.y, cx, cy) < r:
            data.pitch.stop()
            changeWaveType(data, button)



def filterMousePressed(event, data):
    filterButtonDict = filterDimensions(data)
    for button in filterButtonDict:
        cx = filterButtonDict[button][0]
        cy = filterButtonDict[button][1]
        r = filterButtonDict[button][2]
        filterType = filterButtonDict[button][3]
        if distance(event.x, event.y, cx, cy) < r:
            data.curFilter.setType(filterType)
            data.curFilterType = filterType


def metMousePressed(event, data):
    metList = metDimensions(data)
    metCX = metList[0]
    metCY = metList[1]
    metR = metList[2]
    if distance(event.x, event.y, metCX, metCY) < metR:
        if data.metroOut.isOutputting() != True:
            data.metroOut.out()
        else:
            data.metroOut.stop()


def harmMousePressed(event, data):
    harmDict = harmonizerDimensions(data)
    for button in harmDict:
        cx = harmDict[button][0]
        cy = harmDict[button][1]
        r = harmDict[button][2]
        ratio = harmDict[button][3]
        if distance(event.x, event.y, cx, cy) < r:
            if data.curHarmString != button:
                data.curHarmFactor = ratio
                data.curHarmString = button
                data.curHarm = data.curWaveType(data.pitch.freq*ratio, mul = 0.6)
                data.curHarmFilter = Biquadx(data.curHarm,
                type = data.curFilterType).out()
            else:
                data.curHarmFilter.stop()
                data.curHarm = None
                data.curHarmString = None



def consoleMousePressed(event, data):
    consoleDict = mainConsoleDimensions(data)
    for button in consoleDict:
        x1 = consoleDict[button][0]
        y1 = consoleDict[button][1]+4
        x2 = consoleDict[button][2]
        y2 = consoleDict[button][3]-4
        x3 = consoleDict[button][4]
        y3 = consoleDict[button][5]+4
        x4 = consoleDict[button][6]
        y4 = consoleDict[button][7]-4
        if y1 < event.y < y2:
            if x1 < event.x < x2:
                if button == "ThereMyn":
                    data.thereControl = True
                    data.curHarm = None
                    data.curHarmFilter.stop()
                    data.curHarmString = None
                else:
                    data.pitchSnap = True
        if y3 < event.y < y4:
            if x3 < event.x < x4:      
                if button == "ThereMyn":
                    data.thereControl = False
                else:
                    data.pitchSnap = False


def numConsoleMousePressed(event, data):
    numConsoleDict = numConsoleDimensions(data)
    for button in numConsoleDict:
        x1 = numConsoleDict[button][0]
        y1 = numConsoleDict[button][1]+4
        x2 = numConsoleDict[button][2]
        y2 = numConsoleDict[button][3]-4
        if y1 < event.y < y2:
            if x1 < event.x < x2:
                data.numConSelect = button



def loopMousePressed(event, data):
    loopButtonDict = loopDimensions(data)
    for button in loopButtonDict:
        cx = loopButtonDict[button][0]
        cy = loopButtonDict[button][1]
        r = loopButtonDict[button][2]
        playLeft = loopButtonDict[button][3]
        timeTop = loopButtonDict[button][4]
        playRight = loopButtonDict[button][5]
        timeBottom = loopButtonDict[button][6]
        pauseLeft = playRight
        pauseRight = playRight+r
        if button == "loop1":
            if distance(event.x, event.y, cx, cy) < r:
                if data.loop2IsRec == True or data.loop3IsRec == True or \
                data.loop4IsRec == True:
                    continue
                loop1Button(data)
            elif timeTop < event.y < timeBottom:
                print("yeet")
                if data.loop1IsRec == True or data.loop1Full == False:
                    continue
                loop1Play(event, data, playLeft, playRight)
                loop1Pause(event, data, pauseLeft, pauseRight)
        elif button == "loop2":
            if distance(event.x, event.y, cx, cy) < r:
                if data.loop1IsRec == True or data.loop3IsRec == True or \
                data.loop4IsRec == True:
                    continue
                else: loop2Button(data)
            elif timeTop < event.y < timeBottom:
                if data.loop2IsRec == True or data.loop2Full == False:
                    continue
                loop2Play(event, data, playLeft, playRight)
                loop2Pause(event, data, pauseLeft, pauseRight)
        elif button == "loop3":
            if distance(event.x, event.y, cx, cy) < r:
                if data.loop2IsRec == True or data.loop1IsRec == True or \
                data.loop4IsRec == True:
                    continue
                else: loop3Button(data)
            elif timeTop < event.y < timeBottom:
                if data.loop3IsRec == True or data.loop3Full == False:
                    continue
                loop3Play(event, data, playLeft, playRight)
                loop3Pause(event, data, pauseLeft, pauseRight)
        elif button == "loop4":
            if distance(event.x, event.y, cx, cy) < r:
                if data.loop2IsRec == True or data.loop1IsRec == True or \
                data.loop3IsRec == True:
                    continue
                else: loop4Button(data)
            elif timeTop < event.y < timeBottom:
                if data.loop4IsRec == True:
                    continue
                loop4Play(event, data, playLeft, playRight)
                loop4Pause(event, data, pauseLeft, pauseRight)
    


