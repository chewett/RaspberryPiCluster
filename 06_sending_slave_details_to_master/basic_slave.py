import time
import random
import psutil
import ConfigParser
import multiprocessing
import platform
import socket
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.DataPackager import create_payload

config = ConfigParser.ConfigParser()
config.read('rpicluster.cfg')

socket_port = config.getint("slave", "socket_port")
master_ip = config.get("slave", "master_ip")


add_file_logger("slave.log")
logger.info("Starting script...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info("Connecting to the master...")
server_address = (master_ip, socket_port)
sock.connect(server_address)

client_number = random.randint(1, 100000)

logger.info("Sending an initial hello to master")


machine_details = {
    'hostname': socket.gethostname(),
    'cpu_percent_used': psutil.cpu_percent(1),
    'ram': psutil.virtual_memory().total,
    'cpu': platform.processor(),
    'cpu_cores': multiprocessing.cpu_count()
}


sock.send(create_payload(machine_details, 'computer_details'))
while True:
    time.sleep(5)
    sock.send(create_payload("I am still alive, client: {num}".format(num=client_number)))