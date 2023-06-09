FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","src/app.py"]

