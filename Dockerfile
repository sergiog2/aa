FROM python:3.10.8-slim-bullseye

COPY main.py /app/

CMD ["python", "/app/main.py"]