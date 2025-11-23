FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE 8000

<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]

=======
CMD ["uvicorn", "jravis_brain:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
