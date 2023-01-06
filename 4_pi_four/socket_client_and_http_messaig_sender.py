import socket
import requests
import urllib.request

while True:
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    sock.connect(("192.168.0.54", 12345))

    # Receive a response from the server
    data = sock.recv(1024)

    # Print the received data
    data = str(data)[2:-3]

    print(data)

    ola = str("http://192.168.0.55/" + data.replace(" ", "_"))

    get_url = urllib.request.urlopen(ola)

    sock.close()
