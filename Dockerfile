FROM python:2.7

RUN mkdir -p /app

COPY newrelic.ini /app/newrelic.ini
COPY settings.ini /app/settings.ini
COPY gunicorn_config.py /app/gunicorn_config.py
COPY requirements.txt /app/requirements.txt
COPY app /app

RUN pip install -r app/requirements.txt

WORKDIR /app
RUN mkdir -p /tmp

EXPOSE 9097

# Start gunicorn
CMD ["newrelic-admin", "run-program", "gunicorn", "--config", "gunicorn_config.py", "app:app"]
