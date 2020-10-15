

class DisconnectionException(Exception):
    """ Exception to use when there is an issue and the other end has disconnected from the socket """

    def __init__(self, message):
        self.message = message

