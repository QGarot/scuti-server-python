from typing import Union

from communication.outgoing.message_composer import MessageComposer
from network.binary.request import Request
import struct

from network.binary.response import Response


def parse(response, connection):
    """
    Parse incoming data from client
    :param response: the message to parse
    :param connection: the connection
    """

    if response[0] == 60:
        connection.socket.send(encode("<?xml version=\"1.0\"?>\r\n"
                     + "<!DOCTYPE cross-domain-policy SYSTEM \"/xml/dtds/cross-domain-policy.dtd\">\r\n"
                     + "<cross-domain-policy>\r\n"
                     + "<allow-access-from domain=\"*\" to-ports=\"*\" />\r\n"
                     + "</cross-domain-policy>\0"))
    else:
        stream = Request(connection.recv(struct.unpack_from(">i", response, 0)[0]))
        message_header = stream.read_short()

        return message_header, stream


def encode(message: Union[MessageComposer, str, Response]):
    """
    Return outcoming data from client
    :param message:
    """

    # Convert string to bytes
    if type(message) is str:
        return message.encode()

    # Build message in bytes for client from response class
    elif type(message) is Response:
        return message.get_buffer()

    # Assume this is a composer class
    # Build message in bytes for clients from composer
    else:
        message.compose()
        return message.response.get_buffer()
