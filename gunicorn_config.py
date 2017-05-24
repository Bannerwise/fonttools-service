bind = "0.0.0.0:9097"
workers = 2
proxy_protocol = True
# worker_class = 'sync'
# worker_connections = 1000
# timeout = 1000
# keepalive = 5
# limit_request_line = 0
# limit_request_field_size = 0

errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
