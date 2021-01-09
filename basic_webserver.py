#!/usr/bin/env python3

import os
import json
import configparser
from bottle import route, run, template
from RpiCluster.MainLogger import add_file_logger
from RpiCluster.SecondaryNodes.RpiWebserverThread import RpiWebserverSecondaryThread
from RpiCluster.NodeConfig import NodeConfig

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

NodeConfig.load(config)

socket_port = config.getint("secondary", "socket_port")
primary_ip = config.get("secondary", "primary_ip")
webserver_host = config.get("webserver", "webserver_host")
webserver_port = config.get("webserver", "webserver_port")

add_file_logger("webserver.log")

webserver_secondary_thread = RpiWebserverSecondaryThread(primary_ip, socket_port)
webserver_secondary_thread.start()


@route('/')
def index():
    return template("templates/ClusterHomepage.html",
                    primaryinfo=json.dumps(RpiWebserverSecondaryThread.current_primary_details, indent=4, sort_keys=True),
                    secondaryinfo=json.dumps(RpiWebserverSecondaryThread.current_secondary_details, indent=4, sort_keys=True)
                    )


run(host=webserver_host, port=webserver_port)
