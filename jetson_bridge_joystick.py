import pygame
import serial
import time
import threading

# ====== Serial (Arduino) ======
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
time.sleep(2)

# ====== Init pygame ======
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Controller:", joystick.get_name())

# ====== Shared state ======
target_left = 0
target_right = 0
current_left = 0
current_right = 0
lock = threading.Lock()

def scale_trigger(val, max_speed=190):
    # Xbox triggers are -1 at rest, +1 pressed
    return int(((val + 1) / 2) * max_speed)  # map -1→0, 1→max

# ====== Thread: Joystick Reader ======
def joystick_reader():
    global target_left, target_right
    while True:
        pygame.event.pump()

        left_trigger = joystick.get_axis(2)   # L2
        right_trigger = joystick.get_axis(5)  # R2

        with lock:
            target_left = scale_trigger(left_trigger)
            target_right = scale_trigger(right_trigger)

        time.sleep(0.01)

# ====== Thread: Serial Writer (smooth ramp) ======
def serial_writer():
    global current_left, current_right
    ramp_step = 10
    update_rate = 0.05

    while True:
        with lock:
            tl = target_left
            tr = target_right

        # Smooth ramp for left motor
        if current_left < tl:
            current_left = min(current_left + ramp_step, tl)
        elif current_left > tl:
            current_left = max(current_left - ramp_step, tl)

        # Smooth ramp for right motor
        if current_right < tr:
            current_right = min(current_right + ramp_step, tr)
        elif current_right > tr:
            current_right = max(current_right - ramp_step, tr)

        # Send "tank style" command → e.g., "M150,180"
        cmd = f"M{current_left},{current_right}\n"
        ser.write(cmd.encode())
        print("Sent:", cmd.strip())

        time.sleep(update_rate)

# ====== Start threads ======
t1 = threading.Thread(target=joystick_reader, daemon=True)
t2 = threading.Thread(target=serial_writer, daemon=True)

t1.start()
t2.start()

while True:
    time.sleep(1)
