FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN chmod +x wait-for-it.sh
RUN pip install --no-cache-dir -r requirements.txt

# ✅ DB가 열릴 때까지 기다리고, Flask 앱 실행
CMD ["./wait-for-it.sh", "db:3306", "--", "python", "app.py"]