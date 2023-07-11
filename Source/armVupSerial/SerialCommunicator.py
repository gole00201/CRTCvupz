from Source.armVupSerial.StringParser import StringParser
import Source.armVupExeptions.serialExceptions as ex
import serial
import time
import serial.tools.list_ports as list_ports


class SerialDataCommunicator(serial.Serial):
    def __init__(self, logger):
        self.parser = StringParser()
        self.logger = logger
        self.attempts = 5
        self.get_available_com()
        super().__init__(port=self.com_port,
                         baudrate=38400,
                         bytesize=8,
                         parity='N',
                         stopbits=1,
                         timeout=0.4)

    def send_and_get(self, command):
        for cnt in range(self.attempts):
            try:
                self.send_to_serial(command)
                return self.get_from_serial()
            except (ex.GetEmptyString, ex.ParsingException):
                if cnt == self.attempts - 1:
                    raise ex.DeviceDisconnectedException('ВУП отключен')
                continue
            except serial.SerialException:
                self.handle_disconnection()

    def send_to_serial(self, command):
        if not self.write(command.encode()):
            raise ex.SendException('Не удалось отправить')

    def get_from_serial(self):
        try:
            answ = self.readline().decode()
            return self.parser.parse_answ(answ)
        except TimeoutError:
            raise ex.ReadException('Достигнут лимит таймаута')
        except UnicodeDecodeError:
            raise ex.ReadException('Не удалось декодировать ответ из utf-8')

    def get_available_com(self):
        ports = list_ports.comports()
        for port, _, _ in sorted(ports):
            if "ACM" in port:
                self.com_port = str(port)
                self.logger.info(f'Попытка подключения к {self.com_port}')
                return
        raise ex.PortNotFoundException('Не удалось найти доступный COM-порт')

    def handle_disconnection(self):
        self.logger.info(f'Устройство было отключено {self.com_port}')
        self.close()
        while True:
            try:
                time.sleep(0.5)
                self.open()
                if self.isOpen():
                    self.logger.info(f'Попытка подключения к {self.com_port}')
                    break
            except serial.SerialException:
                continue
