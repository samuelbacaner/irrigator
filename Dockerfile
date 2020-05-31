FROM balenalib/raspberrypi4-64-debian-python:3-sid

RUN apt-get update \
  && apt-get install -y gcc python3-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT python -m src.run