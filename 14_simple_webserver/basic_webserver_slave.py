#!/usr/bin/env python

import os
import json
import ConfigParser
from RpiCluster.MainLogger import add_file_logger, logger
from RpiCluster.RpiWebserverSlaveThread import RpiWebserverSlaveThread

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rpicluster.cfg'))

socket_port = config.getint("slave", "socket_port")
master_ip = config.get("slave", "master_ip")
webserver_host = config.get("webserver", "webserver_host")
webserver_port = config.get("webserver", "webserver_port")

add_file_logger("webserver_slave.log")

webserver_slave_thread = RpiWebserverSlaveThread(master_ip, socket_port)

webserver_slave_thread.start()


from bottle import route, run, template

@route('/')
def index():
    return template("templates/ClusterHomepage.html",
                    info=json.dumps(RpiWebserverSlaveThread.current_webserver_data, indent=4, sort_keys=True))

@route('/status.json')
def status_json():
    return template(json.dumps(RpiWebserverSlaveThread.current_webserver_data))




run(host=webserver_host, port=webserver_port)
