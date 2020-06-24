from graphics import Point,Rectangle,Text
from time import time,localtime

def main():
    win = GraphWin('Face', 300, 200)
    frame = Rectangle(Point(20, 20), Point(280, 180))
    frame.config['width'] = 10
    frame.draw(win)

    label = Text(Point(158, 188), '')
    label.setFace("times roman")
    label.setFill("red")
    label.setSize(25)
    label.setStyle("bold")
    label.draw(win)

    t = time.localtime()
    curent_time = time.strfttime('%H:%M:%S', t)
    updateTimeDisplay(timeDisplayText, totalseconds)
    
    def updateTimeDisplay(timeDisplayText, totalseconds):
        for seconds in range(totalseconds, 43200, 1):
            timeText = getTimeString(seconds)
            timeDisplayText.setText(timeText)
            time.sleep(1)

def getTimeString():
    timeString = time.strfttime('%I:%M:%S %p', localtime)
    return timeString

main() 