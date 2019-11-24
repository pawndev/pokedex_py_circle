FROM python:3.7.1

LABEL maintainer="coquelet.c@gmail.com"
LABEL name="pokedexPY"


ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP="app.py"
ENV FLASK_ENV="development"
ENV FLASK_DEBUG=True

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0
