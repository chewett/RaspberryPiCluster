import time
import datetime
from RpiCluster.MainLogger import logger
from RpiCluster.SecondaryNodes.RpiBasicSecondaryThread import RpiBasicSecondaryThread


class RpiWebserverSecondaryThread(RpiBasicSecondaryThread):
    """Subclass of the main RpiBasicSecondaryThread which handles connecting as a webserver

        This is used to continually request data from the primary with the details of the cluster.
        Static variables in this class are used to keep track of this data and make it easily accessible
        by the webserver.
    """

    current_primary_details = None
    current_secondary_details = None
    webserver_data_updated = None

    def perform_action(self):
        logger.info("Now sending a keepalive to the primary")
        self.connection_handler.send_message("I am still alive, client: {num}".format(num=self.uuid))
        self.connection_handler.send_message("node_baseinfo", "info")
        primary_details = self.connection_handler.get_message()
        self.connection_handler.send_message("secondary_details", "info")
        secondary_details = self.connection_handler.get_message()

        RpiWebserverSecondaryThread.current_primary_details = primary_details['payload']
        RpiWebserverSecondaryThread.current_secondary_details = secondary_details['payload']
        RpiWebserverSecondaryThread.webserver_data_updated = datetime.datetime.now()
        time.sleep(5)



