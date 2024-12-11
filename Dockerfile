FROM python

RUN apt update && apt install libpq-dev -y

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN pip install -r requirements/prod.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
