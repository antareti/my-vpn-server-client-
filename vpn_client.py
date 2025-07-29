import socket
from cryptography.fernet import Fernet

# 🔒 Тот же ключ, что и в сервере
key = b'paTGlZSG9bzHZ0yIdZyP9rExUuRvuKnU3ppY1Sy0PjQ='
cipher = Fernet(key)

client = socket.socket()
client.connect(('127.0.0.1', 12345))  # Укажи IP сервера, если не локально

msg = cipher.encrypt(b"ping from client")
client.send(msg)

data = client.recv(4096)
print(f"[SERVER]: {cipher.decrypt(data).decode()}")
