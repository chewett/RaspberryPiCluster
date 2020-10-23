import threading
import time
import socket
import json
from RpiCluster.MainLogger import logger
from RpiCluster.Tasks.MachineInfo import get_base_machine_info
from RpiCluster.ConnectionHandler import ConnectionHandler
from RpiCluster.RpiClusterExceptions import DisconnectionException


class RpiBasicSecondaryThread(threading.Thread):
    """Relatively basic class to represent a "simple" secondary node that connects to the primary and performs no actions.

        Creating children from this base will allow more complex systems to be created. This inherits from thread so
        you are able to start this running and perform other processing at the same time.

        Attributes:
            uuid: A UUID to represent the secondary thread. This is assigned by the primary
            server_address: A tuple representing the IP address and port to use for the primary
            connection_handler: A connection handler object which will be used for sending/recieving messages.
    """

    def __init__(self, primary_ip, socket_port):
        threading.Thread.__init__(self)
        self.uuid = None
        self.server_address = (primary_ip, socket_port)
        self.connection_handler = None

    def run(self):
        """Base method to begin running the thread, this will connect to the primary and then repeatedly call self.perform_action"""
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

                # TODO: possibly add some way to signal to the thread that we want to stop
                while True:
                    self.perform_action()

            except DisconnectionException as e:
                logger.info("Got disconnection exception with message: " + e.message)
                logger.info("Secondary will try and reconnect once primary is back online")

    def perform_action(self):
        """This method is going to be the primary one you will override to make the node to custom exciting things"""
        logger.info("Now sending a keepalive to the primary")
        self.connection_handler.send_message("I am still alive, client: {num}".format(num=self.uuid))
        time.sleep(5)



