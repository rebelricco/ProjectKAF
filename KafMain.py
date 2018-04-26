import time
import smbus
import json
import ActualCoffeMachine.DoStuff as Do
import os
from RPi import GPIO

# WARME SENSOR SKLA VÆRE PÅ 60, SÅ SLUKKER KAFFEMASKINEN

while(True):
    getTimeSettingsFile = open("settings.KAF", "r+");
    rawJsonStringFromSettingsFile = getTimeSettingsFile.read();
    getTimeSettingsFile.close();
    parsedJsonFile = json.loads(rawJsonStringFromSettingsFile);

    getDelayedTime = open("settings.KAF", "r+");
    rawJsonStringFromDelayedTime = getDelayedTime.read();
    getDelayedTime.close();
    parsedDelayedTimeJson = json.loads(rawJsonStringFromDelayedTime);

    if(time.strftime("%H:%M") == parsedJsonFile['time']):
        print("ITS COFFEE TIME");
        Do.lav_kaffe(parsedJsonFile['kopper']);
    if(time.strftime("%H:%M") == parsedJsonFile['time']):
        print("ITS DELAYED COFFEE TIME");
        Do.lav_kaffe(parsedDelayedTimeJson['Kop'])
        os.remove("delayed.KAF");


    print("OK")
    time.sleep(10);