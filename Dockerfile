FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5000
ENTRYPOINT flask run --host=0.0.0.0
