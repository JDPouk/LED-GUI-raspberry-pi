from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPI.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
led = LED(14)

## gUI defintions 
win = Tk()
win.title("LEDs")
myFont = tkiner.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event fucntions
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "Turn LED on"
    else:
        led.on()
        ledButton
        

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
    
## Widgets
ledButton = Button(win, text = 'Turn LED on', font = myFont , command = ledToggle, bg='bisque2', height = 1, width = 24 )
ledButton.grid(row=0,colum=1)

exitButton = Button(win, text = 'Turn LED on', font = myFont , command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=0,colum=1)

win.protrocal("WM_Delete_window", close)

win.mainloop()