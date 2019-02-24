#!/usr/bin/env python

import socket
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.RpiClusterClient import RpiClusterClient

config = ConfigParser.ConfigParser()
config.read('rpicluster.cfg')

socket_port = config.getint("master", "socket_port")
socket_bind_ip = config.get("master", "socket_bind_ip")

add_file_logger("master.log")
logger.info("Starting script...")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((socket_bind_ip, socket_port))

socket.listen(10) #listen to 10 connects
while True:
    (clientsocket, address) = socket.accept()
    logger.info("Got client at {address}".format(address=address))

    rpiClient = RpiClusterClient(clientsocket, address)
    rpiClient.start()



