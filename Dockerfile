FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app     

WORKDIR /app

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

