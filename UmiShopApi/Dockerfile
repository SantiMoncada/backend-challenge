FROM python:3.10.6

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py migrate --run-syncdb && python manage.py runserver 0.0.0.0:8000