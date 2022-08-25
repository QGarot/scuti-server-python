import struct


class Request:
    def __init__(self, buffer):
        self.buffer = buffer
        self.index = 0

    def read_short(self):
        """
        Read 16 bits as a integer
        :return: integer
        """
        num = struct.unpack_from(">h", self.buffer, self.index)[0]
        self.index += 2
        return int(num)

    def read_int(self):
        """
        Read 32 bits as integer
        :return: integer
        """
        num = struct.unpack_from(">i", self.buffer, self.index)[0]
        self.index += 4
        return int(num)

    def read_string(self):
        """
        Read string encoded in UTF-8 from packet with int16 prefix
        :return: string
        """
        str_length = self.read_short()
        str = self.get_as_string()[self.index:self.index + str_length]
        self.index += str_length
        return str

    def get_as_string(self):
        """
        Get received packet as string in ISO-8859-1 encoding
        :return: packet as string
        """
        return self.buffer.decode("ISO-8859-1")

    def get_message_as_readable_string(self):
        """
        Get received packet as string in ISO-8859-1 encoding with replaced charaacters
        :return: packet as string
        """
        _message = self.buffer.decode("ISO-8859-1")[2:]

        for char in range(0, 14):
            _message = _message.replace(chr(char), "{" + str(char) + "}")

        return _message