# Dockerfile (dev/simple)
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# copy app
COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/main.py"]
