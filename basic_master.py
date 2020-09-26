#!/usr/bin/env python2.7

import socket
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger

config = ConfigParser.ConfigParser()
config.read('rpicluster.cfg')

socket_port = config.getint("master", "socket_port")
socket_bind_ip = config.get("master", "socket_bind_ip")

add_file_logger("master.log")
logger.info("Starting script...")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((socket_bind_ip, socket_port))
socket.listen(1)

(clientsocket, address) = socket.accept()
logger.info("Got client at {address}".format(address=address))

data_len = 1
while data_len > 0:
    data = clientsocket.recv(512)
    data_len = len(data)
    if data_len > 0:
        print data
