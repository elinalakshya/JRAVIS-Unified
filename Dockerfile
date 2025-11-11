FROM node:20-slim AS frontend
WORKDIR /app
COPY app/package*.json ./ 
RUN npm install --force
COPY app/ .
RUN npm run build

FROM python:3.10-slim
WORKDIR /app
COPY dashboard_api/requirements.txt .
RUN pip install -r requirements.txt
COPY dashboard_api ./dashboard_api
COPY --from=frontend /app/.next ./frontend
COPY --from=frontend /app/public ./frontend/public
ENV PORT=8000
CMD ["python", "dashboard_api/main.py"]

# === FRONTEND BUILD STAGE ===
FROM node:20-slim AS frontend
WORKDIR /frontend

COPY app/package*.json ./app/
WORKDIR /frontend/app
RUN npm install --force
COPY app/ ./
RUN npm run build

# === BACKEND BUILD STAGE ===
FROM python:3.10-slim AS backend
WORKDIR /app

COPY dashboard_api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dashboard_api ./dashboard_api
COPY --from=frontend /frontend/app/.next ./frontend
COPY --from=frontend /frontend/app/public ./frontend/public

EXPOSE 8000
CMD ["uvicorn", "dashboard_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
