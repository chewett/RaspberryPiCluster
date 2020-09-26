import threading
import random
import time
import socket
import json
from MainLogger import logger
from DataPackager import create_payload, get_message, send_message
from MachineInfo import get_base_machine_info
from RpiClusterExceptions import DisconnectionException


class RpiBasicSlaveThread(threading.Thread):

    def __init__(self, master_ip, socket_port):
        threading.Thread.__init__(self)
        self.uuid = None
        self.server_address = (master_ip, socket_port)
        self.sock = None

    def run(self):
        logger.info("Starting script...")

        while True:
            logger.info("Connecting to the master...")
            connected = False
            while connected is False:
                try:
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.connect(self.server_address)
                    connected = True
                except socket.error as e:
                    logger.info("Failed to connect to master, waiting 60 seconds and trying again")
                    time.sleep(60)

            logger.info("Successfully connected to the master")

            try:
                logger.info("Sending an initial hello to master")
                send_message(self.sock, create_payload("uuid", "info"))
                message = get_message(self.sock)
                self.uuid = message['payload']
                logger.info("My assigned UUID is " + self.uuid)

                send_message(self.sock, create_payload(get_base_machine_info(), 'computer_details'))
                send_message(self.sock, create_payload("computer_details", "info"))

                message = get_message(self.sock)
                logger.info("We have information about the master " + json.dumps(message['payload']))

                while True:
                    self.perform_action()

            except DisconnectionException as e:
                logger.info("Got disconnection exception with message: " + e.message)
                logger.info("Slave will try and reconnect once master is back online")

    def perform_action(self):
        logger.info("Now sending a keepalive to the master")
        send_message(self.sock, create_payload("I am still alive, client: {num}".format(num=self.uuid)))
        time.sleep(5)



