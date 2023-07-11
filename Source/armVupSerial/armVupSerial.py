from Source.armVupSerial.SerialCommunicator import SerialDataCommunicator
from Source.armVupLogs.vupLogger import ArmVupLogger


class ArmVupSerial:
    def __init__(self, queue):
        self.queue = queue
        self.log = ArmVupLogger()
        self.serialW = SerialDataCommunicator(self.log)
        self.attempts_to_send = 3

    def load_data_to_queue(self):
        self.queue.put(self.data)

    def tick_serial(self, command):
        self.data = self.serialW.send_and_get(command)
        # print(self.data)
        # self.load_data_to_queue()
