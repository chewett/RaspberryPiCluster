import time
import datetime
from MainLogger import logger
from DataPackager import create_payload, get_message, send_message
from MachineInfo import get_base_machine_info
from RpiClusterExceptions import DisconnectionException
from RpiBasicSlaveThread import RpiBasicSlaveThread


class RpiWebserverSlaveThread(RpiBasicSlaveThread):

    current_master_details = None
    current_slave_details = None
    webserver_data_updated = None

    def perform_action(self):
        logger.info("Now sending a keepalive to the master")
        send_message(self.sock, create_payload("I am still alive, client: {num}".format(num=self.uuid)))
        send_message(self.sock, create_payload("computer_details", "info"))
        master_details = get_message(self.sock)
        send_message(self.sock, create_payload("slave_details", "info"))
        slave_details = get_message(self.sock)

        RpiWebserverSlaveThread.current_master_details = master_details['payload']
        RpiWebserverSlaveThread.current_slave_details = slave_details['payload']
        RpiWebserverSlaveThread.webserver_data_updated = datetime.datetime.now()
        time.sleep(5)



