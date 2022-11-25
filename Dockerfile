FROM python:3.10-slim-bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential default-libmysqlclient-dev \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY /src /app 

EXPOSE 5002

CMD [ "uwsgi", "--http", "0.0.0.0:5002", \
               "--workers", "4", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi-file","wsgi.py"]