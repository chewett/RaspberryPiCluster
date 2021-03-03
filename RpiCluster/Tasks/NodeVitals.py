import psutil
import platform
import multiprocessing
import socket

from RpiCluster.Payloads.VitalsPayload import VitalsPayload
from RpiCluster.NodeConfig import NodeConfig


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

    # None unless we have a node that supports exporting this
    cpu_temperature = None
    if NodeConfig.node_type == "raspberrypi":
        #Only import this if we are a RaspberryPi node, other nodes might not have this
        from RaspberryPiVcgencmd import Vcgencmd
        vc = Vcgencmd()
        cpu_temperature = vc.get_cpu_temp()


    return VitalsPayload(
        # TODO: Store fans, and battery details if available?
        psutil.cpu_percent(1),
        psutil.cpu_freq().current,
        psutil.virtual_memory().available,
        psutil.swap_memory().free,
        cpu_temperature=cpu_temperature
    )


