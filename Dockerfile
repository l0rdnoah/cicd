FROM python:3.9-slim
WORKDIR /cicd
COPY . .  
CMD ["python3", "app.py"]
