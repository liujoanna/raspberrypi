#!/usr/bin/env python
"""
Code that allows selection of varios functions on boot.
SWITCH1 = Radio
SWITCH2 = Trains
"""
import humble
import piplayer
import jukebox
import trains
import time
import os

BIGBUTTON = 2

def main():
    humble.init()
    hdt = humble.HumbleDisplayThread(humble.data)
    hdt.start()
    humble.data.setLine(0,"Select Function")
    humble.data.setLine(1,"1:Music;2:Trains")
    while (True):
        if humble.switch(0):
            time.sleep(0.2)
            carryOn = True
            while (carryOn):
                humble.data.setLine(0,"Select Function")
                humble.data.setLine(1,"1:Radio;2:Jukebox")
                time.sleep(0.2)
                if humble.switch(0):
                    piplayer.doStuff()
                    humble.data.setLine(0,"Select Function")
                    humble.data.setLine(1,"1:Music;2:Trains")
                if humble.switch(1):
                    jukebox.doStuff()
                    humble.data.setLine(0,"Select Function")
                    humble.data.setLine(1,"1:Radio;2:Jukebox")
                if humble.switch(2):
                    carryOn = False
                    time.sleep(0.2)
                time.sleep(0.2)
            humble.data.setLine(0,"Select Function")
            humble.data.setLine(1,"1:Music;2:Trains")
            time.sleep(0.2)
        if humble.switch(1):
            time.sleep(0.1)
            trains.doStuff()
            humble.data.setLine(0,"Select Function")
            humble.data.setLine(1,"1:Music;2:Trains")
            time.sleep(0.2)
        if humble.switch(2):
            time.sleep(BIGBUTTON)
            if (humble.switch(2)):
                humble.data.setLine(1, "")
                humble.scroll(0, "Shutting Down...")
                humble.data.setLine(0, "Shutting Down...")
                humble.data.setLine(0, "")
                os.system("sudo halt")
        time.sleep(0.1)
    hdt.done()
    
if __name__ == '__main__':
  main()
