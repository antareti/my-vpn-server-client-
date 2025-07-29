import socket
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox, scrolledtext

# 🔑 Тот же ключ, что и у сервера
key = b'paTGlZSG9bzHZ0yIdZyP9rExUuRvuKnU3ppY1Sy0PjQ='
cipher = Fernet(key)

# === Логика VPN-клиента ===
def connect_to_server():
    ip = ip_entry.get()
    log_text.delete(1.0, tk.END)

    try:
        log_text.insert(tk.END, f"🔌 Подключение к {ip}:12345...\n")
        client = socket.socket()
        client.connect((ip, 12345))

        msg = cipher.encrypt(b"ping from GUI client")
        client.send(msg)

        data = client.recv(4096)
        decrypted = cipher.decrypt(data).decode()

        log_text.insert(tk.END, f"📨 Получено (расшифровано): {decrypted}\n")
        client.close()

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось подключиться:\n{str(e)}")

# === GUI ===
root = tk.Tk()
root.title("VPN-клиент (Python GUI)")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="IP сервера:").pack(pady=5)
ip_entry = tk.Entry(root, width=30)
ip_entry.pack()
ip_entry.insert(0, "127.0.0.1")

tk.Button(root, text="Подключиться", command=connect_to_server).pack(pady=10)

log_text = scrolledtext.ScrolledText(root, width=45, height=10)
log_text.pack(padx=10, pady=5)

root.mainloop()
