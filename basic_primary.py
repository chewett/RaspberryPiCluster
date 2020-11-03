#!/usr/bin/env python3

import os
import configparser
from RpiCluster.MainLogger import add_file_logger
from RpiCluster.PrimaryNodes.RpiPrimary import RpiPrimary

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

socket_port = config.getint("primary", "socket_port")
socket_bind_ip = config.get("primary", "socket_bind_ip")

add_file_logger("primary.log")

# The RpiPrimary class handles all of the interesting bits of work that the primary performs
primary = RpiPrimary(socket_bind_ip, socket_port)
primary.start()

