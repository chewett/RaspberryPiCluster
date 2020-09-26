#!/usr/bin/env python2.7

import socket
import ConfigParser
import json
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.DataPackager import get_message, create_payload
from RpiCluster.MachineInfo import get_base_machine_info

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

message = True
while message:
    message = get_message(clientsocket)
    if message:
        if message['type'] == 'message':
            logger.info("Received message: " + message['payload'])
        elif message['type'] == 'computer_details':
            logger.info("Computer specifications: " + json.dumps(message['payload']))
        elif message['type'] == 'info':
            logger.info("Slave wants to know my info about " + message['payload'])
            if message['payload'] == 'computer_details':
                clientsocket.send(create_payload(get_base_machine_info(), "master_info"))
            else:
                clientsocket.send(create_payload("unknown", "bad_message"))

    else:
        logger.info("Client disconnected")