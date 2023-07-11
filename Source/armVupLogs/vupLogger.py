import logging
import sys


class ArmVupLogger:
    def __init__(self):
        self.logger = self.create_logger()

    def create_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(message)s')
        stdout_hendler = logging.StreamHandler(sys.stdout)
        stdout_hendler.setFormatter(formatter)
        logger.addHandler(stdout_hendler)
        return logger

    def debug(self, massege):
        self.logger.debug(massege)

    def info(self, massege):
        self.logger.info(massege)

    def error(self, massege):
        self.logger.error(massege)

    def critical(self, massege):
        self.logger.critical(massege)
