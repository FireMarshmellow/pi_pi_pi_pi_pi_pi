import serial
import socket

ser = serial.Serial("/dev/ttyS0", 9600)

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port
sock.bind(("192.168.0.54", 12345))

# Listen for incoming connections
sock.listen(1)


while True:
    message = ser.read_until(b"\r")
    print(str(message)[2:-3])
    conn, addr = sock.accept()
    conn.send(message)
    conn.close()

ser.close()
