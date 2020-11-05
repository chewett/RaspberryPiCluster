import psutil
import platform
import multiprocessing
import socket


def get_node_baseinfo():
    """When called various interesting statistics about the nodes capabilities are returned

        These are things that are not likely to between launching such as number of cores.

        Currently this includes: hostname, total ram, total swap, CPU name, number of cores the CPU has, and its frequencies
    """
    cpu_freq = psutil.cpu_freq()

    return {
        # TODO: Consider making this an object
        'hostname': socket.gethostname(),
        'ram': psutil.virtual_memory().total,
        'swap': psutil.swap_memory().total,
        'cpu': platform.processor(),
        'cpu_cores': multiprocessing.cpu_count(),
        'cpu_frequency_max': cpu_freq.max,
        'cpu_frequency_min': cpu_freq.min
    }


def get_current_node_vitals():
    """When called various statistics about the node in its current state are returned

        These are things that are expected to change minute to minute.

        Currently this includes cpu percentage, cpu frequency, ram available and swap available.
    """

    return {
        # TODO: Consider making this an object.
        'cpu_percentage': psutil.cpu_percent(1),
        'cpu_frequency': psutil.cpu_freq().current,
        'ram_free': psutil.virtual_memory().free,
        'swap_free': psutil.swap_memory().free,
        # TODO: Store temps, fans, and battery details if available?
    }

