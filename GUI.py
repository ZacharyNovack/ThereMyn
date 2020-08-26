from generalDicts import *
from pyo import *
from changeFunctions import *
from clickFunctions import *


# Contains framework for creating TherMyn's GUI 



### Loop Button Coloring Functions
def setLoop1Color(canvas, data, cx, cy, r):
    if data.loop1IsRec == True and data.loopMetIn.get("tap") < data.loopLength:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "yellow", width = 0)
    elif data.loop1 != None and data.loop1Full != False and \
    data.loop1.isPlaying() == False:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "red", width = 0)
    elif data.loop1 != None and data.loop1Full != False and \
    data.loop1.isOutputting() == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "green2", width = 0)
    elif data.loop1Full == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan", width = 0)
    else:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white", width = 0)

def setLoop2Color(canvas, data, cx, cy, r):
    if data.loop2IsRec == True and data.loopMetIn.get("tap") < data.loopLength:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "yellow", width = 0)
    elif data.loop2 != None and data.loop2Full != False and \
    data.loop2.isPlaying() == False:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "red", width = 0)
    elif data.loop2 != None and data.loop2Full != False and \
    data.loop2.isOutputting() == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "green2", width = 0)
    elif data.loop2Full == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan", width = 0)
    else:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white", width = 0)

def setLoop3Color(canvas, data, cx, cy, r):
    if data.loop3IsRec == True and data.loopMetIn.get("tap") < data.loopLength:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "yellow", width = 0)
    elif data.loop3 != None and data.loop3Full != False and \
    data.loop3.isPlaying() == False:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "red", width = 0)
    elif data.loop3 != None and data.loop3Full != False and \
    data.loop3.isOutputting() == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "green2", width = 0)
    elif data.loop3Full == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan", width = 0)
    else:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white", width = 0)

def setLoop4Color(canvas, data, cx, cy, r):
    if data.loop4IsRec == True and data.loopMetIn.get("tap") < data.loopLength:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "yellow", width = 0)
    elif data.loop4 != None and data.loop4Full != False and \
    data.loop4.isPlaying() == False:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "red", width = 0)
    elif data.loop4 != None and data.loop4Full != False and \
    data.loop4.isOutputting() == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "green2", width = 0)
    elif data.loop4Full == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan", width = 0)
    else:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white", width = 0)




### Main GUI functions
def drawConsole(canvas, data):
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
        if button == "ThereMyn":
            if data.thereControl == False:
                canvas.create_text(data.width/2, (y1+y2)/2, text = button,
                font = "Courier 30", fill = "red", anchor = "e")
                canvas.create_rectangle(x1, y1, x2, y2, width = 2)
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "On",
                font = "Courier 30", fill = "green2")
                canvas.create_rectangle(x3, y3, x4, y4, width = 2,
                outline = "red")
                canvas.create_text((x3+x4)/2, (y3+y4)/2, text = "Off",
                font = "Courier 30", fill = "red")
            else:
                canvas.create_text(data.width/2, (y1+y2)/2, text = button,
                font = "Courier 30", fill = "green2", anchor = "e")
                canvas.create_rectangle(x1, y1, x2, y2, width = 2,
                outline = "green2")
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "On",
                font = "Courier 30", fill = "green2")
                canvas.create_rectangle(x3, y3, x4, y4, width = 2)
                canvas.create_text((x3+x4)/2, (y3+y4)/2, text = "Off",
                font = "Courier 30", fill = "red")
        if button == "Pitch Snap":
            if data.pitchSnap == False:
                canvas.create_text(data.width/2, (y1+y2)/2, text = button,
                font = "Courier 30", fill = "red", anchor = "e")
                canvas.create_rectangle(x1, y1, x2, y2, width = 2)
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "On",
                font = "Courier 30", fill = "green2")
                canvas.create_rectangle(x3, y3, x4, y4, width = 2,
                outline = "red")
                canvas.create_text((x3+x4)/2, (y3+y4)/2, text = "Off",
                font = "Courier 30", fill = "red")
            else:
                canvas.create_text(data.width/2, (y1+y2)/2, text = button,
                font = "Courier 30", fill = "green2", anchor = "e")
                canvas.create_rectangle(x1, y1, x2, y2, width = 2,
                outline = "green2")
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "On",
                font = "Courier 30", fill = "green2")
                canvas.create_rectangle(x3, y3, x4, y4, width = 2)
                canvas.create_text((x3+x4)/2, (y3+y4)/2, text = "Off",
                font = "Courier 30", fill = "red")





def drawNumConsole(canvas, data):
    consoleDict = numConsoleDimensions(data)
    for button in consoleDict:
        x1 = consoleDict[button][0]
        y1 = consoleDict[button][1]+4
        x2 = consoleDict[button][2]
        y2 = consoleDict[button][3]-4
        canvas.create_text(data.width/2, (y1+y2)/2, text = button,
        font = "Courier 30", fill = "white", anchor = "e")
        if button == "Octave":
            if data.numConSelect == button:
                canvas.create_rectangle(x1, y1, x2, y2, width = 2,
                outline = "cyan")
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = str(data.curOctave),
                font = "Courier 30", fill = "cyan")
            else:
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = str(data.curOctave),
                font = "Courier 30", fill = "white")
        if button == "BPM":
            if data.numConSelect == button:
                canvas.create_rectangle(x1, y1, x2, y2, width = 2,
                outline = "cyan")
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = str(data.BPM),
                font = "Courier 30", fill = "cyan")
            else:
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = str(data.BPM),
                font = "Courier 30", fill = "white")
        if button == "Loop Length":
            if data.numConSelect == button:
                canvas.create_rectangle(x1, y1, x2, y2, width = 2,
                outline = "cyan")
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = str(data.loopLength),
                font = "Courier 30", fill = "cyan")
            else:
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = str(data.loopLength),
                font = "Courier 30", fill = "white")
    


def drawLoopButtons(canvas, data):
    buttonDict = loopDimensions(data)
    for button in buttonDict:
        cx = buttonDict[button][0]
        cy = buttonDict[button][1]
        r = buttonDict[button][2]
        x1 = buttonDict[button][3]
        y1 = buttonDict[button][4]
        x2 = buttonDict[button][5]
        y2 = buttonDict[button][6]
        name = button
        set
        if name == "loop1":
            setLoop1Color(canvas, data, cx, cy, r)
        elif name == "loop2":
            setLoop2Color(canvas, data, cx, cy, r)
        elif name == "loop3":
            setLoop3Color(canvas, data, cx, cy, r)
        elif name == "loop4":
            setLoop4Color(canvas, data, cx, cy, r)
        canvas.create_text(cx, cy-20, text = name, fill = "black",
        font="Courier 30")
        canvas.create_rectangle(x1, y1, x2, y2, fill = "green2", width = 2)
        canvas.create_text(cx-r/2, y1+15, text = "Play!", font="Courier 16")
        canvas.create_rectangle(x2, y1, x2+r, y2, fill = "red", width = 2)
        canvas.create_text(cx+r/2, y1+15, text = "Pause!", font="Courier 16")
    pass




def drawFilterButtons(canvas, data):
    buttonDict = filterDimensions(data)
    canvas.create_text(1.5*data.width/14, data.height/3+15, text = "Filter",
    font = "Courier 40 underline italic", fill = "white")
    for button in buttonDict:
        cx = buttonDict[button][0]
        cy = buttonDict[button][1]
        r = buttonDict[button][2]
        filterType = buttonDict[button][3]
        name = button
        if filterType == data.curFilterType:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan1", 
            width = 0)
            canvas.create_text(cx, cy, text = name, fill = "black",
            font="Courier 14")
        else:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white")
            canvas.create_text(cx, cy, text = name, fill = "black",
            font="Courier 14")




def drawWaveButtons(canvas, data):
    buttonDict = buttonDimensions(data)
    canvas.create_text(1.5*data.width/14, data.height/18, text = "Waveform",
    font = "Courier 40 underline italic", fill = "white")
    for button in buttonDict:
        cx = buttonDict[button][0]
        cy = buttonDict[button][1]
        r = buttonDict[button][2]
        name = buttonDict[button][3]
        if button == data.curWaveType:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan1", 
            width = 0)
            canvas.create_text(cx, cy, text = name, fill = "black",
            font="Courier 16")
        else:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white")
            canvas.create_text(cx, cy, text = name, fill = "black",
            font="Courier 16")


def drawHarmButtons(canvas, data):
    buttonDict = harmonizerDimensions(data)
    canvas.create_text(data.width-1.5*data.width/14, data.height/18,
    text = "Harmonizer", font = "Courier 40 underline italic", fill = "white")
    for button in buttonDict:
        cx = buttonDict[button][0]
        cy = buttonDict[button][1]
        r = buttonDict[button][2]
        if button == data.curHarmString:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "cyan1", 
            width = 0)
            canvas.create_text(cx, cy, text = button, fill = "black",
            font="Courier 16")
        else:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "white")
            canvas.create_text(cx, cy, text = button, fill = "black",
            font="Courier 16")


def drawMet(canvas, data):
    metList = metDimensions(data)
    cx = metList[0]
    cy = metList[1]
    r = metList[2]
    if data.metroOut.isOutputting() == True:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "green2", width = 0)
    else:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "red", width = 0)
    canvas.create_text(cx, cy-15, text = "Metronome", fill = "black", font="Courier 16")
    canvas.create_text(cx, cy+10, text = str(data.BPM), fill = "black", font="Courier 16")


def drawMetCounter(canvas, data):
    if data.loop1IsRec == True:
        if data.loopMetIn.get("tap") == data.loopLength:
            canvas.create_text(data.width/8, 3*data.height/4+20,
            text = "Done!", font = "Courier 30")
            data.loopMetOut.stop()
        elif data.loopMetIn.get("tap") > data.loopLength:
            data.loop1IsRec = False
        else:
            canvas.create_text(data.width/8, 3*data.height/4+20,
            text = str(int(data.loopMetIn.get("tap")+1)), font = "Courier 30")
    if data.loop2IsRec == True:
        if data.loopMetIn.get("tap") == data.loopLength:
            canvas.create_text(3*data.width/8, 3*data.height/4+20,
            text = "Done!", font = "Courier 30")
            data.loopMetOut.stop()
        elif data.loopMetIn.get("tap") > data.loopLength:
            data.loop2IsRec = False
        else:
            canvas.create_text(3*data.width/8, 3*data.height/4+20,
            text = str(int(data.loopMetIn.get("tap")+1)), font = "Courier 30")
    if data.loop3IsRec == True:
        if data.loopMetIn.get("tap") == data.loopLength:
            canvas.create_text(5*data.width/8, 3*data.height/4+20,
            text = "Done!", font = "Courier 30")
            data.loopMetOut.stop()
        elif data.loopMetIn.get("tap") > data.loopLength:
            data.loop3IsRec = False
        else:
            canvas.create_text(5*data.width/8, 3*data.height/4+20,
            text = str(int(data.loopMetIn.get("tap")+1)), font = "Courier 30")
    if data.loop4IsRec == True:
        if data.loopMetIn.get("tap") == data.loopLength:
            canvas.create_text(7*data.width/8, 3*data.height/4+20,
            text = "Done!", font = "Courier 30")
            data.loopMetOut.stop()
        elif data.loopMetIn.get("tap") > data.loopLength:
            data.loop4IsRec = False
        else:
            canvas.create_text(7*data.width/8, 3*data.height/4+20,
            text = str(int(data.loopMetIn.get("tap")+1)), font = "Courier 30")


def makeGUI(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black", 
    width = 0)
    canvas.create_text(data.width/2, data.height/26, anchor = "n", fill = "yellow",
    text = "- - - Press enter to start/stop the audio stream - - -",
    font = "Courier 14 italic")
    canvas.create_text(data.width/2, 3.75*data.height/26, anchor = "n", fill = "yellow",
    text = "- - - Use numkeys 1-8 for pitch when ThereMyn is Off! - - -",
    font = "Courier 14 italic")
    canvas.create_text(data.width/2, data.height/18, anchor = "n", fill = "white",
    text = "Welcome to ThereMyn!", font = "arial 58 bold italic")
    drawWaveButtons(canvas, data)
    drawLoopButtons(canvas, data)
    drawFilterButtons(canvas, data)
    drawHarmButtons(canvas, data)
    drawConsole(canvas, data)
    drawNumConsole(canvas, data)
    drawMet(canvas, data)
    drawMetCounter(canvas, data)

