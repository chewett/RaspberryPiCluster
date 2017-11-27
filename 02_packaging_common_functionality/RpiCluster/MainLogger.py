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

def add_file_logger(filename):
    # Create a handler to store the logs to a file
    fileHandler = logging.FileHandler(filename)
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)



logger.info("Starting script...")
