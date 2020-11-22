import json
import threading
import uuid
from RpiCluster.RpiClusterExceptions import DisconnectionException
from RpiCluster.Tasks.NodeVitals import get_node_baseinfo
from RpiCluster.MainLogger import logger
from RpiCluster.ConnectionHandler import ConnectionHandler
from RpiCluster.Payloads.VitalsPayload import VitalsPayload


class RpiClusterClient(threading.Thread):
    """This class is used to handle each secondary node that connects to the primary.

        When running this will continually get messages from the secondary node and return a response
        in some form.

        Attributes:
            uuid: A random UUID created for the node to give everyone a random ID
            primary: a reference to the primary to get information from it
            connection_handler: A handler that manages receiving and sending messages in the payload format
            address: Address of the client
            node_specifications: Details of the node if it provides it

    """

    def __init__(self, primary, clientsocket, address, new_influx_client):
        threading.Thread.__init__(self)
        self.influx_client = new_influx_client
        self.influx_client.connect()
        self.uuid = uuid.uuid4().hex
        self.primary = primary
        self.connection_handler = ConnectionHandler(clientsocket)
        self.address = address
        self.node_specifications = None
        self.current_vitals = None

    def run(self):
        """Method that runs handling the secondary and serving all of its messages"""
        try:
            message = True
            while message:
                message = self.connection_handler.get_message()
                if message['type'] == 'message':
                    logger.info("Received message: " + message['payload'])
                elif message['type'] == 'node_baseinfo':
                    self.node_specifications = message['payload']
                    self.influx_client.add_node_name(self.node_specifications['hostname'])
                    logger.info("Received Node Baseinfo: " + json.dumps(self.node_specifications))
                elif message['type'] == 'vitals':
                    self.current_vitals = VitalsPayload.load_payload(message['payload'])
                    self.influx_client.log_vitals(self.current_vitals)
                elif message['type'] == 'info':
                    logger.info("Secondary wants to know my info about " + message['payload'])
                    if message['payload'] == 'node_baseinfo':
                        self.connection_handler.send_message(get_node_baseinfo(), "primary_info")
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
