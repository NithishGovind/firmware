
import socket
import serial

# Serial (Arduino)
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

# TCP Socket Server (Jetson)
HOST = ""   # listen on all interfaces
PORT = 5000 # choose any free port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Jetson Bridge Ready. Waiting for client...")
conn, addr = s.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1)  # read 1 byte
    if not data:
        break
    cmd = data.decode()
    if cmd in ["f","b","l","r","q","e","s"]:
        ser.write(cmd.encode())
        print("Sent to Arduino:", cmd)

conn.close()
