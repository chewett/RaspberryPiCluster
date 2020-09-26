#!/usr/bin/env python2.7

import os
import socket
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.RpiMaster import RpiMaster

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

socket_port = config.getint("master", "socket_port")
socket_bind_ip = config.get("master", "socket_bind_ip")

add_file_logger("master.log")

master = RpiMaster(socket_bind_ip, socket_port)
master.start()

