# laptop_client.py
import socket

JETSON_IP = "192.168.1.50"  # replace with your Jetson Nano's IP
PORT = 5000

# Map WASD keys to robot commands
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
print("Controls: w=forward, x=backward, a=left, d=right, q=spin left, e=spin right, s=stop, z=exit")

while True:
    cmd = input("Enter command: ").lower()
    if cmd == "z":   # exit program
        break
    if cmd in key_map:
        s.send(key_map[cmd].encode())
        print(f"Sent {cmd} -> {key_map[cmd]}")
    else:
        print("Invalid key, use w/a/s/d/x/q/e")
        
s.close()
