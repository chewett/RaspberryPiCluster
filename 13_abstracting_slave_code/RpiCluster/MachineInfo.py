import psutil
import platform
import multiprocessing
import socket


def get_base_machine_info():
    return {
        'hostname': socket.gethostname(),
        'cpu_percent_used': psutil.cpu_percent(1),
        'ram': psutil.virtual_memory().total,
        'cpu': platform.processor(),
        'cpu_cores': multiprocessing.cpu_count()
    }

