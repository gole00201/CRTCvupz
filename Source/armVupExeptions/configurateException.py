class CustomException(Exception):
    pass


class LoadCfgException(CustomException):
    def __init__(self, comment):
        self.comment = comment
        super().__init__(comment)
