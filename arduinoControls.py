import serial 
import pyfirmata
from pyo import *
from generalDicts import *
from changeFunctions import *
import math

# File contains neccessary framework to process distance data from the arduino
# and translate that into pitch control.

  
# Framework for reading HC-SR04 data from http://www.toptechboy.com/arduino/python-with-ardiuno-3-example-using-ultrasonic-sensor/
arduinoSerialData = serial.Serial('/dev/cu.usbmodem14301',9600)
def getDist():
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        return float(myData)



def smoothNoise(pitchList):
    while len(pitchList) < 5:
        nextVal = getDist()
        if nextVal == None:
            continue
        pitchList.append(nextVal)
    return sum(pitchList)/len(pitchList)



def pitchSnap(data):
    avgSignal = smoothNoise([])
    for note in reversed(arduinoDataToFreqBin()):
        if avgSignal > note[1]:
            return note[0]



def scaleDataToPitch(signal):
    a = 15.88610173
    b = 0.0288113
    return a*math.exp(signal*b)
    

def runPitchSnap(data):
    curNote = pitchSnap(data)
    if curNote == None:
        data.pitch.stop()
        data.curHarmFilter.stop()
    else:
        noteDict = notes()
        for note in noteDict:
            if curNote == note:
                data.pitch.freq = noteDict[note]*2**data.curOctave
                changeHarm(data)
        if data.pitch.isOutputting != True:
            data.pitch.out()
            if data.curHarm != None:
                data.curHarmFilter.out()



def runThereNormal(data):
    avgSignal = smoothNoise([])
    if avgSignal > 30:
        data.pitch.stop()
        data.curHarmFilter.stop()
    else:
        curPitch = scaleDataToPitch(avgSignal)*2**data.curOctave
        data.pitch.freq = curPitch
        changeHarm(data)
        if data.pitch.isOutputting != True:
            data.pitch.out()
            if data.curHarm != None:
                data.curHarmFilter.out()