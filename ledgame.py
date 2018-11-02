#this is a "lights-out" game using three LED bulbs connected to the Raspberry Pi's GPIO board
#toggling a switch will affect adjacent switches
#player wins when all 3 lights are switched off

from gpiozero import LED
import time

led1 = LED(17)
led2 = LED(16)
led3 = LED(21)

while True:
    print("Welcome to the led game")
    time.sleep(1)
    print("try to turn off all the lights")
    time.sleep(1)

    for i in range(0,3):
        led1.on()
        time.sleep(.2)
        led2.on()
        led1.off()
        time.sleep(.2)
        led2.off()
        led3.on()
        time.sleep(.2)
        led3.off()

    led1.on()
    led2.off()
    led3.on()

   
    while led1.is_active == True or led2.is_active == True or led3.is_active == True:

        x = input("flip switch 1, 2, or 3? ")
        
        if x == "1" and led1.is_active == True:
            led1.off()
            if led2.is_active == True:
                led2.off()
                continue
            elif led2.is_active == False:
                led2.on()
                continue

        if x == "1" and led1.is_active == False:
            led1.on()
            if led2.is_active == True:
                led2.off()
            elif led2.is_active == False:
                led2.on()
                continue

        elif x == "2" and led2.is_active == True:
            led2.off()
            if led3.is_active == True:
                led3.off()
            elif led3.is_active == False:
                led3.on()
            if led1.is_active == True:
                led1.off()
            elif led1.is_active == False:
                led1.on()
                continue

        elif x == "2" and led2.is_active == False:
            led2.on()
            if led3.is_active == True:
                led3.off()
            elif led3.is_active == False:
                led3.on()
            if led1.is_active == True:
                led1.off()
            elif led1.is_active == False:
                led1.on()
                continue

        elif x == "3" and led3.is_active == True:
            led3.off()
            if led2.is_active == True:
                led2.off()
            elif led2.is_active == False:
                led2.on()
                continue

        elif x == "3" and led3.is_active == False:
            led3.on()
            if led2.is_active == True:
                led2.off()
            elif led2.is_active == False:
                led2.on()
                continue

        else:
            print("invalid input")
            continue

    print("You Won!")
    time.sleep(1)

    for i in range(0,20):
        led1.on()
        time.sleep(.05)
        led2.on()
        led1.off()
        time.sleep(.05)
        led2.off()
        led3.on()
        time.sleep(.05)
        led3.off()
    break
