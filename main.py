from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=863000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
    data = s.recv(64)
    if data == b'Ping':
        s.send('Pong')
        print("got ping")
    else:
        print(data)
    time.sleep_ms(500)
