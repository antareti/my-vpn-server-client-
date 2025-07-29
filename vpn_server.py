import socket
from cryptography.fernet import Fernet

# 🔒 Постоянный ключ (одинаковый в клиенте и сервере)
key = b'paTGlZSG9bzHZ0yIdZyP9rExUuRvuKnU3ppY1Sy0PjQ='
cipher = Fernet(key)

server = socket.socket()
server.bind(('0.0.0.0', 12345))
server.listen(1)
print("[*] Сервер запущен и ждёт подключения на порту 12345...")
conn, addr = server.accept()
print(f"[*] Подключился клиент: {addr}")

while True:
    data = conn.recv(4096)
    if not data:
        break
    decrypted = cipher.decrypt(data)
    print(f"[CLIENT]: {decrypted.decode()}")
    response = cipher.encrypt(b"pong from server")
    conn.send(response)
