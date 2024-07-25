FROM python:3.11.6
ENV PYTHONUNBUFFERED 1
WORKDIR /events

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /events/

CMD ["python", "app.py"]
