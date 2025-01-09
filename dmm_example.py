#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2017 uberdaff
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import pt3430
from time import sleep

def main(args):
        dmm = pt3430.pt3430Instrument('/dev/tty.usbserial-0001')
        if dmm.isConnected == True:
                for reading in range(5):
                        print('-------------------------------------')
                        print(f'Starting Reading {reading+1}')
                        print(f'Reading {reading+1} Value:\t{dmm.getValue()}V')
                        sleep(1)
                #print(dmm.getValueString())
                #print(dmm.status)
                dmm.close()
        else:
                print('Failed to read device')
        return 0

import sys
sys.exit(main(sys.argv))

for index, byte in enumerate(string):
        hexadecimal = format(ord(byte), "#04x")
        binary = format(ord(byte),"#010b")
        print(f'Byte {index}: \t{hexadecimal}\t{binary}')
