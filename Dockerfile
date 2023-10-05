
FROM python:3.9-slim-buster

WORKDIR /app

RUN python -m venv ssv_env
ENV PATH="ssv_env/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "ssv.wsgi:application", "--bind", "0.0.0.0:8080" ]