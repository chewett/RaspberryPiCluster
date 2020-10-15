import json
import socket
from RpiCluster.RpiClusterExceptions import DisconnectionException

_MESSAGE_SEPARATOR = "\r"


class ConnectionHandler:
    """Class to handle sending and recieving messages from a socket

    Attributes:
        sock: socket object representing the connection
        _buffered_string: A string buffer that holds all characters recieved from the socket not yet converted to messages
        _buffered_messages: An array of messages recieved and ready to be consumed
    """

    def __init__(self, sock):
        self.sock = sock
        self._buffered_string = ""
        self._buffered_messages = []

    def _check_buffer_for_messages(self):
        """Private method to parse the current string buffer for messages and store them if found"""
        split_buffered_data = self._buffered_string.split(_MESSAGE_SEPARATOR)
        if len(split_buffered_data) > 1:  # If we find more than one item, there is a message
            messages_to_process = split_buffered_data[0:-1]
            for message in messages_to_process:
                self._buffered_messages.append(message)

            self._buffered_string = split_buffered_data[-1]

    def _get_message_in_buffer(self):
        """Looks in the buffer to find messages, if it finds one it pops it off otherwise it returns None"""
        if len(self._buffered_messages) > 0:
            return json.loads(self._buffered_messages.pop(0))
        else:
            return None

    def get_message(self):
        """Gets a single message from the socket, blocks if no messages available"""
        message_in_buffer = self._get_message_in_buffer()
        if message_in_buffer:
            return message_in_buffer

        while True:
            try:
                data = self.sock.recv(512)  # Get at max 512 bytes of data from the client
            except socket.error:  # If we failed to get data, assume they have disconnected
                raise DisconnectionException("Failed to receive messages, client has disconnected")

            data_len = len(data)
            if data_len > 0:  # Do something if we get data
                self._buffered_string += data.decode("utf-8")  # Keep track of our buffered stored data

                self._check_buffer_for_messages()
                message_in_buffer = self._get_message_in_buffer()
                if message_in_buffer:
                    return message_in_buffer
            else:
                raise DisconnectionException("No further messages received, client has disconnected")

    def send_message(self, payload, payload_type="message"):
        """Prepares and sends a payload to the along the socket"""
        payload = json.dumps({"type": payload_type, "payload": payload}) + _MESSAGE_SEPARATOR

        try:
            self.sock.send(payload.encode("utf-8"))
            return True
        except socket.error:
            raise DisconnectionException("Failed to send message")





