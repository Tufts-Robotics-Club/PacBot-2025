#!/usr/bin/env python

# Module for communicating with Nucleo for motor control

import serial
import struct


class MotorMsgProtocol:
    def __init__(self, port, buadrate = 9600):
        """
        To find port: `ls -l /dev`
        Look for what Serial0 and Serial1 are symlinked to
        """
        self.PORT = port
        self.BUADRATE = buadrate
        self.ser = serial.Serial(PORT, BUADRATE)

    def send(self, direction: str, speed: float):
        """
        Message Format:
        |{F,B,L,R}|Speed [0..1]|
        """
        string_length = len(direction)
        format_string = f">B{string_length}sf"
        msg = struct.pack(format_string, string_length, text.encode('ascii'), speed)
        self.ser.write(msg)

    def receive(self):
        pass
