import json
import threading
import time
import uuid
from DataPackager import get_message, create_payload, send_message
from RpiClusterExceptions import DisconnectionException
from MachineInfo import get_base_machine_info
from MainLogger import logger


class RpiClusterClient(threading.Thread):

    def __init__(self, primary, clientsocket, address):
        threading.Thread.__init__(self)
        self.uuid = uuid.uuid4().hex
        self.primary = primary
        self.clientsocket = clientsocket
        self.address = address
        self.node_specifications = None

    def run(self):
        try:
            message = True
            while message:
                message = get_message(self.clientsocket)
                if message['type'] == 'message':
                    logger.info("Received message: " + message['payload'])
                elif message['type'] == 'computer_details':
                    self.node_specifications = message['payload']
                    logger.info("Received Computer specifications: " + json.dumps(self.node_specifications))
                elif message['type'] == 'info':
                    logger.info("Secondary wants to know my info about " + message['payload'])
                    if message['payload'] == 'computer_details':
                        send_message(self.clientsocket, create_payload(get_base_machine_info(), "primary_info"))
                    elif message['payload'] == 'uuid':
                        send_message(self.clientsocket, create_payload(self.uuid, "uuid"))
                    elif message['payload'] == 'secondary_details':
                        secondary_details = self.primary.get_secondary_details()
                        send_message(self.clientsocket, create_payload(secondary_details, "secondary_details"))
                    else:
                        send_message(self.clientsocket, create_payload("unknown", "bad_message"))
        except DisconnectionException as e:
            logger.info("Got disconnection exception with message: " + e.message)
            logger.info("Shutting down secondary connection handler")
            self.primary.remove_client(self)
