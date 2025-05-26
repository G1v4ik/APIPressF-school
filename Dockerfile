FROM python:3.12.8

WORKDIR /api

COPY . .

RUN pip install -r 'req.txt'


CMD ["python", "main.py"]