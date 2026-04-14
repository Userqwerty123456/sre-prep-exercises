#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'   # слушаем на всех доступных интерфейсах
PORT = 12345       # порт, который будет слушать бот

def main():
    # Создаем TCP-сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Разрешаем переиспользовать адрес (избавляет от ошибки Address already in use)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Чат-бот запущен на {HOST}:{PORT}")
        print("Ожидание подключений...")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Подключен клиент: {addr}")
                data = conn.recv(1024)
                if data:
                    message = data.decode('utf-8').strip()
                    print(f"Получено: {message}")
                    response = f"Echo: {message}"
                    conn.sendall(response.encode('utf-8'))
                else:
                    print("Клиент отправил пустые данные, закрываем соединение")
                # Соединение закроется автоматически при выходе из блока with

if __name__ == "__main__":
    main()
