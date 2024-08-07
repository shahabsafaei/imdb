FROM python:3.12.4-alpine3.20

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --dev

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]