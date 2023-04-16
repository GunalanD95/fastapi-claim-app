FROM python:3.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fast_api_app fast_api_app

CMD ["uvicorn", "fast_api_app.main:app", "--host", "0.0.0.0", "--port", "8000"]