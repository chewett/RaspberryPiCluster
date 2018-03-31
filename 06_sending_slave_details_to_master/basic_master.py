import socket
import ConfigParser
import json
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.DataPackager import MESSAGE_SEPARATOR, get_message

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
        elif message['type'] == 'machine_details':
            logger.info("Machine specifications: " + json.dumps(message['payload']))
        else:
            logger.warning("Unknown payload type {type}, payload content {content}".format(
                type=message['type'], content=message['payload']
            ))

    else:
        logger.info("Client disconnected")