import datetime
from influxdb import InfluxDBClient


class RpiInfluxClient:
    """ Simple helper class which will hold the details of the RPI Influx Client and make it a little easier to use """

    def __init__(self, influxdb_host, influxdb_port, influxdb_database_prefix):

        self.influxdb_host = influxdb_host
        self.influxdb_port = influxdb_port
        self.influxdb_database_prefix = influxdb_database_prefix
        self.node_vitals_database_name = self.influxdb_database_prefix + "node_vitals"
        self.node_name = None
        # We only connect once we are ready to connect
        self.influx_client = None

    def add_node_name(self, node_name):
        self.node_name = node_name

    def connect(self):

        """ Connects to the influx db Database using their client and sets up the databases needed (if needed)"""
        self.influx_client = InfluxDBClient(self.influxdb_host, self.influxdb_port)
        self.influx_client.create_database(self.node_vitals_database_name)
        self.influx_client.create_retention_policy("node_vitals_year_rp", '365d', 3, database=self.node_vitals_database_name, default=True)

    def _write_datapoint(self, measurement, values):
        if self.node_name is None:
            # We shouldnt ever encounter this but if we do I want it to fail hard so we can debug (not a good idea for production though)
            raise Exception("Cannot write node value without node name")

        points_to_write = [
            {
                "measurement": measurement,
                "tags": {
                    "node": self.node_name
                },
                "time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "fields": values
            }
        ]

        self.influx_client.write_points(points_to_write, database=self.node_vitals_database_name)

    def log_vitals(self, vitals):
        # TODO: Write these in one write_points API call rather than lots of smaller ones

        cpu_data = {
            "frequency": vitals.cpu_frequency,
            "percentage": vitals.cpu_percentage,
        }

        if vitals.cpu_temperature:
            cpu_data['temperature'] = vitals.cpu_temperature

        self._write_datapoint("cpu", cpu_data)
        self._write_datapoint("ram", {
            "free": vitals.ram_free
        })
        self._write_datapoint("swap", {"free": vitals.swap_free})


