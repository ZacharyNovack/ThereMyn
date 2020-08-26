from __future__ import division
from pyo import *

# Contains auxiliary dictionaries/lists that are utilized by other files for
# GUI creation and pitch control


def notes():
    freqDict = {"C": 16.35160, "C#": 17.32391, "D": 18.35405, "Eb": 19.44544,
    "E": 20.60172, "F": 21.82676, "F#": 23.12465, "G": 24.49971, "Ab": 25.95654,
    "A": 27.5, "Bb": 29.13524, "B": 30.86771, "C2": 32.70320}
    return freqDict


def buttonDimensions(data):
    buttonDict = {SuperSaw: [data.width/14, data.height/10+30, data.width/32, "Saw"],
    Sine: [data.width/7, data.height/10+30, data.width/32, "Sine"],
    Blit: [data.width/14, data.height/4.5+30, data.width/32, "Blit"],
    SumOsc: [data.width/7, data.height/4.5+30, data.width/32, "SumOsc"]}
    return buttonDict
    
    
def arduinoDataToFreqBin():
    dataList = [["C", 1.000], ["C#", 3.000], ["D", 5.000], ["Eb", 7.000], 
    ["E", 9.000], ["F", 11.000], ["F#", 13.000], ["G", 15.000], 
    ["Ab", 17.000], ["A", 19.000], ["Bb", 21.000], ["B", 23.000],
    ["C2", 25.000], [None, 27.000]]
    return dataList


def loopDimensions(data):
    loopButtonDict = {"loop1": [data.width/8, 3*data.height/4, data.width/16,
    data.width/8-data.width/16, 3*data.height/4+data.width/16+30, data.width/8,
    3*data.height/4+data.width/16+60, data],
    "loop2": [3*data.width/8, 3*data.height/4, data.width/16,
    3*data.width/8-data.width/16, 3*data.height/4+data.width/16+30,
    3*data.width/8, 3*data.height/4+data.width/16+60],
    "loop3": [5*data.width/8, 3*data.height/4, data.width/16, 
    5*data.width/8-data.width/16, 3*data.height/4+data.width/16+30,
    5*data.width/8, 3*data.height/4+data.width/16+60],
    "loop4": [7*data.width/8, 3*data.height/4, data.width/16,
    7*data.width/8-data.width/16, 3*data.height/4+data.width/16+30,
    7*data.width/8, 3*data.height/4+data.width/16+60]}
    return loopButtonDict


def filterDimensions(data):
    filterDict = {"Low-Pass": [data.width/14, data.height/3+80, data.width/32, 0],
    "High-Pass": [data.width/7, data.height/3+80, data.width/32, 1],
    "None": [data.width/14, data.height/2+40, data.width/32, 4]}
    return filterDict


def mainConsoleDimensions(data):
    consoleDict = {"ThereMyn": [data.width/2+data.width/40, data.height/6,
    3*data.width/5, data.height/6+40, 3*data.width/5+data.width/40, data.height/6,
    7*data.width/10, data.height/6+40], "Pitch Snap": [data.width/2+data.width/40,
    data.height/6+40,3*data.width/5, data.height/6+80, 3*data.width/5+data.width/40,
    data.height/6+40, 7*data.width/10, data.height/6+80]}
    return consoleDict

def numConsoleDimensions(data):
    numConDict = {"Octave": [data.width/2+data.width/40, data.height/6+100,
    3*data.width/5, data.height/6+140], "BPM": [data.width/2+data.width/40, data.height/6+140,
    3*data.width/5, data.height/6+180], "Loop Length": [data.width/2+data.width/40, data.height/6+180,
    3*data.width/5, data.height/6+220]}
    return numConDict


def harmonizerDimensions(data):
    harmDict = {"+Octave": [data.width-data.width/14, data.height/10+30,
    data.width/32, 2],
    "-Octave": [data.width-data.width/7, data.height/10+30, data.width/32, 0.5],
    "Fifth": [data.width-data.width/14, data.height/4.5+30, data.width/32, 3/2],
    "Fourth": [data.width-data.width/7, data.height/4.5+30, data.width/32, 4/3],
    "M3": [data.width-data.width/14, 2*data.height/4.5-50, data.width/32, 5/4],
    "m3": [data.width-data.width/7, 2*data.height/4.5-50, data.width/32, 6/5],
    "M6": [data.width-data.width/14, 3*data.height/4.5-130, data.width/32, 5/3],
    "m6": [data.width-data.width/7, 3*data.height/4.5-130, data.width/32,8/5]}
    return harmDict



def metDimensions(data):
    return [data.width/2, 3*data.height/5-20, data.width/20]
    