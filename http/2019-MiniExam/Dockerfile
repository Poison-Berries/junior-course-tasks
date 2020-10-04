FROM python:3.8-alpine

COPY requirements.txt /requirements.txt
RUN ["/usr/local/bin/pip3", "install", "-Ur", "requirements.txt"]

WORKDIR /app
COPY http_exam.py /app/

ENTRYPOINT ["/usr/local/bin/python3", "http_exam.py"]
