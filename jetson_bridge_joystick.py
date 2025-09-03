import pygame
import serial
import time
import threading

# Serial (Arduino)
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
time.sleep(2)  # wait for Arduino reset

# Init pygame for Xbox controller
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Controller:", joystick.get_name())

# Shared variable
current_cmd = "s"
lock = threading.Lock()

def joystick_reader():
    global current_cmd
    deadband = 0.2
    
    while True:
        pygame.event.pump()  # process events

        x_axis = joystick.get_axis(3)  # right stick X
        y_axis = joystick.get_axis(4)  # right stick Y

        new_cmd = "s"
        if abs(y_axis) > abs(x_axis):  # forward/back priority
            if y_axis < -deadband:
                new_cmd = "f"
            elif y_axis > deadband:
                new_cmd = "b"
        else:  # left/right
            if x_axis < -deadband:
                new_cmd = "l"
            elif x_axis > deadband:
                new_cmd = "r"

        # Update shared command
        with lock:
            current_cmd = new_cmd
        
        time.sleep(0.01)  # fast polling

def serial_writer():
    last_cmd = ""
    while True:
        with lock:
            cmd = current_cmd

        if cmd != last_cmd:  # only send if changed
            ser.write(cmd.encode())
            print("Sent to Arduino:", cmd)
            last_cmd = cmd

        time.sleep(0.05)  # steady sending rate

# Start threads
t1 = threading.Thread(target=joystick_reader, daemon=True)
t2 = threading.Thread(target=serial_writer, daemon=True)

t1.start()
t2.start()

# Keep main alive
while True:
    time.sleep(1)
