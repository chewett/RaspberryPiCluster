#!/usr/bin/env python3

import os
import configparser
from RpiCluster.MainLogger import add_file_logger
from RpiCluster.SecondaryNodes.RpiBasicSecondaryThread import RpiBasicSecondaryThread
from RpiCluster.NodeConfig import NodeConfig

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

NodeConfig.load(config)

socket_port = config.getint("secondary", "socket_port")
primary_ip = config.get("secondary", "primary_ip")

add_file_logger("secondary.log")

# This class creates and runs a basic secondary thread
basic_secondary_thread = RpiBasicSecondaryThread(primary_ip, socket_port)
basic_secondary_thread.start()

