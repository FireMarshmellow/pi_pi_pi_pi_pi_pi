import requests
from bs4 import BeautifulSoup
from time import sleep
import serial

ser = serial.Serial("/dev/ttyS0", 9600)
last_string = ""


while True:
    response = requests.get('http://192.168.0.27:5000/display')
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    print(text)
    new_string = text+"\r"
    if last_string.lower() == new_string.lower():
        pass
    else:
        ser.write(new_string.encode())

    last_string = new_string
    
    sleep(1)

ser.close()