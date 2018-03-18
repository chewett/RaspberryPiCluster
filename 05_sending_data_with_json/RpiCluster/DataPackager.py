import json

MESSAGE_SEPARATOR = "\r"

def create_msg_payload(message):
    return json.dumps({'msg': message}) + MESSAGE_SEPARATOR


_buffered_string = ""
_buffered_messages = []


def get_message(clientsocket):
    global _buffered_string, _buffered_messages
    data_len = 1
    #Continue while we get data
    while data_len > 0:
        data = clientsocket.recv(512) #Get at max 512 bytes of data from the client
        data_len = len(data)
        if data_len > 0: #Do something if we got data
            _buffered_string += data #Keep track of our buffered stored data

            split_buffered_data = _buffered_string.split(MESSAGE_SEPARATOR)
            if len(split_buffered_data) > 1: #If we find more than one item, there is a message
                messages_to_process = split_buffered_data[0:-1]
                for message in messages_to_process:
                    _buffered_messages.append(message)

                _buffered_string = split_buffered_data[-1]
                return json.loads(_buffered_messages.pop(0))

