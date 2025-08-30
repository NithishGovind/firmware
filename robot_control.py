import serial
import time

# Change COM port for Windows (e.g., "COM3") or Linux/Mac (e.g., "/dev/ttyUSB0")
ser = serial.Serial("COM3", 115200, timeout=1)
time.sleep(2)  # wait for Arduino reset

print("Control Robot: f=forward, b=backward, l=left, r=right, q=spin left, e=spin right, s=stop, x=exit")

while True:
    cmd = input("Enter command: ")
    if cmd == "x":
        break
    if cmd in ["f", "b", "l", "r", "q", "e", "s"]:
        ser.write(cmd.encode())
