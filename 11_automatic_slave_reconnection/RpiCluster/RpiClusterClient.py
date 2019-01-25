import json
import threading
import time
from DataPackager import get_message, create_payload, send_message
from RpiClusterExceptions import DisconnectionException
from MachineInfo import get_base_machine_info
from MainLogger import logger


class RpiClusterClient(threading.Thread):

    def __init__(self, clientsocket, address):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.address = address

    def run(self):
        try:
            message = True
            while message:
                message = get_message(self.clientsocket)
                if message['type'] == 'message':
                    logger.info("Received message: " + message['payload'])
                elif message['type'] == 'computer_details':
                    logger.info("Computer specifications: " + json.dumps(message['payload']))
                elif message['type'] == 'info':
                    logger.info("Slave wants to know my info about " + message['payload'])
                    if message['payload'] == 'computer_details':
                        send_message(self.clientsocket, create_payload(get_base_machine_info(), "master_info"))
                    else:
                        send_message(self.clientsocket, create_payload("unknown", "bad_message"))
        except DisconnectionException as e:
            logger.info("Got disconnection exception with message: " + e.message)
            logger.info("Shutting down slave connection handler")
