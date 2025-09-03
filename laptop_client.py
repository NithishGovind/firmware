# laptop_client.py
import socket

JETSON_IP = "192.168.137.118"  # replace with Jetson Nano's IP
PORT = 5000

# WASD mapping to Arduino commands
key_map = {
    "w": "f",   # forward
    "x": "b",   # backward
    "a": "l",   # left
    "d": "r",   # right
    "q": "q",   # spin left
    "e": "e",   # spin right
    "s": "s",   # stop
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((JETSON_IP, PORT))

print("Connected to robot!")
print("Controls:")
print("  w = forward")
print("  x = backward")
print("  a = left")
print("  d = right")
print("  q = spin left")
print("  e = spin right")
print("  s = stop")
print("  z = exit")

while True:
    cmd = input("Enter command: ").lower().strip()
    if cmd == "z":
        break
    if cmd in key_map:
        s.send(key_map[cmd].encode())
        print(f"Sent command: {cmd} -> {key_map[cmd]}")
    else:
        print("Invalid key, use w/a/s/d/x/q/e or z to quit")

s.close()
