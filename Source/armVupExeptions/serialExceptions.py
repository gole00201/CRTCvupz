class CustomExeption(Exception):
    pass


class SendException(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)


class ReadException(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)


class LoseComConnetion(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)


class ParsingException(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)


class GetEmptyString(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)


class PortNotFoundException(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)


class DeviceDisconnectedException(CustomExeption):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)
