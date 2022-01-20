FROM python:3.8-alpine
RUN apk add --no-cache git && pip3 install -U pip
WORKDIR /app
COPY main.py main.py
ENTRYPOINT ["python3", "main.py"]
