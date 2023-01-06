from machine import Pin
from easy_comms import Easy_comms
from time import sleep

red = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)
blue = Pin(15, Pin.OUT)

com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

while True:
    message = com1.read()

    if message.lower() is not None:
        print(message)

    if message.lower() == "red on":
        red.on()
    if message.lower() == "red off":
        red.off()

    if message.lower() == "green on":
        green.on()
    if message.lower() == "green off":
        green.off()

    if message.lower() == "blue on":
        blue.on()
    if message.lower() == "blue off":
        blue.off()

    if message.lower() == "all on":
        red.on()
        green.on()
        blue.on()

    if message.lower() == "all off":
        blue.off()
        green.off()
        red.off()

    sleep(1)
