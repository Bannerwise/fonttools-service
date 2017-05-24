bind = "0.0.0.0:9097"
workers = 1
worker_class = 'sync'
worker_connections = 1000
timeout = 100
keepalive = 2

errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
