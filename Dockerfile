# Используем официальный легкий образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта в контейнер
COPY . .

# Открываем порт, который будет слушать приложение
EXPOSE 8000

# Переменная окружения для Gunicorn
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8000 --workers=4 --access-logfile=-"

# Запускаем приложение с помощью Gunicorn
# Указываем главный файл app и экземпляр приложения (app:app)
CMD ["gunicorn", "app:app"]
