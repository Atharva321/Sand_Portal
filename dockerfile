FROM python:3.8-slim

ENV PATH="${PATH}:/home/admin/.local/bin"

RUN apt-get update && apt-get install libpq-dev build-essential -y && apt-get clean &&\
    rm -rf /usr/games && \
    mkdir -p  /usr/django_sand_portal

RUN  addgroup django && \
     adduser --disabled-password --ingroup django --gecos '' admin && \
     chown -R admin:django /usr/django_sand_portal 

COPY ./requirements.txt /usr/django_sand_portal/

WORKDIR /usr/django_sand_portal

USER admin

RUN pip install -r requirements.txt

COPY . /usr/django_sand_portal/

EXPOSE 8000

CMD ["python",  "manage.py",  "runserver",  "0.0.0.0:8000"]
