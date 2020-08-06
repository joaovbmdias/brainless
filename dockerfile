# Brainless Dockerfile

FROM python:3.7

COPY /src /app

COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["brainless.py"]