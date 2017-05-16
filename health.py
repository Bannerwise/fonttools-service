from datetime import datetime, timedelta
import psutil
import socket

def getHealth():
    totalMemory = psutil.virtual_memory().total / 1048576
    freeMemory = psutil.virtual_memory().available / 1048576
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())

    cpu = psutil.cpu_percent(interval=1)

    data = {
        'os': {
            'hostname': socket.gethostname()
            'memory': {
                'total': str(totalMemory) + ' MB' ,
                'free': str(freeMemory) + ' MB'
            }
        },
        'process': {
            'uptime': str(uptime.days) + " days"
        }
    }

    return data
