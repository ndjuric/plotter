#!/usr/bin/env python
import argparse
import time

from tqdm import tqdm

import serial


def main():
    SERIAL_CONNECTION = serial.Serial('/dev/ttyUSB0', 115200)
    print('Opening Serial Port')

    # Hit enter a few times to wake up
    SERIAL_CONNECTION.write(str.encode("\r\n\r\n"))
    time.sleep(2)  # Wait for initialization
    SERIAL_CONNECTION.flushInput()  # Flush startup text in serial input
    print('Sending GCode')

    cmd_gcode = 'M03 S1000'
    if cmd_gcode.isspace() is False and len(cmd_gcode) > 0:
        SERIAL_CONNECTION.write(cmd_gcode.encode() + str.encode('\n'))
        grbl_out = SERIAL_CONNECTION.readline()
        print(grbl_out.strip().decode("utf-8"))

    SERIAL_CONNECTION.write(str.encode('G0X0Y0Z0') + str.encode('\n'))
    SERIAL_CONNECTION.close()


if __name__ == '__main__':
    main()
