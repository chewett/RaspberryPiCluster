import socket
import json
from RpiClusterExceptions import DisconnectionException

MESSAGE_SEPARATOR = "\r"


def create_payload(payload, payload_type="message"):
    return json.dumps({"type": payload_type, "payload": payload}) + MESSAGE_SEPARATOR


_buffered_string = ""
_buffered_messages = []


def _check_buffer_for_messages():
    global _buffered_string, _buffered_messages
    split_buffered_data = _buffered_string.split(MESSAGE_SEPARATOR)
    if len(split_buffered_data) > 1:  # If we find more than one item, there is a message
        messages_to_process = split_buffered_data[0:-1]
        for message in messages_to_process:
            _buffered_messages.append(message)

        _buffered_string = split_buffered_data[-1]


def _get_message_in_buffer():
    global _buffered_messages
    if len(_buffered_messages) > 0:
        return json.loads(_buffered_messages.pop(0))
    else:
        return None


def get_message(clientsocket):
    global _buffered_string, _buffered_messages

    message_in_buffer = _get_message_in_buffer()
    if message_in_buffer:
        return message_in_buffer

    while True:
        try:
            data = clientsocket.recv(512)  # Get at max 512 bytes of data from the client
        except socket.error:  # If we failed to get data, assume they have disconnected
            raise DisconnectionException("Failed to receive messages, client has disconnected")

        data_len = len(data)
        if data_len > 0:  # Do something if we got data
            _buffered_string += data  # Keep track of our buffered stored data

            _check_buffer_for_messages()
            message_in_buffer = _get_message_in_buffer()
            if message_in_buffer:
                return message_in_buffer
        else:
            raise DisconnectionException("No further messages received, client has disconnected")


def send_message(clientsocket, payload):
    try:
        clientsocket.send(payload)
        return True
    except socket.error:
        raise DisconnectionException("Failed to send message")

