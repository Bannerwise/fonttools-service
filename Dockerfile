# FROM ubuntu:latest
# # ENV DEBIAN_FRONTEND noninteractive
#
# RUN \
#   apt-get update && \
#   apt-get -y upgrade && \
#   apt-get install -y python python-pip python-dev python-virtualenv gunicorn
#
# RUN mkdir -p /deploy/app
#
# COPY gunicorn_config.py /deploy/gunicorn_config.py
# COPY newrelic.ini /deploy/newrelic.ini
# COPY app /deploy/app
#
# RUN pip install -r /deploy/app/requirements.txt
# WORKDIR /deploy/app
#
# EXPOSE 9097
#
# ENTRYPOINT ["newrelic-admin", "run-program"]
# # Start gunicorn
# CMD ["/usr/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "app:app"]

FROM python:2

RUN mkdir -p /app

COPY newrelic.ini /app/newrelic.ini
COPY gunicorn_config.py /app/gunicorn_config.py
COPY requirements.txt /app/requirements.txt
COPY app /app

RUN pip install -r app/requirements.txt

WORKDIR /app

EXPOSE 9097

# ENTRYPOINT ["newrelic-admin", "run-program"]
# Start gunicorn
CMD ["newrelic-admin", "run-program", "gunicorn", "--config", "gunicorn_config.py", "app:app"]
