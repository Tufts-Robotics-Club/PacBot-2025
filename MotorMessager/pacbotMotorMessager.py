#!/usr/bin/env python

# Module for communicating with Nucleo for motor control

import serial
import struct
import ctypes

class MotorMsgProtocol:
    def __init__(self, port, buadrate = 9600):
        """
        To find port: `ls -l /dev`
        Look for what Serial0 and Serial1 are symlinked to
        """
        self.PORT = port
        self.BUADRATE = buadrate
        self.ser = serial.Serial(PORT, BUADRATE)

    def send(self, direction: ctypes.c_uint8, speed: ctypes.c_uint8):
        """
        Message Format:
        0: Forward
        1: Backwards
        2: Left
        3: Right
        Speed: 0-255
        """
        direction = ctypes.c_uint8(direction)
        speed = ctypes.c_uint8(speed)


        msg = struct.pack('>BB', direction.value, speed.value)
        self.ser.write(msg)

    def receive(self):
        pass
