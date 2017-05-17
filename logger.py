import logging
from logentries import LogentriesHandler
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('settings.ini')
API_KEY = config.get('logentries', 'key')

log = logging.getLogger('logentries')
log.setLevel(logging.DEBUG)

log.addHandler(LogentriesHandler(API_KEY))
