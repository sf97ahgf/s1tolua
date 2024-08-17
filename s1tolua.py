# s1tolua v1.1
# Python script that automates the process of importing Sonic 1 Level information into Roblox using the the Sonic 1 disassembly.
# made by tedbasher3000
import os
import sys


def readbyte(byte):
    string = str(byte).lower().strip()
    hexonly = '0' + str(byte)[3:len(str(byte))-1]
    if len(string) > 6:
        # is a non-string hex
        return int(hexonly, 16)
    else:
        # is a character
        return int(hex(ord(string[3])), 16)

if len(sys.argv) < 3:
    print('usage: s1tolua.py [l/c] <file> <output>\nmode: l for Level Layout, c for Chunks \nfile: file to parse\noutput: file to output to')
else:
    table = '{'
    width = 0
    height = 0
    
    index = 0
    if sys.argv[1] == 'l':
        with open(sys.argv[2], "rb") as f:
            while (byte := f.read(1)):
                index = index + 1

                # parse header
                if index == 1:
                    width = readbyte(byte) + 1
                elif index == 2:
                    height = readbyte(byte) + 1
                elif index > 2:
                    # header done, parse level
                    if index == 3:
                        table = table + str(readbyte(byte))
                    else:
                        table = table + ', ' + str(readbyte(byte))

            table = table + '}'
            level = f"""--[[
    File from s1tolua v1.1
    Generated from: {sys.argv[2]}
    ! CAUTION ! s1tolua is *STILL* experimental!
    This file may as well be complete garbage data.
    by tedbasher3000
]]--
return {{
    Name = '{sys.argv[2][:4]}';
    Act = 1;
    Width = {str(width)};
    Height = {str(height)};
    Chunks = {table}
}}"""
        with open(sys.argv[3], "wt") as f:
            f.write(level)
            print(f"Converted {sys.argv[2]} to {sys.argv[3]}!")

    elif sys.argv[1] == 'c':
        print('e') # todo: make kosinski decompression & figure out 2 byte multi info decompression
    else:
        print("Unrecognized mode")
