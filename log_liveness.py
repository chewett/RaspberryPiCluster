#!/usr/bin/env python2.7

import logging
import time

# First lets set up the formatting of the logger
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

# Get the base logger and set the default level
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a console handler to output the logging to the screen
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)

# Create a handler to store the logs to a file
fileHandler = logging.FileHandler("mainlogger.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.info("Starting script...")


def find_work_to_do():
    logger.info("Node slave still alive")
    logger.info("Looking for work to run")
    return None


while True:
    work = find_work_to_do()
    if work is None:
        logger.info("Found no jobs to perform, going to sleep again")
        time.sleep(10)
    else:
        pass # we will do work in the future but not at the moment
