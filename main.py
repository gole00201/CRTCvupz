from Source.armVupSerial.armVupSerial import ArmVupSerial


armSerial = ArmVupSerial('queue')
while 1:
    armSerial.tick_serial('bmk:009:getStatus\r\n')
    print(armSerial.data)
