FROM python:3.12

WORKDIR /queryembed

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

CMD ["python","run", "src/main.py"]
