# s1tolua
# by ted
import os
import sys

hexc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

if len(sys.argv) < 2:
    print('usage: s1tolua.py <file> <output>\nfile: file to parse\noutput: file to output to')
else:
    #file = open(sys.argv[1], 'rb')
    table = '{'
    
    index = 0
    with open(sys.argv[1], "rb") as f:
        while (byte := f.read(1)):
            # Do stuff with byte.
            #i = i + 1
            index = index + 1
            string = str(byte).lower().strip()
            hexonly = '0' + str(byte)[3:len(str(byte))-1]
            comma = ', '
            if index == 1:
                comma = ''
            print(byte, string, hexonly)
            if len(string) > 6:
                # is a non-string hex
                table = table + comma + str(int(hexonly, 16))
            else:
                # is a character
                table = table + comma + str(int(hex(ord(string[3])), 16))
    
    table = table + '}'
    level = f"""--[[
    File from s1tolua v1
    Generated from: {sys.argv[1]}
    ! CAUTION ! s1tolua is *STILL* experimental!
    This file may as well be complete garbage data.
    by tedbasher3000
]]--
return {{
    Name = '{sys.argv[1]}';
    Act = 1;
    Chunks = {table}
}}"""
    with open(sys.argv[2], "wt") as f:
        f.write(level)
