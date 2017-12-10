import time
import socket
import threading
from RpiCluster.MainLogger import add_file_logger, logger

add_file_logger("master.log")
logger.info("Starting script...")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 31415))
socket.listen(1)

(clientsocket, address) = socket.accept()
logger.info("Got client at {address}".format(address=address))

data_len = 1
while data_len > 0:
    data = clientsocket.recv(512)
    data_len = len(data)
    if data_len > 0:
        print data
