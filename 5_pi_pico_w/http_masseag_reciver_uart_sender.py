import time
import network
import socket
from machine import Pin
from easy_comms import Easy_comms
from time import sleep


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID", "PASSWord")

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("waiting for connection...")
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError("network connection failed")
else:
    print("Connected")
    status = wlan.ifconfig()
    print("ip = " + status[0])


# Open socket
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("listening on", addr)


com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

last_string = ""

# Listen for connections, serve client
while True:
    try:
        cl, addr = s.accept()
        print("client connected from", addr)
        request = cl.recv(1024)
        message = request.decode().split("\n")[0][5:-10].replace("_", " ")
        print(message)

        new_string = message + "\r"
        if last_string.lower() == new_string.lower():
            pass

        else:
            com1.send(message)

        last_string = new_string

        sleep(1)

        cl.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
        cl.close()

    except OSError as e:
        cl.close()
        print("connection closed")
