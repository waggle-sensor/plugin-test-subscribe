FROM python:3.8
WORKDIR /app
COPY main.py main.py
ENTRYPOINT ["python3", "main.py"]
