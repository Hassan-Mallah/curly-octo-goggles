FROM python:3.11.6
ENV PYTHONUNBUFFERED 1
WORKDIR /odds

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /odds/

CMD ["python", "app.py"]

