import psutil
import platform
import multiprocessing
import socket


def get_base_machine_info():
    """When called various interesting statistics about the machine are returned

        Currently this includes: hostname, cpu percentage, total ram, CPU name, number of cores the CPU has
    """
    return {
        # TODO: Consider making this an object
        'hostname': socket.gethostname(),
        'cpu_percent_used': psutil.cpu_percent(1),
        'ram': psutil.virtual_memory().total,
        'cpu': platform.processor(),
        'cpu_cores': multiprocessing.cpu_count()
    }

