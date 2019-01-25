import time
import random
import ConfigParser
import socket
import json
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.DataPackager import create_payload, get_message, send_message
from RpiCluster.MachineInfo import get_base_machine_info
from RpiCluster.RpiClusterExceptions import DisconnectionException

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

try:
    logger.info("Sending an initial hello to master")
    send_message(sock, create_payload(get_base_machine_info(), 'computer_details'))
    send_message(sock, create_payload("computer_details", "info"))

    message = get_message(sock)
    logger.info("We have information about the master " + json.dumps(message['payload']))

    while True:
        logger.info("Now sending a keepalive to the master")
        send_message(sock, create_payload("I am still alive, client: {num}".format(num=client_number)))
        time.sleep(5)

except DisconnectionException as e:
    logger.info("Got disconnection exception with message: " + e.message)
    logger.info("Shutting down slave")
