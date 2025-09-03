import pygame
import serial
import time
import threading

# ====== Serial (Arduino) ======
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
time.sleep(2)  # wait for Arduino reset

# ====== Init pygame for Xbox controller ======
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Controller:", joystick.get_name())

# ====== Shared variable between threads ======
current_cmd = "s0"
lock = threading.Lock()

# ====== Helper: map joystick axis to motor speed ======
def scale_speed(value, max_speed=255):
    # joystick -1.0 → 1.0 → 0–255
    return int(abs(value) * max_speed)

# ====== Thread: Joystick Reader ======
def joystick_reader():
    global current_cmd
    deadband = 0.2
    
    while True:
        pygame.event.pump()  # process events

        x_axis = joystick.get_axis(3)  # right stick X
        y_axis = joystick.get_axis(4)  # right stick Y

        new_cmd = "s0"  # default stop

        if abs(y_axis) > abs(x_axis):  # forward/back takes priority
            if y_axis < -deadband:
                new_cmd = f"f{scale_speed(y_axis)}"
            elif y_axis > deadband:
                new_cmd = f"b{scale_speed(y_axis)}"
        else:  # left/right
            if x_axis < -deadband:
                new_cmd = f"l{scale_speed(x_axis)}"
            elif x_axis > deadband:
                new_cmd = f"r{scale_speed(x_axis)}"

        # Update shared variable
        with lock:
            current_cmd = new_cmd

        time.sleep(0.01)  # polling rate

# ====== Thread: Serial Writer ======
def serial_writer():
    last_cmd = ""
    while True:
        with lock:
            cmd = current_cmd

        if cmd != last_cmd:  # only send when changed
            ser.write((cmd + "\n").encode())  # add newline
            print("Sent to Arduino:", cmd)
            last_cmd = cmd

        time.sleep(0.05)  # steady sending rate

# ====== Start threads ======
t1 = threading.Thread(target=joystick_reader, daemon=True)
t2 = threading.Thread(target=serial_writer, daemon=True)

t1.start()
t2.start()

# Keep main alive
while True:
    time.sleep(1)
