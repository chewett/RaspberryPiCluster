import json
import threading
import uuid
from RpiCluster.RpiClusterExceptions import DisconnectionException
from RpiCluster.MachineInfo import get_base_machine_info
from RpiCluster.MainLogger import logger
from RpiCluster.ConnectionHandler import ConnectionHandler


class RpiClusterClient(threading.Thread):

    def __init__(self, primary, clientsocket, address):
        threading.Thread.__init__(self)
        self.uuid = uuid.uuid4().hex
        self.primary = primary
        self.connection_handler = ConnectionHandler(clientsocket)
        self.address = address
        self.node_specifications = None

    def run(self):
        try:
            message = True
            while message:
                message = self.connection_handler.get_message()
                if message['type'] == 'message':
                    logger.info("Received message: " + message['payload'])
                elif message['type'] == 'computer_details':
                    self.node_specifications = message['payload']
                    logger.info("Received Computer specifications: " + json.dumps(self.node_specifications))
                elif message['type'] == 'info':
                    logger.info("Secondary wants to know my info about " + message['payload'])
                    if message['payload'] == 'computer_details':
                        self.connection_handler.send_message(get_base_machine_info(), "primary_info")
                    elif message['payload'] == 'uuid':
                        self.connection_handler.send_message(self.uuid, "uuid")
                    elif message['payload'] == 'secondary_details':
                        secondary_details = self.primary.get_secondary_details()
                        self.connection_handler.send_message(secondary_details, "secondary_details")
                    else:
                        self.connection_handler.send_message("unknown", "bad_message")
        except DisconnectionException as e:
            logger.info("Got disconnection exception with message: " + e.message)
            logger.info("Shutting down secondary connection handler")
            self.primary.remove_client(self)
