import time
import socket
import random
import json
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.DataPackager import create_msg_payload

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
sock.send(create_msg_payload("Hello World, I am client {num}".format(num=client_number)))
while True:
    time.sleep(5)
    sock.send(create_msg_payload("I am still alive, client: {num}".format(num=client_number)))