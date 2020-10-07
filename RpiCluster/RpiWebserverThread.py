import time
import datetime
from MainLogger import logger
from DataPackager import create_payload, get_message, send_message
from MachineInfo import get_base_machine_info
from RpiClusterExceptions import DisconnectionException
from RpiBasicSecondaryThread import RpiBasicSecondaryThread


class RpiWebserverSecondaryThread(RpiBasicSecondaryThread):

    current_primary_details = None
    current_secondary_details = None
    webserver_data_updated = None

    def perform_action(self):
        logger.info("Now sending a keepalive to the primary")
        send_message(self.sock, create_payload("I am still alive, client: {num}".format(num=self.uuid)))
        send_message(self.sock, create_payload("computer_details", "info"))
        primary_details = get_message(self.sock)
        send_message(self.sock, create_payload("secondary_details", "info"))
        secondary_details = get_message(self.sock)

        RpiWebserverSecondaryThread.current_primary_details = primary_details['payload']
        RpiWebserverSecondaryThread.current_secondary_details = secondary_details['payload']
        RpiWebserverSecondaryThread.webserver_data_updated = datetime.datetime.now()
        time.sleep(5)



