import json
import threading
from DataPackager import get_message, create_payload
from MachineInfo import get_base_machine_info
from MainLogger import logger


class RpiClusterClient(threading.Thread):

    def __init__(self, clientsocket, address):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.address = address

    def run(self):
        message = True
        while message:
            message = get_message(self.clientsocket)
            if message:
                if message['type'] == 'message':
                    logger.info("Received message: " + message['payload'])
                elif message['type'] == 'computer_details':
                    logger.info("Computer specifications: " + json.dumps(message['payload']))
                elif message['type'] == 'info':
                    logger.info("Slave wants to know my info about " + message['payload'])
                    if message['payload'] == 'computer_details':
                        self.clientsocket.send(create_payload(get_base_machine_info(), "master_info"))
                    else:
                        self.clientsocket.send(create_payload("unknown", "bad_message"))

            else:
                logger.info("Client disconnected at address {addr}".format(addr=self.address))

