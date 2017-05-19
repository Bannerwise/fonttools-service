FROM ubuntu:latest
# ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python python-pip python-dev python-virtualenv gunicorn

RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
RUN pip install -r /deploy/app/requirements.txt
WORKDIR /deploy/app

EXPOSE 9097
ENTRYPOINT ["/usr/local/bin/newrelic-admin", "run-program"]
# Start gunicorn
CMD ["/usr/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "app:app"]
