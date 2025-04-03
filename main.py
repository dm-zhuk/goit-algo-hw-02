import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()


# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1000, 9999)  # Генерація унікального номера заявки
    print(f"Створено нову заявку з ID: {request_id}")
    request_queue.put(request_id)  # Додати заявку до черги


# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()  # Видалити заявку з черги
        print(f"Обробка заявки з ID: {request_id}")
    else:
        print("Черга пуста, немає заявок для обробки.")


# Головний цикл програми
def main():
    try:
        while True:
            generate_request()  # Створення нових заявок
            process_request()  # Обробка заявок
            time.sleep(2)  # Затримка для імітації часу обробки
    except KeyboardInterrupt:
        print("Програма зупинена.")


if __name__ == "__main__":
    main()
