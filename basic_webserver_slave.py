#!/usr/bin/env python2.7

import os
import json
import ConfigParser
from RpiCluster.MainLogger import add_file_logger
from RpiCluster.RpiWebserverSlaveThread import RpiWebserverSlaveThread
from bottle import route, run, template

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

socket_port = config.getint("slave", "socket_port")
master_ip = config.get("slave", "master_ip")
webserver_host = config.get("webserver", "webserver_host")
webserver_port = config.get("webserver", "webserver_port")

add_file_logger("webserver_slave.log")

webserver_slave_thread = RpiWebserverSlaveThread(master_ip, socket_port)
webserver_slave_thread.start()


@route('/')
def index():
    return template("templates/ClusterHomepage.html",
                    masterinfo=json.dumps(RpiWebserverSlaveThread.current_master_details, indent=4, sort_keys=True),
                    slaveinfo=json.dumps(RpiWebserverSlaveThread.current_slave_details, indent=4, sort_keys=True)
                    )

run(host=webserver_host, port=webserver_port)
