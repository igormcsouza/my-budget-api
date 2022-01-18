FROM python:3.8-slim

RUN useradd -ms /bin/bash user
WORKDIR /home/user

ENV VIRTUAL_ENV=.venv

USER user

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY project/ project/

CMD gunicorn app:app --bind 0.0.0.0:8000