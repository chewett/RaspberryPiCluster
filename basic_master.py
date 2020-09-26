#!/usr/bin/env python2.7

import time
from RpiCluster.MainLogger import add_file_logger, logger

add_file_logger("master.log")
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
