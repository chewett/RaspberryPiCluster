#!/usr/bin/env python2.7

import time
import socket
import random
from RpiCluster.MainLogger import add_file_logger, logger

add_file_logger("slave.log")
logger.info("Starting script...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info("Connecting to the master...")
server_address = ('localhost', 31415)
sock.connect(server_address)

client_number = random.randint(1, 100000)

logger.info("Sending an initial hello to master")
sock.send("Hello World, I am client {num}".format(num=client_number))
while True:
    time.sleep(5)
    sock.send("I am still alive, client: {num}".format(num=client_number))