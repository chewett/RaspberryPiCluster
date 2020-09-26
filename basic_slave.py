#!/usr/bin/env python2.7

import os
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.RpiBasicSlaveThread import RpiBasicSlaveThread

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

socket_port = config.getint("slave", "socket_port")
master_ip = config.get("slave", "master_ip")

add_file_logger("slave.log")

basic_slave_thread = RpiBasicSlaveThread(master_ip, socket_port)

basic_slave_thread.start()

