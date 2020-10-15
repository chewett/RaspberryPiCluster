import threading
import time
import socket
import json
from RpiCluster.MainLogger import logger
from RpiCluster.Tasks.MachineInfo import get_base_machine_info
from RpiCluster.ConnectionHandler import ConnectionHandler
from RpiCluster.RpiClusterExceptions import DisconnectionException


class RpiBasicSecondaryThread(threading.Thread):

    def __init__(self, primary_ip, socket_port):
        threading.Thread.__init__(self)
        self.uuid = None
        self.server_address = (primary_ip, socket_port)
        self.connection_handler = None

    def run(self):
        logger.info("Starting script...")

        while True:
            logger.info("Connecting to the primary...")
            connected = False
            while connected is False:
                try:
                    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connection.connect(self.server_address)
                    self.connection_handler = ConnectionHandler(connection)
                    connected = True
                except socket.error as e:
                    logger.info("Failed to connect to primary, waiting 60 seconds and trying again")
                    time.sleep(60)

            logger.info("Successfully connected to the primary")

            try:
                logger.info("Sending an initial hello to primary")
                self.connection_handler.send_message("uuid", "info")
                message = self.connection_handler.get_message()
                self.uuid = message['payload']
                logger.info("My assigned UUID is " + self.uuid)

                self.connection_handler.send_message(get_base_machine_info(), 'computer_details')
                self.connection_handler.send_message("computer_details", "info")

                message = self.connection_handler.get_message()
                logger.info("We have information about the primary " + json.dumps(message['payload']))

                while True:
                    self.perform_action()

            except DisconnectionException as e:
                logger.info("Got disconnection exception with message: " + e.message)
                logger.info("Secondary will try and reconnect once primary is back online")

    def perform_action(self):
        logger.info("Now sending a keepalive to the primary")
        self.connection_handler.send_message("I am still alive, client: {num}".format(num=self.uuid))
        time.sleep(5)



