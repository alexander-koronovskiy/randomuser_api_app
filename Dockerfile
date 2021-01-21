FROM python:latest
MAINTAINER Alexander Koronovskiy 'alexander.koronovskiy.com'
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY app /app
WORKDIR /app
CMD python index.py
