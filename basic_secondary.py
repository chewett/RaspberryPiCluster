#!/usr/bin/env python2.7

import os
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.RpiBasicSecondaryThread import RpiBasicSecondaryThread

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

socket_port = config.getint("secondary", "socket_port")
primary_ip = config.get("secondary", "primary_ip")

add_file_logger("secondary.log")

basic_secondary_thread = RpiBasicSecondaryThread(primary_ip, socket_port)

basic_secondary_thread.start()
