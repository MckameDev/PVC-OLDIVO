FROM python:3.11-slim

WORKDIR /app

# Copiar solo requirements para cachear instalación
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto para Gunicorn
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]