import time
import datetime
import socket
from MainLogger import logger

from RpiClusterClient import RpiClusterClient


class RpiPrimary:

    def __init__(self, socket_bind_ip, socket_port):
        self.socket_bind_ip = socket_bind_ip
        self.socket_port = socket_port
        self.connected_clients = {}

    def start(self):
        logger.info("Starting script...")

        listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listening_socket.bind((self.socket_bind_ip, self.socket_port))

        listening_socket.listen(10)  # listen to 10 connects
        while True:
            (clientsocket, address) = listening_socket.accept()
            logger.info("Got client at {address}".format(address=address))

            rpi_client = RpiClusterClient(self, clientsocket, address)
            self.connected_clients[rpi_client.uuid] = rpi_client
            rpi_client.start()

    def remove_client(self, rpi_client):
        del self.connected_clients[rpi_client.uuid]

    def get_secondary_details(self):
        secondary_details = {}
        for uuid in self.connected_clients:
            secondary_details[uuid] = {
                "uuid": uuid,
                "address": str(self.connected_clients[uuid].address[0]) + ":" + str(self.connected_clients[uuid].address[1]),

            }

        return secondary_details

