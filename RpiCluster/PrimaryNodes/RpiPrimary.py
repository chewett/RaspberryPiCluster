import socket
from RpiCluster.MainLogger import logger
from RpiCluster.RpiClusterClient import RpiClusterClient
from RpiCluster.RpiInfluxClient import RpiInfluxClient


class RpiPrimary:
    """Class to create a primary node which will handle connections coming in from a secondary

        This will form the basis of a general primary node which will be in charge of listening for connections
        and handling each one.

        Attributes:
            socket_bind_ip: IP address to bind the listening socket server to
            socket_port: Port number to bind the listening socket server to
            connected_clients: Dict of connected clients
    """

    def __init__(self, socket_bind_ip, socket_port, influxdb_host, influxdb_port, influxdb_database_prefix):
        self.socket_bind_ip = socket_bind_ip
        self.socket_port = socket_port
        self.influxdb_host = influxdb_host
        self.influxdb_port = influxdb_port
        self.influxdb_database_prefix = influxdb_database_prefix

        self.connected_clients = {}
        self.influx_client = None

    def start(self):
        """Set up the primary to handle the various responsibilities"""
        logger.info("Starting primary...")



        # Start the handling of the secondary nodes
        listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listening_socket.bind((self.socket_bind_ip, self.socket_port))

        listening_socket.listen(10)  # listen to 10 connects
        while True:
            (clientsocket, address) = listening_socket.accept()
            logger.info("Got client at {address}".format(address=address))

            new_influx_client = RpiInfluxClient(self.influxdb_host, self.influxdb_port, self.influxdb_database_prefix)
            rpi_client = RpiClusterClient(self, clientsocket, address, new_influx_client)
            self.connected_clients[rpi_client.uuid] = rpi_client
            rpi_client.start()

    def remove_client(self, rpi_client):
        """Removes a given client from the list of connected clients, typically called after disconnection"""
        del self.connected_clients[rpi_client.uuid]

    def get_secondary_details(self):
        """Allows retrieving some basic information of every secondary connected to the primary"""
        secondary_details = {}
        for uuid in self.connected_clients:
            secondary_details[uuid] = {
                "uuid": uuid,
                "address": str(self.connected_clients[uuid].address[0]) + ":" + str(self.connected_clients[uuid].address[1]),
            }

        return secondary_details

