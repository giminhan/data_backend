FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /data/

RUN apt-get update && apt-get -y install libpq-dev
RUN apt-get install -y netcat

COPY requirements.txt /data/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /data/

# static file 
RUN python manage.py collectstatic --no-input