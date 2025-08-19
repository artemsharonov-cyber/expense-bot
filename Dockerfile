# Используем стабильный образ Python 3.11
FROM python:3.11-slim

# Устанавливаем необходимые системные зависимости для сборки aiohttp
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаём рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt .
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду запуска бота
CMD ["python", "main.py"]
