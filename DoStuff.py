import time
import smbus
from RPi import GPIO
import ActualCoffeMachine.SpinnerMotorSpin as MotorSpin
import json

GPIO.cleanup();
GPIO.setmode(GPIO.BCM)

on_off_relay = 15;
CoffeeServo = 14;
RemovePowderServo1 = 27;
RemovePowderServo2 = 22;
WaterValve = 17;

GPIO.setup(on_off_relay, GPIO.OUT);
GPIO.setup(CoffeeServo, GPIO.OUT)
GPIO.setup(RemovePowderServo1, GPIO.OUT)
GPIO.setup(RemovePowderServo2, GPIO.OUT)
GPIO.setup(WaterValve, GPIO.OUT)








def AddWater(kopper):
    GPIO.output(WaterValve, 1);
    time.sleep(1);
    GPIO.output(WaterValve, 0);


def RemovePowder():
    Motorspinner = MotorSpin.Spinner

    Motorspinner.SpinClockWise(Motorspinner, RemovePowderServo1);
    time.sleep(3);
    Motorspinner.SpinClockWise(Motorspinner, RemovePowderServo2);
    time.sleep(3);
    Motorspinner.SpinCounterClockWise(Motorspinner, RemovePowderServo2);
    time.sleep(3);
    Motorspinner.SpinCounterClockWise(Motorspinner, RemovePowderServo1);
    time.sleep(3);


def AddPowder(cups):
    getState = open("State.KAF", "r+");
    rawJsonStringFromState = getState.read();
    getState.close();
    parsedState = json.loads(rawJsonStringFromState);

    State = int(parsedState['State']);

    Motorspinner = MotorSpin.Spinner
    j = 0
    while (j < cups):
        if (State % 2 == 0):
            Motorspinner.SpinCounterClockWise(Motorspinner, 14)
        else:
            Motorspinner.SpinClockWise(Motorspinner, 14)
        j += 1
        State += 1
        time.sleep(2)

        setting_file = open("State.KAF", "w+");
        json.dump(State, setting_file);
        setting_file.close();


def lav_kaffe(kopper):
    intcups = int(kopper);

    #RemovePowder();
    AddPowder(intcups);

    AddWater(intcups);


    # TÆND RELÆ
    GPIO.output(on_off_relay, 1);

    bus = smbus.SMBus(1)
    bus.write_byte(0x48, 0x00)

    kaf = True;
    while (kaf):
        reading = bus.read_byte(0x48)
        print(reading)
        if(reading < 190):
            #SLUK RELÆ
            GPIO.output(on_off_relay, 0);
            print("COFFEE DONE");
            kaf = False;
        time.sleep(0.5)

    return "KAF IS DONE " + str(intcups);





