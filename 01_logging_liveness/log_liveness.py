import logging
import time


logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("mainlogger.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)

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
        pass # we will do work in the future but not at the momentS
