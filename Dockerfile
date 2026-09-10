FROM python:3.12-slim

WORKDIR /app

# Копируем проект в контейнер
COPY . .

# Порт, который слушает приложение
EXPOSE 8000

# Запускаем лендинг
CMD ["python", "vpn.py"]
